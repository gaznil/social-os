"""Post queue rules: statuses, allowed changes, and which posts are due."""
from datetime import datetime

STATUSES = ("draft", "waiting", "approved", "posting", "posted", "failed", "rejected")

_ALLOWED = {
    "draft": {"waiting", "rejected"},
    "waiting": {"approved", "rejected", "draft"},
    "approved": {"posting", "waiting", "rejected"},
    "posting": {"posted", "failed"},
    "failed": {"approved", "rejected"},
    "posted": set(),
    "rejected": {"draft"},
}

# Platforms with no free posting API yet: the user posts these by hand.
MANUAL_PLATFORMS = frozenset({"x", "threads"})


def can_move(old, new):
    return new in _ALLOWED.get(old, set())


def parse_time(s):
    t = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if t.tzinfo is None:
        raise ValueError(f"time has no offset: {s}")
    return t


def due_posts(posts, now):
    due = [p for p in posts
           if p.get("status") == "approved"
           and p.get("platform") not in MANUAL_PLATFORMS
           and p.get("plannedAt")
           and parse_time(p["plannedAt"]) <= now]
    return sorted(due, key=lambda p: parse_time(p["plannedAt"]))
