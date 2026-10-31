# Phase 3: Video Studio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** From the dashboard, the user asks for a video (brief and/or clip link) and gets back a paste-ready Prompt Guy prompt with a Copy button; optionally "one video -> pack" also drafts a different post for every connected platform.

**Architecture:** The dashboard writes a `jobs` doc (status `requested`). Claude's next run (sos-inbox -> new `sos-studio` skill) reads it, uses `deepdive` for a clip's transcript, writes the prompt with the `prompt-guy` skill, and for packs runs `sos-create` once per target that `tools/sos/studio.py pack-plan` returns. The page shows the prompt and links to the pack drafts in Approve.

**Tech Stack:** Python 3 stdlib + unittest (existing `tools/sos`), artifact page `dashboard/index.html` (db capability), ArtifactData.

## Global Constraints
- Video = Prompt Guy ONLY (user rule 31 Oct): never run Edit King, Motion King, faceless-explainer or HyperFrames; no "Run it" button.
- Every pack post is a draft with status `waiting`; nothing publishes without the user's Approve.
- Never the same content on two accounts of the same platform; each platform gets its own rewrite.
- Realism rule (LESSONS 31 Oct): only what we can show working.
- No private data (handles, drafts) in this public repo.
- Zero spend.

---

### Task 1: `studio.py` - job check + pack plan

**Files:**
- Create: `tools/sos/studio.py`
- Modify: `tools/sos/cli.py` (add `studio-check` and `pack-plan` commands)
- Test: `tests/test_studio.py`

**Interfaces:**
- Produces: `check_job(job: dict) -> list[str]` (problems, empty = ok); `pack_plan(job: dict, accounts: list[dict]) -> list[dict]` each `{"accountId", "platform", "format"}`.
- CLI: `python -m tools.sos.cli studio-check <job.json>`, `python -m tools.sos.cli pack-plan <job.json> <accounts.json>` -> JSON on stdout.

Rules: job needs `accountId`, `kind` in (`prompt`, `pack`), and a non-empty `brief` or `clipUrl`. Pack plan: one target per *active* account (skip the job's own account's reel, it is the video itself); format per platform: instagram -> carousel, linkedin -> text, x -> thread, threads -> text, facebook -> text, youtube -> short-description (`text`). One target per account; accounts with status other than `active` skipped.

- [x] Step 1: write `tests/test_studio.py`:

```python
import unittest
from tools.sos.studio import check_job, pack_plan

ACC = [
    {"id": "ig-a", "platform": "instagram", "status": "active"},
    {"id": "li-a", "platform": "linkedin", "status": "active"},
    {"id": "x-a", "platform": "x", "status": "setup"},
]

class StudioTest(unittest.TestCase):
    def test_ok_job(self):
        self.assertEqual(check_job({"accountId": "ig-a", "kind": "prompt", "brief": "a reel"}), [])
    def test_needs_brief_or_clip(self):
        self.assertTrue(check_job({"accountId": "ig-a", "kind": "prompt"}))
    def test_bad_kind(self):
        self.assertTrue(check_job({"accountId": "ig-a", "kind": "run", "brief": "x"}))
    def test_needs_account(self):
        self.assertTrue(check_job({"kind": "pack", "brief": "x"}))
    def test_pack_plan(self):
        plan = pack_plan({"accountId": "ig-a", "kind": "pack", "brief": "x"}, ACC)
        self.assertEqual(plan, [
            {"accountId": "ig-a", "platform": "instagram", "format": "carousel"},
            {"accountId": "li-a", "platform": "linkedin", "format": "text"},
        ])
    def test_prompt_job_has_no_pack(self):
        self.assertEqual(pack_plan({"accountId": "ig-a", "kind": "prompt", "brief": "x"}, ACC), [])

if __name__ == "__main__":
    unittest.main()
```

- [x] Step 2: run `python -m unittest tests.test_studio` -> FAIL (no module).
- [x] Step 3: write `tools/sos/studio.py`:

```python
"""Video studio jobs: check a job and plan the 'one video -> pack' drafts."""

KINDS = ("prompt", "pack")
PACK_FORMAT = {"instagram": "carousel", "linkedin": "text", "x": "thread", "threads": "text",
               "facebook": "text", "youtube": "text"}


def check_job(job):
    problems = []
    if not job.get("accountId"):
        problems.append("Pick an account.")
    if job.get("kind") not in KINDS:
        problems.append("Kind must be prompt or pack.")
    if not (job.get("brief") or "").strip() and not (job.get("clipUrl") or "").strip():
        problems.append("Add a brief or a clip link.")
    return problems


def pack_plan(job, accounts):
    if job.get("kind") != "pack":
        return []
    return [{"accountId": a["id"], "platform": a["platform"], "format": PACK_FORMAT[a["platform"]]}
            for a in accounts if a.get("status") == "active" and a.get("platform") in PACK_FORMAT]
```

- [x] Step 4: add to `tools/sos/cli.py` the two commands (read JSON files, print `json.dumps`), matching its existing `check` command style.
- [x] Step 5: `python -m unittest discover -s tests` -> all pass. Commit.

### Task 2: `sos-studio` skill + wiring

**Files:** Create `.claude/skills/sos-studio/SKILL.md`; modify `.claude/skills/sos-inbox/SKILL.md` step 1, `docs/DATA.md`, `SYSTEM.md`.

`jobs/{autoId}` (DATA.md): `accountId`, `kind` (`prompt`|`pack`), `brief` (string), `clipUrl` (string|null: a public link, or a file name in `C:\Gaznil\social-os-media\inbox\`), `status` (`requested` | `working` | `done` | `failed`), `prompt` (string|null, set by Claude), `postIds` (array, pack drafts), `note` (string|null), `createdAt`, `updatedAt`.

Skill steps: skills rule + learning rule (same wording as other sos skills); 1) query `jobs` status `requested`, `update` -> `working`; 2) `studio-check` - problems -> `failed` + note; 3) clip -> `python -m tools.sos.deepdive` for transcript + frames; 4) load `prompt-guy`, write the paste-ready prompt from brief + transcript + the account's `voice.md`/`style.md`, update `prompt`; 5) kind pack -> `pack-plan`, run `sos-create` per target (own rewrite each, realism rule), collect `postIds`; 6) `update` status `done` + one-line note. Never runs any video tool.
Inbox: after ideas, "Then run sos-studio."

- [x] Write files, grep check `grep -c "Learning rule" .claude/skills/sos-*/SKILL.md` shows sos-studio, commit.

### Task 3: Dashboard Studio tab

**Files:** Modify `dashboard/index.html`: add `jobs` to state + snapshot list (pending +1), tab `["studio", "Studio"]`, `viewStudio()`: form (account select via `accountOptions`, brief textarea, clip link input, two buttons "Get prompt" / "Prompt + all-platform pack") -> `db.collection("jobs").add({... status: "requested"})`; list of jobs newest first: status pill, brief, prompt in a `<pre>` with **Copy prompt** button (clipboard, same fallback toast as `data-copy`), pack -> "N drafts in Approve". Keep input values on re-render (same pattern as Ideas tab).

- [x] Edit, publish to the dashboard URL, check in Playwright at 390 px wide that the tab renders empty and with one job. Commit.

### Task 4: End-to-end dry run

- [x] ArtifactData `set jobs/test-studio` (kind `prompt`, ig account, brief "30 s reel: one Claude Code command that saves an hour"). Run sos-studio: it must NOT run Prompt Guy for a test job (user 31 Oct: "who said to give prompt now?"), only the one-line placeholder. Check `prompt` filled + status `done`, visible in Studio tab. Delete the test job. Update CLAUDE.md STATUS, commit + push both repos.
