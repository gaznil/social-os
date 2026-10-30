# Social OS — head rules

**Start card**
1. What: one system that researches, plans, writes, makes, posts and measures content for many social accounts (Instagram, YouTube, LinkedIn, X, Facebook, Threads).
2. Where we are: read STATUS below, then `docs/plans/` for the current plan.
3. Private data (accounts, voices, drafts, numbers) lives in `private/` = repo `gaznil/social-os-private`. Never copy it into this public repo.
4. Every post waits for the user's approval before it goes out. No exceptions.
5. Zero spend: only free tiers (Composio free plan, Claude subscription). Anything that costs money is flagged, never used.

---

## 1. WHAT THIS IS
A content system run by Claude for the user's own accounts, several per platform. Flow:
research -> strategy -> create -> approve -> publish -> analyse -> back to strategy. Full flow: `SYSTEM.md`.
The user's screen is a Claude artifact dashboard (`dashboard/`). Claude Code is the engine.

## 2. STATUS
- **30 Oct 2026:** project created. Skill research done and recorded in `SKILLS.md` (each pick compared by opening the repos).
  Four skill packs vendored into `.claude/skills/`. Repos: `gaznil/social-os` (public, so GitHub Actions minutes are free)
  and `gaznil/social-os-private` (private, cloned into `private/`).
- **30 Oct 2026:** Phase 1 plan written: `docs/plans/2026-10-30-phase-1-foundation.md` (7 tasks). Execution = inline,
  Claude decides. **Task 1 DONE** (queue + preflight rules, 27 tests pass: `python -m unittest discover -s tests`).
  **Next: Task 2** (dashboard v1). Task 3 needs the user's account list (platforms + one niche each).
- **30 Oct 2026 (round 2):** user asked for more. ChatGPT-chat repos opened and mined (SKILLS.md "Round 2"); added
  Ideas tab + model/effort picker to Phase 1; new Phase 2 = video studio (Edit King / Motion King / Prompt Guy from the
  dashboard), Phase 3 = research (Apify no-login competitor radar, reel deep dive, Agent Reach no-login channels,
  last30days). yt-dlp not installed; ffmpeg is.
- **30 Oct 2026 (round 3, user decisions):** (1) video editing = **Prompt Guy first**, then "Run it" with Edit King /
  Motion King; (2) **zero accounts now**: the user will create ONE account later, so Task 3 waits and the dashboard must
  work empty; (3) every format (carousel, story, reel, image, text, thread) previews in the dashboard's Approve tab;
  `story` format added to the plan (Task 2 Step 0); (4) model picker uses Claude's names: Haiku 5.5 / Sonnet 5.5 /
  Opus 5.5 + Low / Medium / High. **Agent Reach: INSTALLED by the user 30 Oct**, tested OK (YouTube + Reddit search,
  no login). Role = free read-only research (see engine/research README).
  **HANDOFF 30 Oct:** user switched chats. **Next = Task 2** (Step 0 story rule, then dashboard v1). Nothing else pending.

## 3. WHERE THINGS LIVE
- This folder: `C:\Projects\social-os` = github.com/gaznil/social-os (PUBLIC).
- `private\` = github.com/gaznil/social-os-private (PRIVATE), its own git repo, ignored by this one.
- Platform rules + which skills to use: `platforms/<platform>/README.md`.
- Pipeline stages: `engine/<stage>/README.md` (research, strategy, create, publish, analytics).
- Dashboard: `dashboard/` (artifact page source; its live data sits in the artifact database, not in git).
- Skill choices and rejected options with reasons: `SKILLS.md`. Licences of vendored skills: `THIRD_PARTY.md`.

## 4. RULES
- **Approval gate:** nothing is published until the user approves that exact post (dashboard "Approve" or a yes in chat).
- **Public repo hygiene:** no account names, handles, voices, drafts, numbers, IDs or secrets in this repo. They go in `private/`.
  Secrets go nowhere in git: platform logins live in Composio, keys in git-ignored `.env` files only.
- **Voice files:** the vendored skills look for `~/.claude/<platform>/voice.md`. Use the active account's
  `private/accounts/<account-id>/voice.md` instead, every time.
- **One niche per account.** Never post the same content to two accounts on the same platform (spam rules = bans).
- **Never automate** likes, follows, mass comments or cold DMs. Instagram replies/DMs after a comment = Porotta, not this system.
- **Posting only through official APIs** (via Composio). No browser automation, no password sharing, no scraping behind logins.
- **Skills first:** before writing or building, load the skill named in the platform/stage README. If a better one appears, compare
  by opening both (not by stars) and record the result in `SKILLS.md`.
- **Save as you go:** after every real step update STATUS above, commit and push both repos.

## 5. GOTCHAS
- X (Twitter) API has no free tier for new developers (pay per use, checked 30 Oct 2026). X posts go out by "copy + open X"
  unless a free route is proven.
- YouTube: Google lifted the "API uploads stay private" rule for unaudited projects (issue tracker, 13 Oct 2026). Re-check if uploads lock.
- Instagram API: max 100 API posts per account per 24 h; account must be Creator or Business; media must be a clean public URL
  or a Composio-staged file.
- LinkedIn: one personal profile per human; extra accounts must be company pages.
- Claude cloud scheduled tasks: at most once an hour; each run uses normal subscription usage.
- Agent Reach command is `C:\Users\gazni\.local\bin\agent-reach.exe` (that folder is not on PATH). Use only its no-login
  channels (youtube, reddit, github, web); never `agent-reach login` for Instagram/X/Facebook/LinkedIn.

## 6. QUEUE
The current plan in `docs/plans/` is the queue. Do not duplicate it here.
