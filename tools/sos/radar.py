"""Reel Radar: extract/normalize inspiration URLs and rank them by viral priority (0-100)."""
import re
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

_URL_RE = re.compile(r"https?://[^\s<>\"'\]\)]+", re.IGNORECASE)
_TRACKING_PREFIXES = ("utm_", "igsh", "si", "fbclid", "gclid", "ref", "feature", "t", "s")


def detect_platform(url):
    host = (urlparse(url).netloc or "").lower()
    if "instagram.com" in host or "instagr.am" in host:
        return "instagram"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    if "x.com" in host or "twitter.com" in host:
        return "x"
    if "linkedin.com" in host:
        return "linkedin"
    if "threads.net" in host or "threads.com" in host:
        return "threads"
    if "facebook.com" in host or "fb.watch" in host:
        return "facebook"
    return "web"


def normalize_url(raw):
    """Strip tracking query params, fragments, and trailing punctuation so duplicates match."""
    u = raw.strip().rstrip(".,;:!?)")
    p = urlparse(u)
    if not p.scheme or not p.netloc:
        return u
    kept = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=False)
            if not any(k.lower().startswith(pref) for pref in _TRACKING_PREFIXES)]
    path = re.sub(r"/+$", "", p.path) or "/"
    return urlunparse((p.scheme.lower(), p.netloc.lower(), path, "", urlencode(kept), ""))


def extract_urls(text):
    """Pull unique normalized URLs from raw chat/textarea paste, preserving order."""
    seen, out = set(), []
    for match in _URL_RE.findall(text or ""):
        norm = normalize_url(match)
        if norm and norm not in seen:
            seen.add(norm)
            out.append({"url": norm, "platform": detect_platform(norm)})
    return out


def _clamp(val, lo, hi):
    return max(lo, min(hi, val))


def score_item(item):
    """Deterministic 0-100 priority score from measured signals (no guessing).

    Weights:
      - Viral velocity / outlier multiple (0-35): >=10x = 30, >=5x = 24, >=3x = 18, >=1.5x = 10, else 4
        + freshness bonus (<=3 days: +5, <=7 days: +3, <=14 days: +1)
      - Hook strength (0-25): hookScore (0-100 from hookscore.py) scaled to 0-25 (default 12 if unmeasured)
      - Niche & realism fit (0-25): fitScore (0-100, default 60 -> 15); if provable is False -> capped at 5
      - Execution speed / ROI (0-15): effort 'low' = 15, 'medium' = 10, 'high' = 5
    """
    outlier = item.get("outlierMultiple")
    if outlier is None:
        viral_base = 12
    elif outlier >= 10:
        viral_base = 30
    elif outlier >= 5:
        viral_base = 24
    elif outlier >= 3:
        viral_base = 18
    elif outlier >= 1.5:
        viral_base = 10
    else:
        viral_base = 4

    age_days = item.get("ageDays")
    if age_days is None:
        fresh = 2
    elif age_days <= 3:
        fresh = 5
    elif age_days <= 7:
        fresh = 3
    elif age_days <= 14:
        fresh = 1
    else:
        fresh = 0
    viral = _clamp(viral_base + fresh, 0, 35)

    hook_raw = item.get("hookScore")
    hook = round(_clamp(hook_raw, 0, 100) * 0.25) if hook_raw is not None else 12

    fit_raw = item.get("fitScore")
    fit = round(_clamp(fit_raw, 0, 100) * 0.25) if fit_raw is not None else 15
    if item.get("provable") is False:
        fit = min(fit, 5)

    effort = (item.get("effort") or "medium").lower()
    speed = {"low": 15, "medium": 10, "high": 5}.get(effort, 10)

    total = _clamp(viral + hook + fit + speed, 0, 100)
    if item.get("provable") is False or total < 25:
        tier = "skip"
    elif total >= 75:
        tier = "P1"
    elif total >= 50:
        tier = "P2"
    else:
        tier = "P3"

    return {
        "id": item.get("id"),
        "url": item.get("url"),
        "score": total,
        "tier": tier,
        "breakdown": {"viral": viral, "hook": hook, "fit": fit, "speed": speed},
    }


def rank_inspirations(items):
    """Score and sort a batch of inspiration items highest priority first."""
    scored = [score_item(it) for it in items]
    return sorted(scored, key=lambda x: (-x["score"], str(x.get("id") or "")))
