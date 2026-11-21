# Dashboard (v25)

A private Claude artifact page: the user's one screen, phone or PC. No domain, no server.

**Tabs (6):** Control room · Plan · Approve · Calendar · Studio · Accounts.
Header has a global **Account Switch** (scopes every tab, form, and voice tool) and a **Live / Showcase** toggle.

**How it works**
- Its own artifact database holds the live state: `accounts`, `posts`, `messages`, `ideas`, `inspirations`, `options`, `scripts`, `hooks`, `jobs`, `schedules`, `competitors`, `stats`, `runs`. Claude Code reads and writes it; the page shows it live.
- **Control room:** 3D iridescent orb, Talk to Claude (instant on-page Claude with Haiku 5.5 / Sonnet 5.5 / Opus 5.5 + Low / Medium / High effort, plus Voice Mode via OS/keyboard dictation), 9 live channel cards, real `runs` Engine Log, and the **Growth** section (followers line, 4 IST tiles, synced to the account switch).
- **Plan (3 sub-views: Workspace · Reel Radar · Hook Vault):**
  - **Workspace:** 3 doors (Week/Month plan, One video about…, or open Studio), Options (Pick / Drop, with slot-swap context), and Scripts (EN | Malayalam-English toggle, Approve script / Ask changes, plus an **Approved & Ready to Film** section with a **fullscreen Teleprompter**).
  - **Reel Radar (v25):** paste 1 or many viral Instagram/YouTube/X URLs at once (or share them in VS Code chat). `sos-radar` deduplicates, deconstructs, and ranks them 0–100 (`P1 Film Now` -> `P2 Queue` -> `P3 Save` -> `Skip`) with outlier multiple, hook score, "why it popped", and "our twist", then writes improved EN + ML-EN scripts for Gate 1 approval.
  - **Hook Vault:** searchable hook templates by type; `"Use this"` sends the hook into the Plan/Options flow (never skips Gate 1).
- **Approve:** Failed-post recovery banner (`post.error` + Retry / Reject) and waiting drafts with previews for every format (carousel 4:5, story 9:16, reel/video, YouTube thumbnail, image, text, thread cards), **inline caption/title editing** (tracks `editedFrom` for `sos-learn`), "Back to draft" with feedback note, and two-step confirmation on `Approve + post now`.
- **Calendar:** Toggle between **Month grid**, **14-day list**, and **Instagram 3:4 Grid Preview**. Tap any slot to view caption, media, `permalink`, per-post `metrics`, reschedule `plannedAt`, swap/replace, or Copy + Open X + Mark as posted.
- **Studio (Prompt Guy only):** brief + optional clip link or filename in `C:\Gaznil\social-os-media\inbox\`, plus optional Model / Effort pickers. Prompt Guy writes the paste-ready prompt with a Copy button; "Prompt + all-platform pack" also drafts one post per active account. Never runs Edit King / Motion King.
- **Accounts:** manage accounts (shows learned `bestTimes`), **Competitors & profiles I like**, **Schedules** (synced to Claude cloud tasks), and recent **Engine Runs**.
- **Voice:** the phone keyboard's mic or `Win + H` in any text box (artifact pages cannot use the microphone on this account).

**Source:** `dashboard/index.html`. Published with the Artifact tool; its URL is in `private/README.md`.
