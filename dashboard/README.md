# Dashboard (v26)

A private Claude artifact page: the user's one screen, phone or PC. No domain, no server.

**Tabs (6):** Home · Plan · Approve · Calendar · Studio · Accounts.
Header has a global **Account Switch** (scopes every tab, form, and voice tool), a **Live / Showcase** toggle, and a **+ Drop viral URLs** shortcut.

**How it works**
- Its own artifact database holds the live state: `accounts`, `posts`, `messages`, `ideas`, `inspirations`, `options`, `scripts`, `hooks`, `learnings`, `jobs`, `schedules`, `competitors`, `stats`, `runs`. Claude Code reads and writes it; the page shows it live.
- **Welcome Screen & Studio Liquid-Glass Pearl Sphere:** Multilingual greeting (`Hello`, `നമസ്കാരം`, `Bonjour`, `こんにちは`, etc.) with an Iris Aperture transition into the Quiet Studio OS cockpit and interactive 3D gyroscopic orbit stage.
- **Home (One-Glance Cockpit):** answers 5 things immediately on phone (`390px`) or desktop:
  1. **Expiring today banner:** warns when any active `update` or `trend` expires within 24 hours.
  2. **Needs your yes & Film today:** scripts waiting for Gate 1, approved scripts ready to film today with a 1-tap **Teleprompter** button, and posts waiting for Gate 2.
  3. **Up next:** next scheduled posts across active channels.
  4. **Daily Auto-Run & Live Channel strip:** status of the daily 07:30 IST research auto-run (or 1-tap enable) + latest engine run log.
  5. **What Claude learned & Growth:** recent voice/style rules learned from your videos, edits, and 2x+ heaters, plus follower/view growth tiles.
- **Plan (3 sub-views: Workspace · Reel Radar · Hook Vault):**
  - **Workspace:** 3 doors (Week/Month plan, One video about…, or open Studio), Options (Pick / Drop, with Shelf-Life + First-Mover badges), and Scripts (EN | Malayalam-English toggle, Approve script / Ask changes, plus **Approved & Ready to Film** with the **v26 Teleprompter**: active reading line highlight, dimmed `[ON SCREEN]` cues, tap-to-pause, and saved speed/font size in `localStorage`).
  - **Reel Radar (v25-v26):** paste 1 or many viral Instagram/YouTube/X/GitHub URLs at once (or share them in VS Code chat). `sos-radar` deduplicates, deconstructs, checks **First-Mover chance** (`0 in niche` / `Early wave` / `Saturated`) and **Shelf Life** (`Update · 24-48h` / `Trend · 3-7d` / `Evergreen` / `Expired · avoid`), and ranks them 0-100 (`P1 Film Now` -> `P2 Queue` -> `P3 Save` -> `Skip` -> `Expired`). Includes **"Script top 3"** batch action and **"Remake as evergreen"** on expired trends.
  - **Hook Vault:** searchable hook templates by type; `"Use this"` sends the hook into the Plan/Options flow (never skips Gate 1).
- **Approve:** Failed-post recovery banner (`post.error` + Retry / Reject), **"Approve all clean"** batch button for phone, Shelf-Life expiry warnings (*"This trend expired N days ago · Tap again to post anyway"*), Viewer Panel score badge (`viewerScore`), Trial Reel / Collab badges, previews for every format (carousel 4:5, story 9:16 1-7 frames, reel/video, YouTube thumbnail, image, text, thread cards), **inline caption/title editing** (tracks `editedFrom` for `sos-learn`), and "Back to draft" with feedback note.
- **Calendar:** Toggle between **Month grid**, **14-day list**, and **Instagram 3:4 Grid Preview**, showing Shelf-Life deadline badges on time-sensitive slots.
- **Studio (Prompt Guy only):** brief + optional clip link or filename in `C:\Gaznil\social-os-media\inbox\`, plus optional Model / Effort pickers. Prompt Guy writes the paste-ready prompt with a Copy button; "Prompt + all-platform pack" also drafts one post per active account. Never runs Edit King / Motion King.
- **Accounts:** manage accounts (shows learned `bestTimes`), **"What Claude learned"** section (`voiceProfile` summary + per-rule `learnings` cards with source, date, **Remove** button, and manual rule input), **Competitors & profiles I like**, **Schedules** (with 1-tap Daily Auto-Run setup), and recent **Engine Runs**.

**Source:** `dashboard/index.html`. Published with the Artifact tool; its URL is in `private/README.md`.
