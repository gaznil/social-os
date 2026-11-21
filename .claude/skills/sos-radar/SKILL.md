---
name: sos-radar
description: Intake one or many viral/trending reel or video URLs (pasted in VS Code chat OR in the dashboard's Reel Radar), deconstruct and score them by viral priority (0-100) using platform viral/hook skills, save top hook templates to Hook Vault, and write improved EN + ML-EN scripts for Gate 1 approval.
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
   - YouTube / X / web: Agent Reach (`C:\Users\gazni\.local\bin\agent-reach.exe`) or `yt-dlp --no-browser-cookies`.
   - When a video file/direct link is available for top candidates: run `python -m tools.sos.deepdive <src> --out private/research/deepdive/radar-<id> --source <url>` to extract the 6-frame contact sheet and timestamped transcript.
3. **Score with evidence (never guess — LESSONS 15 Nov):**
   - Load the platform viral & hook skills (`ig-viral` + `ig-reel/hookscore.py` for IG/Shorts; `yt-viral` + `yt-script/hookscore.py` for YT; `x-viral` + `x-post/hookscore.py` for X).
   - Score the extracted 0–2 s hook with `hookscore.py` -> `hookScore` (0–100).
   - Check the account's `private/accounts/<accountId>/pillars.md`, `voice.md`, and `RULES.md` realism rule -> `fitScore` (0–100), `provable` (true/false), `effort` (`low`|`medium`|`high`).
   - Save the batch to the scratchpad and run `python -m tools.sos.cli score-radar <file.json>` -> deterministic `score` (0–100), `tier` (`P1`|`P2`|`P3`|`skip`), and `breakdown`.
4. **Update `inspirations/<id>`:**
   - Write `title`, `hook` (extracted first line), `hookScore`, `outlierMultiple`, `storyFormat` (one of Kallaway's 10 formats), `whyPopped` (1 concrete sentence), `ourTwist` (how we make it better/real in our voice — copy the shape, never the words), `audioNote` (string or null), `score`, `tier`, `status: "scored"`, `updatedAt`.
   - If `hookScore >= 70`, also add a reusable template to `hooks` (Hook Vault) so it compounds.
5. **Write improved script for Gate 1 approval:**
   - Automatically script the top `P1` item(s) (max 2 per batch unless the user asked for all) AND any item with `status == "script"` (user tapped "Write script" in dashboard).
   - Load `private/knowledge/storytelling-formats.md` + account `voice.md`/`style.md` + `ig-reel` (`hooks.json`, `hookscore.py`, `beats.py`). Write 3 hooks, score them, keep the winner (must be >= 50). Humanize with `ig-human` / `RULES.md`.
   - ArtifactData `add scripts` with `accountId`, `inspirationId: <id>`, `title`, `storyFormat`, `hookScore`, `en` (English script with `[ON SCREEN: ...]` beats), `mlen` (natural Malayalam-English mix), `status: "draft"`, `createdAt`, `updatedAt`.
   - Update `inspirations/<id>`: `status: "scripted"`, `scriptId`, `updatedAt`.
6. **Report:** In chat, show the priority-ranked table (Tier | Score | Title/URL | Outlier | Hook | Why & Twist) and tell the user which improved scripts are waiting for Gate 1 approval in **Plan -> Scripts**.
