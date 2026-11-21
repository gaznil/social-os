"""Reel Radar & Inspiration Inbox helpers.

Normalizes pasted social media URLs, detects platform, evaluates shelf-life
expiry ('update' | 'trend' | 'evergreen'), and scores saved reels/posts on a
deterministic 0-100 scale (virality/outlier, hook strength, niche fit &
relatability, first-mover advantage, production effort, and live urgency) to
recommend P1 / P2 / P3 / Skip / Expired.
"""

from datetime import datetime, timedelta, timezone
import re
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


_TRACKING_EXACT = frozenset({
    "fbclid",
    "gclid",
    "igsh",
    "igshid",
    "si",
    "s",
    "t",
    "ref",
    "ref_src",
    "ref_url",
    "feature",
    "pp",
    "rcm",
    "trk",
})

_URL_RE = re.compile(r"https?://[^\s<>\"')]+", re.IGNORECASE)
_IG_SHORTCODE_RE = re.compile(r"^/(?:p|reel|reels|tv)/([A-Za-z0-9_-]+)", re.IGNORECASE)

_DEFAULT_SHELF_HOURS = {
    "update": 48,
    "trend": 168,  # 7 days
    "evergreen": None,
}


def detect_platform(url):
    host = (urlparse(str(url or "").strip()).netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    if "instagram.com" in host or "instagr.am" in host:
        return "instagram"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    if host in ("x.com", "twitter.com", "mobile.twitter.com"):
        return "x"
    if "linkedin.com" in host:
        return "linkedin"
    if "tiktok.com" in host:
        return "tiktok"
    if "threads.net" in host:
        return "threads"
    if "facebook.com" in host or "fb.watch" in host:
        return "facebook"
    if "github.com" in host:
        return "github"
    if "reddit.com" in host or "redd.it" in host:
        return "reddit"
    if "news.ycombinator.com" in host:
        return "hackernews"
    return "web"


def _is_tracking_param(key):
    k = key.lower()
    return k in _TRACKING_EXACT or k.startswith("utm_")


def normalize_url(raw):
    text = str(raw or "").strip()
    if not text:
        return ""
    parsed = urlparse(text)
    if not parsed.scheme or not parsed.netloc:
        return text

    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    if host in ("twitter.com", "mobile.twitter.com"):
        host = "x.com"
    elif host == "instagr.am":
        host = "instagram.com"

    path = re.sub(r"/+", "/", parsed.path or "/")
    kept = [
        (k, v)
        for k, v in parse_qsl(parsed.query, keep_blank_values=False)
        if not _is_tracking_param(k)
    ]

    if host == "instagram.com":
        m = _IG_SHORTCODE_RE.match(path)
        if m:
            path = f"/reel/{m.group(1)}"

    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]

    query = urlencode(kept)
    return urlunparse((parsed.scheme.lower(), host, path, "", query, ""))


def extract_urls(text):
    seen = set()
    results = []
    for match in _URL_RE.findall(str(text or "")):
        cleaned = normalize_url(match.rstrip(".,;!]"))
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            results.append({"url": cleaned, "platform": detect_platform(cleaned)})
    return results


def _parse_iso(ts):
    if not ts:
        return None
    if isinstance(ts, datetime):
        return ts if ts.tzinfo else ts.replace(tzinfo=timezone.utc)
    s = str(ts).strip()
    if not s:
        return None
    try:
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        dt = datetime.fromisoformat(s)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def check_expiry(item, now=None):
    """Evaluate shelf-life status for an inspiration, option, script, or post.

    Returns dict with:
      - shelfLife: 'update' | 'trend' | 'evergreen'
      - state: 'evergreen' | 'active' | 'expiring_today' | 'expired'
      - hoursLeft: int or None
      - daysLeft: int or None
    """
    item = item or {}
    shelf = str(item.get("shelfLife") or "evergreen").lower()
    if shelf not in _DEFAULT_SHELF_HOURS:
        shelf = "evergreen"

    now_dt = _parse_iso(now) or datetime.now(timezone.utc)
    exp_dt = _parse_iso(item.get("expiresAt"))

    if exp_dt is None and _DEFAULT_SHELF_HOURS[shelf] is not None:
        created_dt = _parse_iso(item.get("createdAt"))
        if created_dt is not None:
            exp_dt = created_dt + timedelta(hours=_DEFAULT_SHELF_HOURS[shelf])

    if shelf == "evergreen" and exp_dt is None:
        return {
            "shelfLife": "evergreen",
            "state": "evergreen",
            "hoursLeft": None,
            "daysLeft": None,
        }

    if exp_dt is None:
        default_h = _DEFAULT_SHELF_HOURS.get(shelf) or 168
        return {
            "shelfLife": shelf,
            "state": "active",
            "hoursLeft": default_h,
            "daysLeft": max(1, round(default_h / 24)),
        }

    delta_hours = (exp_dt - now_dt).total_seconds() / 3600.0
    hours_left = int(round(delta_hours))
    days_left = int(round(delta_hours / 24.0))

    if delta_hours <= 0:
        state = "expired"
    elif delta_hours <= 24:
        state = "expiring_today"
    else:
        state = "active"

    return {
        "shelfLife": shelf,
        "state": state,
        "hoursLeft": hours_left,
        "daysLeft": days_left,
    }


def _clamp(value, low, high):
    return max(low, min(high, value))


def _norm_100(value, default=65.0):
    if value is None:
        return default
    v = float(value)
    if 0.0 < v <= 10.0:
        v *= 10.0
    return _clamp(v, 0.0, 100.0)


def score_item(item, now=None):
    """Compute a deterministic 0-100 score and priority tier for a Radar item.

    Inputs read from `item`:
    - outlierMultiple (float): views / creator median views (e.g. 5.0 = 5x outlier)
    - ageDays (float): how many days ago the source post went up (default 3)
    - hookScore (float, 0-100 or 0-10): strength & transferability of the hook
    - fitScore (float, 0-100 or 0-10): fit for the account's niche & demoable truth
    - relatabilityScore (float, 0-100 or 0-10, optional): local/daily-life relatability
    - firstMover (str, optional): 'untapped' (0 in niche) | 'early' (1-2) | 'saturated'
    - shelfLife (str, optional): 'update' | 'trend' | 'evergreen'
    - expiresAt / createdAt (ISO str, optional): used to detect expired trends
    - effort (str): 'low' | 'medium' | 'high'
    - provable (bool): False if the claim cannot be demoed honestly
    """
    outlier = float(item.get("outlierMultiple") or 1.5)
    age_days = max(0.25, float(item.get("ageDays") or 3.0))
    hook = _norm_100(item.get("hookScore"), 65.0)
    fit = _norm_100(item.get("fitScore"), 70.0)
    if item.get("relatabilityScore") is not None:
        rel = _norm_100(item.get("relatabilityScore"), 70.0)
        fit = (fit * 0.65) + (rel * 0.35)
    effort = str(item.get("effort") or "medium").lower()
    provable = item.get("provable", True) is not False
    first_mover = str(item.get("firstMover") or "").lower()

    # 1. Virality & velocity (0-35)
    recency_factor = 1.15 if age_days <= 2 else (1.0 if age_days <= 7 else (0.85 if age_days <= 21 else 0.65))
    outlier_points = _clamp(outlier * 3.8 * recency_factor, 0.0, 35.0)

    # 2. Hook transferability (0-25)
    hook_points = (hook / 100.0) * 25.0

    # 3. Niche & relatability fit (0-25)
    fit_points = (fit / 100.0) * 25.0

    # 4. Effort efficiency (0-15)
    effort_map = {"low": 15.0, "medium": 10.0, "high": 5.0}
    effort_points = effort_map.get(effort, 10.0)

    # 5. First-mover bonus / saturation penalty (-8 to +8)
    fm_map = {"untapped": 8.0, "first": 8.0, "early": 4.0, "saturated": -8.0}
    fm_points = fm_map.get(first_mover, 0.0)

    expiry = check_expiry(item, now=now)
    urgency_bonus = 0.0
    if expiry["state"] in ("active", "expiring_today") and expiry["shelfLife"] in ("update", "trend"):
        urgency_bonus = 5.0 if expiry["shelfLife"] == "update" else 3.0

    total = round(_clamp(outlier_points + hook_points + fit_points + effort_points + fm_points + urgency_bonus, 0.0, 100.0))
    if not provable or fit < 30.0:
        total = min(total, 39)

    if expiry["state"] == "expired":
        tier = "expired"
    elif total >= 78:
        tier = "P1"
    elif total >= 58:
        tier = "P2"
    elif total >= 40:
        tier = "P3"
    else:
        tier = "skip"

    return {
        "score": total,
        "tier": tier,
        "shelfLife": expiry["shelfLife"],
        "expiryState": expiry["state"],
        "hoursLeft": expiry["hoursLeft"],
        "daysLeft": expiry["daysLeft"],
        "breakdown": {
            "outlier": round(outlier_points, 1),
            "hook": round(hook_points, 1),
            "fit": round(fit_points, 1),
            "effort": round(effort_points, 1),
            "firstMover": round(fm_points, 1),
            "urgency": round(urgency_bonus, 1),
        },
    }


def rank_inspirations(items, now=None):
    enriched = []
    for raw in items or []:
        copy = dict(raw)
        copy["url"] = normalize_url(copy.get("url", ""))
        copy["platform"] = copy.get("platform") or detect_platform(copy["url"])
        verdict = score_item(copy, now=now)
        copy["score"] = verdict["score"]
        copy["tier"] = verdict["tier"]
        copy["shelfLife"] = verdict["shelfLife"]
        copy["expiryState"] = verdict["expiryState"]
        copy["hoursLeft"] = verdict["hoursLeft"]
        copy["daysLeft"] = verdict["daysLeft"]
        copy["breakdown"] = verdict["breakdown"]
        enriched.append(copy)

    def _sort_key(x):
        is_expired = 1 if x.get("expiryState") == "expired" else 0
        is_live_window = 0 if (x.get("expiryState") in ("active", "expiring_today") and x.get("shelfLife") in ("update", "trend")) else 1
        return (is_expired, is_live_window, -x["score"], str(x.get("title") or ""))

    enriched.sort(key=_sort_key)
    return enriched
