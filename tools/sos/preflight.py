"""Platform rule checks for one post. Returns plain-English problems; empty list = OK."""
import re

CAPTION_LIMITS = {"instagram": 2200, "facebook": 63206, "linkedin": 3000,
                  "x": 280, "threads": 500, "youtube": 5000}
_URL = re.compile(r"https?://\S+")


def _weighted_len(text):
    """X-style count: every link is 23, wide characters (CJK, emoji) count 2."""
    n = 23 * len(_URL.findall(text))
    for ch in _URL.sub("", text):
        n += 2 if ord(ch) >= 0x1100 else 1
    return n


def check(post):
    problems = []
    platform = post.get("platform")
    if platform not in CAPTION_LIMITS:
        return [f"Unknown platform: {platform}"]

    caption = post.get("caption") or ""
    media = post.get("mediaUrls") or []
    fmt = post.get("format")

    if not caption.strip():
        problems.append("Caption is empty.")
    if post.get("status") == "approved" and not post.get("approvedAt"):
        problems.append("Approved but no approval time recorded.")

    limit = CAPTION_LIMITS[platform]
    if platform == "x":
        n = _weighted_len(caption)
        if n > limit:
            problems.append(f"Post is {n} weighted characters; x allows {limit}.")
    elif len(caption) > limit:
        problems.append(f"Caption is {len(caption)} characters; {platform} allows {limit}.")

    if platform == "instagram":
        if not media:
            problems.append("Instagram needs at least one image or video.")
        tags = re.findall(r"#\w+", caption)
        if len(tags) > 5:
            problems.append(f"Instagram allows 5 hashtags; this has {len(tags)}.")
        for url in media:
            if "?" in url:
                problems.append(f"Media link has '?' in it; Instagram often refuses those: {url}")
        if fmt == "carousel" and not 2 <= len(media) <= 10:
            problems.append(f"A carousel needs 2 to 10 images; this has {len(media)}.")

    if platform == "youtube":
        title = post.get("title") or ""
        if not title.strip():
            problems.append("YouTube needs a title.")
        elif len(title) > 100:
            problems.append(f"Title is {len(title)} characters; YouTube allows 100.")
        if not media:
            problems.append("YouTube needs a video file.")

    return problems
