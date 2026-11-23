---
name: sos-radar
description: Intake one or many viral/trending reel, video, or GitHub/news URLs (pasted in VS Code chat OR in the dashboard's Reel Radar), deconstruct and score them by viral priority (0-100), first-mover chance, relatability, and shelf life (update / trend / evergreen), save top hook templates to Hook Vault, and write improved EN + ML-EN scripts for Gate 1 approval.
---
**Rules:** `RULES.md` (repo root) wins over any outside skill when they disagree.
**Skills rule:** at each step load the skills named here (and in the platform README) before doing the work.
**Learning rule:** read `LESSONS.md` before starting (skip if already read this session). Any correction from the user, failed step, wasted spend or workaround found -> run `sos-learn` in that same turn (lesson + fix this skill + commit).
**Video rule (user, 31 Oct):** video = Prompt Guy ONLY. Never run Edit King / Motion King / HyperFrames.

1. **Intake (chat OR dashboard):**
   - If the user pasted URLs in VS Code chat: extract & deduplicate with `tools/sos/radar.py` (`extract_urls`), then ArtifactData `add inspirations` for each URL not already in `inspirations` (`accountId` = active/named account, `url`, `platform`, `userNote`, `status: "new"`, `createdAt`, `updatedAt`).
   - ArtifactData `query inspirations` where `status` in (`new`, `script`), oldest first.
2. **Deconstruct each `new` item (no login, free/cheap first):**
   - Instagram reel/post: fetch public post metadata (`apify/instagram-scraper` `directUrls` if Apify credit > $0.10, else `yt-dlp --no-browser-cookies --dump-json` / web metadata). Note views, creator median (for `outlierMultiple`), age in days, audio name (flag trending audio in `audioNote` for manual IG app add).
   - YouTube / X / GitHub / web: Agent Reach (`C:\Users\gazni\.local\bin\agent-reach.exe`) or `yt-dlp --no-browser-cookies`.
   - When a video file/direct link is available for top candidates: run `python -m tools.sos.deepdive <src> --out private/research/deepdive/radar-<id> --source <url>` to extract the 6-frame contact sheet and timestamped transcript. If it is the user's own video, also extract voice/speaking patterns via `sos-learn`.
3. **Score with evidence, First-Mover & Shelf Life (never guess — LESSONS 15 Nov):**
   - Load the platform viral & hook skills (`ig-viral` + `ig-reel/hookscore.py` for IG/Shorts; `yt-viral` + `yt-script/hookscore.py` for YT; `x-viral` + `x-post/hookscore.py` for X).
   - Score the extracted 0-2 s hook with `hookscore.py` -> `hookScore` (0-100).
   - `accountIds` (array, may be empty) = every account the user ticked; score fit for each and use the best one as `accountId`.
   - Check the account's `private/accounts/<accountId>/pillars.md`, `voice.md`, and `RULES.md` realism rule -> `fitScore` (0-100), `relatabilityScore` (0-100, local Kerala/Malayalam-English + AI workflow relatability), `provable` (true/false), `effort` (`low`|`medium`|`high`).
   - Check **first-mover chance** in our niche: `firstMover` = `"untapped"` (0 covered it yet) | `"early"` (1-2 creators) | `"saturated"` (everywhere).
   - Classify **shelf life**: `shelfLife` = `"update"` (24-48h window, set `expiresAt`) | `"trend"` (3-7d window, set `expiresAt`) | `"evergreen"` (`expiresAt: null`).
   - Save the batch to the scratchpad and run `python -m tools.sos.cli score-radar <file.json>` -> deterministic `score` (0-100), `tier` (`P1`|`P2`|`P3`|`skip`|`expired`), `expiryState`, `hoursLeft`, `daysLeft`, and `breakdown`.
4. **Update `inspirations/<id>`:**
   - Write `title` (the idea in plain words, never the URL), `concept` (1-2 plain sentences: what the reel shows and why it works), `hook`, `hookScore`, `outlierMultiple`, `relatabilityScore`, `firstMover`, `shelfLife`, `expiresAt`, `storyFormat` (one of Kallaway's 10 formats), `whyPopped` (1 concrete sentence), `ourTwist` (how we make it better/real in our voice), `audioNote` (string or null), `score`, `tier`, `status: "scored"`, `updatedAt`.
   - If `hookScore >= 70`, also add a reusable template to `hooks` (Hook Vault) so it compounds.
5. **Write improved script for Gate 1 approval:**
   - Automatically script the top non-expired `P1` item(s) (live `update`/`trend` items first!) AND any item with `status == "script"` (including expired items the user tapped **"Remake as evergreen"** on, where `shelfLife` was set to `"evergreen"`).
   - Load `private/knowledge/storytelling-formats.md` + account `voice.md`/`style.md` + `learnings` + `ig-reel` (`hooks.json`, `hookscore.py`, `beats.py`). Write 3 hooks, score them, keep the winner (must be >= 50). Humanize with `ig-human` / `RULES.md`.
   - ArtifactData `add scripts` with `accountId`, `inspirationId: <id>`, `title`, `storyFormat`, `hookScore`, `shelfLife`, `expiresAt`, `firstMover`, `en` (English script with `[ON SCREEN: ...]` beats), `mlen` (natural Malayalam-English mix in the user's learned voice), `status: "draft"`, `createdAt`, `updatedAt`.
   - Update `inspirations/<id>`: `status: "scripted"`, `scriptId`, `updatedAt`.
6. **Report:** In chat, show the priority-ranked table (Tier | Score | Shelf Life | First Mover | Title/URL | Hook & Twist) and tell the user which improved scripts are waiting for Gate 1 approval in **Plan -> Scripts**.
