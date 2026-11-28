"""Results loop: best posting hours per account, Growth tiles, and Analytics Heaters (>= 2x median + 90d evergreen recycling)."""
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from statistics import median

from tools.sos.queue import parse_time

IST = timedelta(hours=5, minutes=30)
MIN_POSTS = 6  # fewer posted items than this = not enough to pick times
EVERGREEN_RECYCLE_DAYS = 90


def best_times(posts, top=3):
    by_acc = defaultdict(lambda: defaultdict(list))
    for p in posts:
        views = (p.get("metrics") or {}).get("views")
        if p.get("status") != "posted" or not p.get("postedAt") or views is None:
            continue
        hour = (parse_time(p["postedAt"]) + IST).hour
        by_acc[p["accountId"]][hour].append(views)
    result = {}
    for acc, hours in by_acc.items():
        if sum(len(v) for v in hours.values()) < MIN_POSTS:
            result[acc] = None
            continue
        ranked = sorted(hours, key=lambda h: sum(hours[h]) / len(hours[h]), reverse=True)
        result[acc] = ["%02d:00" % h for h in ranked[:top]]
    return result


def growth_tiles(stats, account_id, today):
    rows = sorted((s for s in stats if account_id in (None, "all") or s["accountId"] == account_id),
                  key=lambda s: s["date"])
    end = date.fromisoformat(today)
    week = {(end - timedelta(days=i)).isoformat() for i in range(7)}
    prev = {(end - timedelta(days=i)).isoformat() for i in range(7, 14)}

    def followers_on(days):
        latest = {}
        for s in rows:
            if s["date"] <= max(days) and s.get("followers") is not None:
                latest[s["accountId"]] = s["followers"]
        return sum(latest.values()) if latest else None

    now, before = followers_on(week), followers_on(prev)
    return {
        "followers": now,
        "viewsWeek": sum(s.get("views", 0) for s in rows if s["date"] in week),
        "postsWeek": sum(s.get("posts", 0) for s in rows if s["date"] in week),
        "change": None if now is None or before is None else now - before,
    }


def _rate(m, top, bottom="reach"):
    a, b = m.get(top), m.get(bottom)
    if a is None or not b or b <= 0:
        return None
    return a / b


def signal_rates(metrics):
    """The three numbers Instagram's head names as top ranking signals, per post.

    sharesPerReach = closest public number to 'sends per reach' (the API has no separate DM-send count).
    avgWatchSec is the raw average watch time; never turned into a % without a known video length.
    Any missing input gives None, never 0.
    """
    m = metrics or {}
    return {
        "sharesPerReach": _rate(m, "shares"),
        "likesPerReach": _rate(m, "likes"),
        "savesPerReach": _rate(m, "saves"),
        "avgWatchSec": m.get("avgWatchSec"),
        "skipRate": m.get("skipRate"),
    }


SIGNALS = ("sharesPerReach", "likesPerReach", "avgWatchSec")


def scorecard(posts):
    """Per posted item: the signal rates and each one as a multiple of the account's own median.

    Needs >= 3 posted items per account that have the signal; otherwise the multiple is None.
    The three multiples are shown separately; `signalMean` is only their plain average (for sorting).
    """
    by_acc = defaultdict(list)
    for p in posts or []:
        if p.get("status") != "posted" or not p.get("metrics"):
            continue
        by_acc[p.get("accountId") or "unknown"].append((p, signal_rates(p["metrics"])))
    out = []
    for acc, items in by_acc.items():
        meds = {}
        for s in SIGNALS:
            vals = [r[s] for _, r in items if r[s] is not None and r[s] > 0]
            meds[s] = float(median(vals)) if len(vals) >= 3 else None
        for p, r in items:
            mult = {s: (round(r[s] / meds[s], 1) if r[s] is not None and meds[s] else None) for s in SIGNALS}
            have = [v for v in mult.values() if v is not None]
            out.append({
                "id": p.get("id"), "accountId": acc, "format": p.get("format"),
                "views": (p["metrics"] or {}).get("views"),
                "rates": {k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()},
                "multiples": mult,
                "signalMean": round(sum(have) / len(have), 1) if have else None,
            })
    out.sort(key=lambda x: (x["signalMean"] is None, -(x["signalMean"] or 0)))
    return out


def find_heaters(posts, today=None):
    """Find outlier posts ('heaters') that beat >= 2x their account's median views.

    Also flags heaters posted >= 90 days ago with `evergreenRecycle = True`
    so the weekly strategy loop can remake them with a fresh hook.
    """
    today_date = date.fromisoformat(today) if today else datetime.now(timezone.utc).date()
    by_acc = defaultdict(list)
    for p in posts or []:
        views = (p.get("metrics") or {}).get("views")
        if p.get("status") != "posted" or views is None or views <= 0:
            continue
        by_acc[p.get("accountId") or "unknown"].append(p)

    heaters = []
    for acc, items in by_acc.items():
        if len(items) < 3:
            continue
        med = float(median([p["metrics"]["views"] for p in items]))
        if med <= 0:
            continue
        for p in items:
            views = float(p["metrics"]["views"])
            mult = round(views / med, 1)
            if mult < 2.0:
                continue
            age_days = 0
            if p.get("postedAt"):
                posted_dt = parse_time(p["postedAt"])
                age_days = max(0, (today_date - posted_dt.date()).days)
            shelf = str(p.get("shelfLife") or "evergreen").lower()
            heaters.append({
                "id": p.get("id"),
                "accountId": acc,
                "format": p.get("format"),
                "caption": (p.get("caption") or "")[:140],
                "views": int(views),
                "medianViews": int(round(med)),
                "multiple": mult,
                "ageDays": age_days,
                "evergreenRecycle": age_days >= EVERGREEN_RECYCLE_DAYS and shelf == "evergreen",
            })

    # additive: attach the signal multiples (shares/likes per reach, avg watch time vs own median) when known
    cards = {c["id"]: c for c in scorecard(posts)}
    for h in heaters:
        c = cards.get(h["id"])
        if c:
            h["signalMultiples"] = c["multiples"]
            h["signalMean"] = c["signalMean"]
    heaters.sort(key=lambda h: (-h["multiple"], -h["views"]))
    return heaters


SUM_FIELDS = ("views", "reach", "interactions", "profileViews", "followerGain", "posts",
              "likes", "comments", "shares", "saves")


def growth_metrics(stats, account_id, today):
    """Week totals + % vs the previous 7 days for every Growth metric.

    A field with no number in a window stays None (never 0), so the dashboard can show a dash.
    pct is None unless the previous window has data above 0. Same maths as the page's growthMetrics().
    """
    rows = [s for s in stats if account_id in (None, "all") or s["accountId"] == account_id]
    end = date.fromisoformat(today)
    week = {(end - timedelta(days=i)).isoformat() for i in range(7)}
    prev = {(end - timedelta(days=i)).isoformat() for i in range(7, 14)}

    def total(field, days):
        vals = [s[field] for s in rows if s["date"] in days and s.get(field) is not None]
        return sum(vals) if vals else None

    out = {}
    for f in SUM_FIELDS:
        cur, old = total(f, week), total(f, prev)
        pct = None if cur is None or not old else round((cur - old) / old * 100)
        out[f] = {"week": cur, "prev": old, "pct": pct}
    return out
