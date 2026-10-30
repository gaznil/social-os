# Social OS — Phase 1: Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** One working loop for real accounts: a dashboard where the user approves drafts, and a publisher that posts approved items to LinkedIn and Instagram through Composio, with every rule checked before posting.

**Architecture:** Claude Code is the engine; project skills in `.claude/skills/sos-*` hold each job's steps. A private Claude artifact page (`dashboard/index.html`) is the user's screen; its artifact database is the live state (accounts, posts, messages). Small stdlib-only Python modules in `tools/sos/` hold the rules that must never be wrong (queue status changes, platform limits), with unit tests. Posting goes only through the Composio connector.

**Tech Stack:** Python 3.14 stdlib (`unittest`, no dependencies), a single-file HTML/JS artifact (no build step), Claude artifact `db` + `sample` + `user` capabilities, Composio connector (free plan), Claude Code cloud scheduled tasks.

## Global Constraints

- Zero spend: free tiers only. Anything that would cost money stops and is reported, never used.
- Nothing is published without the user's approval of that exact post (`status: "approved"` set from the dashboard, or a yes in chat that Claude records as `approvedBy: "chat"`).
- Public repo `gaznil/social-os` holds no account handles, voices, drafts, metrics, IDs or secrets. Those go in `private/` (`gaznil/social-os-private`). Secrets go in no git repo.
- Time zone for all planning: `Asia/Kolkata`. Times are stored as ISO 8601 with offset, e.g. `2026-11-02T19:00:00+05:30`.
- Platforms: `instagram`, `youtube`, `linkedin`, `x`, `facebook`, `threads`. Auto-post in Phase 1: `linkedin`, `instagram`. Manual ("copy + open app"): `x`, `threads`. `youtube`, `facebook`: Phase 2.
- Instagram: max 5 hashtags, caption max 2,200 characters, media URL must not contain `?`.
- Every draft passes the platform humanizer skill (`ig-human`, `linkedin-humanizer`, `x-human`) before it reaches the user.
- Python tests run with: `python -m unittest discover -s tests -v` from `C:\Projects\social-os`.

## Roadmap (later phases get their own plan files)

| Phase | Delivers |
|---|---|
| **1 (this file)** | Rules + tests, dashboard v1 (incl. Ideas tab and the model/effort picker in Talk), accounts, draft → approve → post for LinkedIn + Instagram, cloud publisher, message inbox |
| 2 | Video studio: Studio tab, `jobs` collection, in-page upload (assets, 20 MB) + Google Drive "Social OS inbox" folder, `sos-studio` skill running Edit King / Motion King / Prompt Guy / faceless-explainer with the job's model + effort, install yt-dlp; results become drafts |
| 3 | Research: per-account foundation (`pillars.md`, `formats.md` via interview), Apify competitor radar (daily), deep dive (ffmpeg contact sheet + faster-whisper + formula card, weekly), install Agent Reach (no-login channels) + `last30days`, Research tab, weekly plan auto-filled |
| 4 | More platforms: YouTube + Facebook posting, Composio X test, Threads route, Porotta link (auto DM automation for "comment KEYWORD" posts), "Post now" from the page if Composio works there |
| 5 | Analytics: weekly numbers pull, review ending in ONE change into `lessons.md`, dashboard charts (`dataviz`), monthly `llm-council` strategy check, best posts → gaznil.com via `blog-repurpose` |

## File map

| File | Responsibility |
|---|---|
| `tools/__init__.py`, `tools/sos/__init__.py` | Package markers (empty) |
| `tools/sos/queue.py` | Post statuses, allowed status changes, which posts are due |
| `tools/sos/preflight.py` | Platform rule checks on one post; returns a list of plain-English problems |
| `tools/sos/cli.py` | `python -m tools.sos.cli due|check <posts.json>`: used by the skills on exported posts |
| `tests/test_queue.py`, `tests/test_preflight.py`, `tests/test_cli.py` | Unit tests |
| `docs/DATA.md` | The database shape every part uses (collections + fields) |
| `dashboard/index.html` | The artifact page |
| `.claude/skills/sos-account/SKILL.md` | Add an account (private folder + db doc + Composio connection) |
| `.claude/skills/sos-create/SKILL.md` | Make one draft from an idea/slot, humanized and preflighted |
| `.claude/skills/sos-publish/SKILL.md` | Post due approved items; write results back |
| `.claude/skills/sos-inbox/SKILL.md` | Read and answer dashboard messages |
| `platforms/linkedin/PUBLISH.md`, `platforms/instagram/PUBLISH.md` | Exact Composio call sequence per platform |

## Data shape (copied into `docs/DATA.md` in Task 2)

- `accounts/{accountId}`: `platform`, `label` (shown in the dashboard, no handle needed), `niche`, `language`, `postsPerWeek` (number), `composioAccountId` (string or null), `status` (`active`|`paused`), `updatedAt` (ISO).
- `posts/{postId}`: `accountId`, `platform`, `format` (`text`|`image`|`carousel`|`reel`|`video`|`short`|`thread`), `title` (YouTube only, else `""`), `caption`, `mediaUrls` (array of strings), `plannedAt` (ISO), `status` (see queue), `approvedBy` (`dashboard`|`chat`|null), `approvedAt` (ISO|null), `postedAt` (ISO|null), `platformPostId` (string|null), `permalink` (string|null), `error` (string|null), `problems` (array of strings from preflight), `updatedAt` (ISO).
- `messages/{messageId}`: `from` (`user`|`claude`), `text`, `status` (`new`|`done`), `reply` (string|null), `createdAt` (ISO).
- `ideas/{ideaId}`: `text`, `accountId` (string|null = any account), `source` (`user`|`research`|`plan`), `status` (`new`|`drafted`|`dropped`), `createdAt` (ISO).
- `jobs/{jobId}` (Phase 2; listed now so names stay stable): `tool` (`edit-king`|`motion-king`|`prompt-guy`|`faceless-explainer`|`sos-create`), `accountId`, `brief`, `inputs` (array of asset URLs or Drive links), `model` (`haiku`|`sonnet`|`opus`), `effort` (`low`|`medium`|`high`), `status` (`new`|`working`|`done`|`failed`), `output` (array of links), `note` (string|null), `createdAt`.
- `runs/{runId}`: `kind` (`publish`|`inbox`|`research`|`analytics`), `startedAt`, `finishedAt`, `summary` (one plain sentence).
- `settings/main`: `timezone` (`Asia/Kolkata`), `postingWindows` (array, default `["09:00","13:00","19:00"]`).

---

### Task 1: Queue and preflight rules (tested)

**Files:**
- Create: `tools/__init__.py`, `tools/sos/__init__.py` (both empty)
- Create: `tools/sos/queue.py`, `tools/sos/preflight.py`, `tools/sos/cli.py`
- Test: `tests/test_queue.py`, `tests/test_preflight.py`, `tests/test_cli.py`

**Interfaces:**
- Produces: `queue.STATUSES: tuple[str, ...]`, `queue.can_move(old: str, new: str) -> bool`, `queue.parse_time(s: str) -> datetime` (raises `ValueError` if no offset), `queue.due_posts(posts: list[dict], now: datetime) -> list[dict]`, `queue.MANUAL_PLATFORMS: frozenset[str]`, `preflight.check(post: dict) -> list[str]`, CLI `python -m tools.sos.cli due <file> [--now ISO]` and `python -m tools.sos.cli check <file>` printing JSON.

- [ ] **Step 1: Write the failing queue tests**

`tests/test_queue.py`:
```python
import unittest
from datetime import datetime, timezone, timedelta

from tools.sos import queue

IST = timezone(timedelta(hours=5, minutes=30))
NOW = datetime(2026, 11, 2, 19, 0, tzinfo=IST)


def post(**kw):
    base = {"id": "p1", "platform": "linkedin", "status": "approved",
            "plannedAt": "2026-11-02T18:00:00+05:30"}
    base.update(kw)
    return base


class CanMove(unittest.TestCase):
    def test_normal_path(self):
        for old, new in [("draft", "waiting"), ("waiting", "approved"),
                         ("approved", "posting"), ("posting", "posted")]:
            self.assertTrue(queue.can_move(old, new), (old, new))

    def test_cannot_skip_approval(self):
        self.assertFalse(queue.can_move("draft", "approved"))
        self.assertFalse(queue.can_move("waiting", "posting"))

    def test_posted_is_final(self):
        for s in queue.STATUSES:
            self.assertFalse(queue.can_move("posted", s))

    def test_failed_can_be_reapproved(self):
        self.assertTrue(queue.can_move("failed", "approved"))

    def test_unknown_status(self):
        self.assertFalse(queue.can_move("banana", "approved"))


class ParseTime(unittest.TestCase):
    def test_offset_required(self):
        with self.assertRaises(ValueError):
            queue.parse_time("2026-11-02T18:00:00")

    def test_z_suffix(self):
        self.assertEqual(queue.parse_time("2026-11-02T12:30:00Z"),
                         datetime(2026, 11, 2, 18, 0, tzinfo=IST))


class DuePosts(unittest.TestCase):
    def test_only_approved_and_past(self):
        posts = [post(id="a"),
                 post(id="b", status="waiting"),
                 post(id="c", plannedAt="2026-11-02T20:00:00+05:30"),
                 post(id="d", status="posted")]
        self.assertEqual([p["id"] for p in queue.due_posts(posts, NOW)], ["a"])

    def test_oldest_first(self):
        posts = [post(id="late", plannedAt="2026-11-02T18:30:00+05:30"),
                 post(id="early", plannedAt="2026-11-02T09:00:00+05:30")]
        self.assertEqual([p["id"] for p in queue.due_posts(posts, NOW)],
                         ["early", "late"])

    def test_manual_platforms_never_due(self):
        posts = [post(id="x1", platform="x"), post(id="t1", platform="threads")]
        self.assertEqual(queue.due_posts(posts, NOW), [])

    def test_missing_time_skipped(self):
        self.assertEqual(queue.due_posts([post(plannedAt=None)], NOW), [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify it fails**

Run: `python -m unittest tests.test_queue -v`
Expected: FAIL / ERROR with `ImportError` or `ModuleNotFoundError: No module named 'tools'`.

- [ ] **Step 3: Implement `tools/sos/queue.py`** (and create the two empty `__init__.py` files)

```python
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
```

- [ ] **Step 4: Run to verify it passes**

Run: `python -m unittest tests.test_queue -v`
Expected: all tests `ok`.

- [ ] **Step 5: Write the failing preflight tests**

`tests/test_preflight.py`:
```python
import unittest

from tools.sos import preflight


def post(**kw):
    base = {"platform": "linkedin", "format": "text", "title": "",
            "caption": "A real post.", "mediaUrls": [], "status": "waiting",
            "approvedAt": None}
    base.update(kw)
    return base


class Common(unittest.TestCase):
    def test_clean_post_has_no_problems(self):
        self.assertEqual(preflight.check(post()), [])

    def test_unknown_platform(self):
        self.assertIn("Unknown platform: myspace", preflight.check(post(platform="myspace")))

    def test_empty_caption(self):
        self.assertIn("Caption is empty.", preflight.check(post(caption="  ")))

    def test_approved_needs_time(self):
        self.assertIn("Approved but no approval time recorded.",
                      preflight.check(post(status="approved")))


class Instagram(unittest.TestCase):
    def ig(self, **kw):
        fields = {"platform": "instagram", "format": "image",
                  "mediaUrls": ["https://cdn.example.com/a.jpg"]}
        fields.update(kw)
        return post(**fields)

    def test_needs_media(self):
        p = self.ig()
        p["mediaUrls"] = []
        self.assertIn("Instagram needs at least one image or video.", preflight.check(p))

    def test_hashtag_cap(self):
        cap = "Post " + " ".join(f"#t{i}" for i in range(6))
        self.assertIn("Instagram allows 5 hashtags; this has 6.", preflight.check(self.ig(caption=cap)))

    def test_query_in_url(self):
        p = self.ig()
        p["mediaUrls"] = ["https://cdn.example.com/a.jpg?sig=1"]
        self.assertIn("Media link has '?' in it; Instagram often refuses those: https://cdn.example.com/a.jpg?sig=1",
                      preflight.check(p))

    def test_caption_length(self):
        self.assertIn("Caption is 2201 characters; instagram allows 2200.",
                      preflight.check(self.ig(caption="a" * 2201)))

    def test_carousel_size(self):
        p = self.ig(format="carousel")
        p["mediaUrls"] = ["https://cdn.example.com/a.jpg"]
        self.assertIn("A carousel needs 2 to 10 images; this has 1.", preflight.check(p))


class X(unittest.TestCase):
    def test_weighted_length_counts_links_as_23(self):
        cap = "a" * 250 + " https://example.com/a/very/long/path/that/is/long"
        self.assertEqual(preflight.check(post(platform="x", caption=cap)), [])

    def test_too_long(self):
        self.assertIn("Post is 281 weighted characters; x allows 280.",
                      preflight.check(post(platform="x", caption="a" * 281)))

    def test_wide_characters_count_double(self):
        self.assertIn("Post is 282 weighted characters; x allows 280.",
                      preflight.check(post(platform="x", caption="😀" * 141)))


class YouTube(unittest.TestCase):
    def test_needs_title_and_video(self):
        problems = preflight.check(post(platform="youtube", format="video"))
        self.assertIn("YouTube needs a title.", problems)
        self.assertIn("YouTube needs a video file.", problems)

    def test_title_length(self):
        p = post(platform="youtube", format="video", title="t" * 101,
                 mediaUrls=["C:/videos/a.mp4"])
        self.assertIn("Title is 101 characters; YouTube allows 100.", preflight.check(p))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 6: Run to verify it fails**

Run: `python -m unittest tests.test_preflight -v`
Expected: ERROR `cannot import name 'preflight'`.

- [ ] **Step 7: Implement `tools/sos/preflight.py`**

```python
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
```

- [ ] **Step 8: Run to verify it passes**

Run: `python -m unittest tests.test_preflight -v`
Expected: all `ok`. (Check: `"😀" * 141` = 282 weighted, `"a"*250 + link` = 250 + 1 space + 23 = 274.)

- [ ] **Step 9: Write the failing CLI test**

`tests/test_cli.py`:
```python
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    out = subprocess.run([sys.executable, "-m", "tools.sos.cli", *args],
                         cwd=ROOT, capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


class Cli(unittest.TestCase):
    def setUp(self):
        posts = [
            {"id": "a", "platform": "linkedin", "format": "text", "caption": "Hi",
             "status": "approved", "approvedAt": "2026-11-01T10:00:00+05:30",
             "plannedAt": "2026-11-02T09:00:00+05:30", "mediaUrls": []},
            {"id": "b", "platform": "instagram", "format": "image", "caption": "Hi",
             "status": "approved", "approvedAt": "2026-11-01T10:00:00+05:30",
             "plannedAt": "2026-11-03T09:00:00+05:30", "mediaUrls": []},
        ]
        self.tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(posts, self.tmp)
        self.tmp.close()

    def tearDown(self):
        Path(self.tmp.name).unlink()

    def test_due(self):
        res = run("due", self.tmp.name, "--now", "2026-11-02T10:00:00+05:30")
        self.assertEqual([p["id"] for p in res], ["a"])

    def test_check(self):
        res = run("check", self.tmp.name)
        self.assertEqual(res["a"], [])
        self.assertIn("Instagram needs at least one image or video.", res["b"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 10: Run to verify it fails**

Run: `python -m unittest tests.test_cli -v`
Expected: ERROR, `subprocess.CalledProcessError` (no module `tools.sos.cli`).

- [ ] **Step 11: Implement `tools/sos/cli.py`**

```python
"""Command line for skills: `due` and `check` on a JSON list of posts (each with an "id")."""
import argparse
import json
import sys
from datetime import datetime, timezone

from tools.sos import preflight, queue


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tools.sos.cli")
    ap.add_argument("command", choices=["due", "check"])
    ap.add_argument("file")
    ap.add_argument("--now", help="ISO time with offset; default = now")
    args = ap.parse_args(argv)

    with open(args.file, encoding="utf-8") as f:
        posts = json.load(f)

    if args.command == "due":
        now = queue.parse_time(args.now) if args.now else datetime.now(timezone.utc)
        result = queue.due_posts(posts, now)
    else:
        result = {p["id"]: preflight.check(p) for p in posts}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 12: Run the whole suite**

Run: `python -m unittest discover -s tests -v`
Expected: every test `ok`, 0 failures.

- [ ] **Step 13: Commit**

```bash
git add tools tests
git commit -m "Queue and preflight rules with tests"
git push
```

---

### Task 2: Dashboard v1 (artifact page + database)

**Files:**
- Create: `docs/DATA.md` (the "Data shape" section above, verbatim)
- Create: `dashboard/index.html`
- Modify: `private/README.md` (record the dashboard URL)

**Interfaces:**
- Consumes: data shape above; status names from `queue.STATUSES`; the same `can_move` table (mirrored in JS, see below).
- Produces: a published artifact with `capabilities: {db: {}, user: {}, sample: {}}` (the page stays private to the user, so the default rules are enough); collections `accounts`, `posts`, `messages`, `runs`, `settings`.

- [ ] **Step 1: Load the design skills** — `artifact-design` (required before any artifact) and `dataviz` (stat tiles). Follow their page contract: `<title>Social OS</title>`, colour tokens on `:root` with the dark-mode block, explicit `body` background, phone width with 16px gutter, no horizontal scroll.

- [ ] **Step 2: Write `docs/DATA.md`** with the data shape section copied from this plan, plus one line: "The dashboard and every `sos-*` skill read and write exactly these fields."

- [ ] **Step 3: Write `dashboard/index.html`** with six tabs:
  - **Today:** counts (waiting approval, approved & scheduled, posted this week, failed) and the next 5 scheduled posts.
  - **Approve:** every `waiting` post as a card: account label, platform, planned time, caption, media thumbnails, `problems` list in red if not empty. Buttons: Approve, Back to draft, Reject. Approve is disabled while `problems` is not empty.
  - **Calendar:** next 14 days, posts grouped by day, coloured by status. X/Threads posts show a "Copy text" button and an "Open app" link (`https://x.com/compose/post`, `https://www.threads.net/`).
  - **Accounts:** list of `accounts` (label, platform, niche, posts per week, connected yes/no, status). Read-only in Phase 1.
  - **Ideas:** a text box ("Tip: tap the mic on your phone keyboard to speak"), an account picker (accounts + "Any account"), Save → writes an `ideas` doc `{text, accountId, source:"user", status:"new", createdAt}`. Below: the list of ideas with status.
  - **Talk:** a message box + list of `messages` (newest first). Send writes `{from:"user", text, status:"new", reply:null, createdAt}`. A second button "Quick answer" calls `sample` for an instant reply shown under the box (not saved), with the page's own system text: "You help a social media creator. Answer briefly and concretely." Two pickers beside it, remembered in browser storage (wrapped in try/catch): **Model** = Fast (`modelTier:"quick"`) / Balanced (`"default"`) / Best (`"complex"`); **Effort** = low / medium / high. Show the model that answered from `modelTierApplied`. Below the box: "Tip: tap the mic on your phone keyboard to speak."

  The data module inside the page (vanilla JS; status rules mirror `tools/sos/queue.py`):
  ```html
  <script type="module">
  const ALLOWED = {
    draft: ["waiting", "rejected"], waiting: ["approved", "rejected", "draft"],
    approved: ["posting", "waiting", "rejected"], posting: ["posted", "failed"],
    failed: ["approved", "rejected"], posted: [], rejected: ["draft"],
  };
  const canMove = (from, to) => (ALLOWED[from] || []).includes(to);
  const nowIso = () => new Date().toISOString();
  const state = { accounts: [], posts: [], messages: [], ideas: [] };

  const db = await claude.use("db");
  if (!db) { showOffline(); } else {
    for (const name of ["accounts", "posts", "messages", "ideas"]) {
      db.collection(name).onSnapshot(
        snap => { state[name] = snap.docs.map(d => ({ id: d.id, ...d.data() })); render(); },
        err => showError(name, err));
    }
  }

  async function setStatus(post, to) {
    if (!canMove(post.status, to)) return showToast(`Can't move ${post.status} to ${to}`);
    const patch = { status: to, updatedAt: nowIso() };
    if (to === "approved") Object.assign(patch, { approvedBy: "dashboard", approvedAt: nowIso() });
    await db.doc(`posts/${post.id}`).update(patch);
  }

  async function sendMessage(text) {
    if (!text.trim()) return;
    await db.collection("messages").add({ from: "user", text, status: "new", reply: null, createdAt: nowIso() });
  }

  async function saveIdea(text, accountId) {
    if (!text.trim()) return;
    await db.collection("ideas").add({ text, accountId: accountId || null, source: "user", status: "new", createdAt: nowIso() });
  }

  async function quickAnswer(text, modelTier, effort) {
    const sample = await claude.use("sample");
    if (!sample) return showToast("Quick answers are off for this page.");
    const out = await sample([{ role: "user", content:
      "You help a social media creator. Answer briefly and concretely.\n\n" + text }],
      { cache: false, modelTier, effort });
    return { text: out.text, tier: out.modelTierApplied };
  }
  </script>
  ```
  `render`, `showOffline`, `showError`, `showToast` are plain DOM functions in the same script: render builds each tab from `state`; offline shows "Open this page signed in to claude.ai to see your data."; errors show the collection name and `err.code` in plain words. Empty collections show a friendly empty state ("No drafts waiting. Claude adds them here."), never a blank tab.

- [ ] **Step 4: Publish** with the Artifact tool: `file_path: C:\Projects\social-os\dashboard\index.html`, `icon: "chart"`, `description: "Approve, schedule and track posts for every account."`, `capabilities` exactly as in Interfaces.

- [ ] **Step 5: Seed and verify the database** with `ArtifactData`:
  - `set settings/main` = `{timezone: "Asia/Kolkata", postingWindows: ["09:00","13:00","19:00"]}`.
  - `set posts/test-1` = a `waiting` LinkedIn text post with `caption: "TEST - do not publish"`, `problems: []`, `plannedAt` tomorrow 09:00 IST.
  - `list posts` → shows `test-1`. Then ask the user to open the page on their phone and press Approve on the test card; `get posts/test-1` must show `status: "approved"`, `approvedBy: "dashboard"`, `approvedAt` set. Then `delete posts/test-1`.
  Expected: all reads match; tell the user in one line what was exercised.

- [ ] **Step 6: Record the URL** in `private/README.md` ("Dashboard URL: <url>"), commit and push both repos.

```bash
git add docs/DATA.md dashboard/index.html && git commit -m "Dashboard v1 and data shape" && git push
git -C private add README.md && git -C private commit -m "Dashboard URL" && git -C private push
```

---

### Task 3: Accounts — `sos-account` skill + the first real accounts

**Files:**
- Create: `.claude/skills/sos-account/SKILL.md`
- Create (private): `private/accounts/<account-id>/{profile.md, voice.md, competitors.md}` per account

**Interfaces:**
- Consumes: `private/accounts/_template/*`, Composio `COMPOSIO_MANAGE_CONNECTIONS` (`add` with an `alias` = account id; `list` to confirm ACTIVE).
- Produces: one `accounts/{accountId}` db doc per account, with `composioAccountId` from the Composio `list` result.

- [ ] **Step 1: Write `.claude/skills/sos-account/SKILL.md`**:
  ```markdown
  ---
  name: sos-account
  description: Add or update a Social OS account (private folder, dashboard record, Composio login). Use when the user names a new account or changes one.
  ---
  1. Account id = `<platform>-<short-niche>` in lowercase with dashes (e.g. `ig-ai-tools`). Ask only for what the user must decide: platform, niche, language, posts per week, on camera or not.
  2. Copy `private/accounts/_template/` to `private/accounts/<id>/`. Fill `profile.md`. Copy `voice-<platform>.md` to `voice.md` (Facebook uses the Instagram one, Threads the X one).
  3. Voice: if the user has posts, ask for 3 links or pasted texts and fill `voice.md` from them; else interview with 5 questions from the template.
  4. Composio: `COMPOSIO_SEARCH_TOOLS` for the platform, then `COMPOSIO_MANAGE_CONNECTIONS` action `add`, alias = account id. Give the user the link as a markdown link. After they say done, `list` and confirm ACTIVE. Store the account id from `list` as `composioAccountId`.
  5. ArtifactData `set accounts/<id>` with the data-shape fields (`label` = a name with no handle).
  6. Commit + push `private/`. Never write handles or IDs into the public repo.
  ```

- [ ] **Step 2: Ask the user for the starting accounts** (product decision): which accounts on which platforms, one niche each. Recommended start: their existing LinkedIn (already connected in Composio) + 1 Instagram account.

- [ ] **Step 3: Run `sos-account` for each.** Instagram must be a Creator/Business account first (user step in the Instagram app: Settings → Account type and tools → Switch to professional account).

- [ ] **Step 4: Verify**: ArtifactData `list accounts` shows each with `status: "active"` and a non-null `composioAccountId`; the dashboard Accounts tab shows them as connected.

---

### Task 4: Drafts — `sos-create` skill

**Files:**
- Create: `.claude/skills/sos-create/SKILL.md`

**Interfaces:**
- Consumes: account doc + `private/accounts/<id>/voice.md`; platform skills; `python -m tools.sos.cli check`.
- Produces: `posts/{postId}` docs with `status: "waiting"` and `problems` filled.

- [ ] **Step 1: Write `.claude/skills/sos-create/SKILL.md`**:
  ```markdown
  ---
  name: sos-create
  description: Turn an idea or calendar slot into a ready draft for one Social OS account, humanized and rule-checked, and put it in the dashboard for approval.
  ---
  1. Read `platforms/<platform>/README.md` and load the writing skill it names (Instagram: ig-reel / ig-caption / ig-carousel; LinkedIn: linkedin-post-writer; X: x-post / x-thread; YouTube: yt-script + yt-package). Use the account's `voice.md` wherever the skill asks for `~/.claude/<platform>/voice.md`.
  2. Write the draft. Never invent numbers, clients or results; leave `{{your number}}` and say so.
  3. Run the platform humanizer (ig-human / linkedin-humanizer / x-human) and apply its fixes.
  4. Media: images rendered to PNG (1080x1350 for Instagram) into `C:\Gaznil\social-os-media\<account-id>\`; for Instagram, upload through Composio's file staging when posting. Never put media in git.
  5. Write the post JSON to the scratchpad and run `python -m tools.sos.cli check <file>`; put the result in `problems`. Fix and re-check until empty, or leave the problems for the user to see.
  6. ArtifactData `set posts/<id>` with status `waiting`, `plannedAt` = next free posting window for that account (settings/main), all data-shape fields present.
  7. Tell the user one line: what is waiting and where to approve it.
  ```

- [ ] **Step 2: Make one real draft per connected account** (topic from the account niche). Expected: each appears in the dashboard Approve tab with `problems: []`.

- [ ] **Step 3: Commit** `.claude/skills/sos-create` and push.

---

### Task 5: Publishing — `sos-publish` skill, LinkedIn + Instagram recipes, first real posts

**Files:**
- Create: `.claude/skills/sos-publish/SKILL.md`
- Create: `platforms/linkedin/PUBLISH.md`, `platforms/instagram/PUBLISH.md`

**Interfaces:**
- Consumes: `posts` docs; `python -m tools.sos.cli due|check`; Composio tools named below.
- Produces: post docs moved `approved → posting → posted|failed` with `platformPostId`, `permalink`, `postedAt` or `error`; one `runs/{id}` doc per run.

- [ ] **Step 1: Write `platforms/linkedin/PUBLISH.md`**:
  ```markdown
  1. `LINKEDIN_GET_MY_INFO` → author id (cache it in the account doc as `authorUrn` after the first run).
  2. With an image: `LINKEDIN_INITIALIZE_IMAGE_UPLOAD` (top-level `owner` = author), PUT the bytes to the upload URL (201 with empty body = success).
  3. `LINKEDIN_CREATE_LINKED_IN_POST` with author + commentary (+ image). Save the returned id.
  4. `LINKEDIN_GET_POST_CONTENT` to read it back; a 403 here is NOT a failure if step 3 returned an id.
  ```
- [ ] **Step 2: Write `platforms/instagram/PUBLISH.md`**:
  ```markdown
  1. `INSTAGRAM_GET_USER_INFO` → ig_user_id. `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` → stop if quota is used up (result list is under response.data.data).
  2. Image: `INSTAGRAM_POST_IG_USER_MEDIA` (image_url without `?`, or image_file staged) + caption → container id.
     Carousel: one container per image, then `INSTAGRAM_CREATE_CAROUSEL_CONTAINER`. Reel: media_type REELS + video.
  3. Wait 30 s (video: poll the container until FINISHED), then `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` with creation_id.
  4. On error 9007 wait 60 s and publish again once. On error 9 ("too many actions") stop and mark failed: never fast-retry.
  5. `INSTAGRAM_GET_IG_MEDIA` → permalink.
  ```
- [ ] **Step 3: Write `.claude/skills/sos-publish/SKILL.md`**:
  ```markdown
  ---
  name: sos-publish
  description: Post every approved, due Social OS post through Composio and write results back to the dashboard. Use on "publish", in the scheduled publisher run, or when the user approves something for now.
  ---
  1. ArtifactData `query posts` where status == "approved". Save them as JSON in the scratchpad.
  2. `python -m tools.sos.cli due <file>` → the list to post now. `check` again; any problem → status `failed`, `error` = the problems, skip it.
  3. For each: set status `posting` first (so a second run can't double-post), then follow `platforms/<platform>/PUBLISH.md` with the account's Composio connection.
  4. Success → status `posted`, `platformPostId`, `permalink`, `postedAt`. Failure → status `failed`, `error` = one plain sentence + the platform's error code.
  5. ArtifactData `set runs/<publish-YYYYMMDD-HHMM>` with a one-sentence summary ("Posted 2, 1 failed: Instagram quota").
  6. Never post a doc whose status is not `approved`. Never touch X or Threads (manual).
  ```
- [ ] **Step 4: Dry run.** Put one approved LinkedIn post with `plannedAt` tomorrow → run `sos-publish` → expected: nothing posted, run summary "Nothing due."
- [ ] **Step 5: First real posts (needs the user's yes in chat for these exact posts).** The user approves one LinkedIn draft and one Instagram draft in the dashboard with `plannedAt` = now; run `sos-publish`. Expected: both `posted` with permalinks; the user opens each link on their phone to confirm.
- [ ] **Step 6: Commit** skills + PUBLISH files, push. Update STATUS in `CLAUDE.md`.

---

### Task 6: Cloud publisher (runs with the PC off)

**Files:**
- Modify: `CLAUDE.md` (STATUS + GOTCHAS with what the test proved)
- Possibly modify: `docs/DATA.md`, `dashboard/index.html`, `sos-publish` (only if the fallback is needed)

**Interfaces:**
- Consumes: `sos-publish` skill; cloud scheduled task environment.
- Produces: a scheduled task "Social OS publisher" at the posting windows (09:00, 13:00, 19:00 IST = 03:30, 07:30, 13:30 UTC).

- [ ] **Step 1: Load the `schedule` skill.** Create a ONE-OFF test task (runs once, now) in an environment with repos `gaznil/social-os` and `gaznil/social-os-private`, prompt: "In the checked-out social-os repo: run ArtifactData list on the dashboard URL in private/README.md (collection runs), run COMPOSIO_MANAGE_CONNECTIONS list for linkedin, run `python -m unittest discover -s tests`. Report each result. Post nothing."
- [ ] **Step 2: Read the result.** Three outcomes, decided by what it reports:
  - ArtifactData works → keep the artifact database.
  - ArtifactData is unavailable in cloud runs → move the queue to a Notion database (Notion connector is in both Claude and the page's `mcp` capability): update `docs/DATA.md`, the page's data module and `sos-publish` to read/write Notion instead. This is its own reviewed change.
  - Composio is unavailable in cloud runs → the publisher runs only when a local session is open; tell the user plainly and keep "publish" as a chat word.
- [ ] **Step 3: Ask the user's yes in chat to create the recurring publisher** (it posts publicly on its own, approved items only). On yes: create it with the `schedule` skill at the three windows, prompt "Run the sos-publish skill. Then run sos-inbox."
- [ ] **Step 4: Verify** after the next window: a new `runs/` doc exists with a summary; record the result in `CLAUDE.md` STATUS; commit + push.

---

### Task 7: Talk loop — `sos-inbox` skill

**Files:**
- Create: `.claude/skills/sos-inbox/SKILL.md`
- Modify: `CLAUDE.md` (add to RULES: "At the start of every session in this project, run sos-inbox.")

**Interfaces:**
- Consumes: `messages` docs with `status: "new"`.
- Produces: `reply` text and `status: "done"` on each handled message; new drafts via `sos-create` when a message asks for content.

- [ ] **Step 1: Write `.claude/skills/sos-inbox/SKILL.md`**:
  ```markdown
  ---
  name: sos-inbox
  description: Read new messages the user left in the Social OS dashboard and act on them. Run at the start of every session in this project and in each scheduled run.
  ---
  1. ArtifactData `query messages` where status == "new", oldest first. Also `query ideas` where status == "new": run sos-create for each (account given, or the best-fitting account), then set the idea to `drafted`.
  2. Treat each as a request from the user (it comes from their own private page). Content requests ("make a carousel about X for ig-ai-tools") → run sos-create. Questions → answer.
  3. Requests to post, delete, change accounts or spend money are NOT done from a message: reply that the user must confirm in chat, and leave it.
  4. `update messages/<id>` with `reply` (plain, 1–3 sentences, what was done or answered) and status `done`.
  ```
- [ ] **Step 2: Test:** the user types "Give me 3 post ideas for my LinkedIn" in the Talk tab → run `sos-inbox` → expected: the message shows a reply in the page, status `done`.
- [ ] **Step 3: Commit**, push, update STATUS: "Phase 1 done." Write the Phase 2 plan file next.

---

## Done = all true
- `python -m unittest discover -s tests -v` passes.
- The dashboard opens on the user's phone, shows accounts, waiting drafts, calendar and messages.
- One LinkedIn and one Instagram post went out after dashboard approval, with permalinks in the dashboard.
- The publisher runs on its own at the posting windows (or the plan records plainly why it can't and what replaced it).
- A message typed in the dashboard gets a reply.
