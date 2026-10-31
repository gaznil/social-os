"""Results loop: best posting hours per account and the Growth tiles, from posts and daily `stats` docs."""
from collections import defaultdict
from datetime import date, timedelta

from tools.sos.queue import parse_time

IST = timedelta(hours=5, minutes=30)
MIN_POSTS = 6  # fewer posted items than this = not enough to pick times


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
            if s["date"] <= max(days):
                latest[s["accountId"]] = s["followers"]
        return sum(latest.values()) if latest else None

    now, before = followers_on(week), followers_on(prev)
    return {
        "followers": now,
        "viewsWeek": sum(s.get("views", 0) for s in rows if s["date"] in week),
        "postsWeek": sum(s.get("posts", 0) for s in rows if s["date"] in week),
        "change": None if now is None or before is None else now - before,
    }
