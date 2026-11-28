---
name: sos-research
description: Daily auto-run & research engine. Finds what is viral and trending across GitHub trending/releases, Reddit/HN/YouTube, Web/AI news, Reel Radar URLs, and competitors; checks first-mover advantage and shelf life (update / trend / evergreen); writes ranked options and EN + Malayalam-English scripts in the user's learned voice for approval.
---
**Rules:** `RULES.md` (repo root) wins over any outside skill when they disagree.
**Skills rule:** at each step load the skills named here (and in the platform README) before doing the work. If another installed skill fits a step better, use it too and add it to `SKILLS.md`.
**Learning rule:** read `LESSONS.md` and `learnings` (for the active account) before starting. Any correction from the user, failed step, wasted spend or workaround found -> run `sos-learn` in that same turn (lesson + fix this skill + commit).

Read `engine/research/README.md` first. Never log in anywhere; public data only.

1. **Foundation (first run per account):** if `private/accounts/<id>/pillars.md` or `formats.md` is missing, write them yourself from `profile.md` + `style.md` (what already got the most plays). Load `niche-content-strategist` + `content-strategy`. Do not ask the user to approve percentages; ask only a plain either/or with an example post if a choice is truly theirs. **User picks first:** ArtifactData `query competitors` where status == "remove": remove each from `competitors.md` and delete the doc. Then `query competitors` where status == "new": add each to `competitors.md` as group `user pick`, scrape it like the others, then `update` it to status `tracked` with a one-line `note` of what we learned. If `competitors.md` is empty: load the platform viral skill (`ig-viral` / `yt-viral` / `x-viral` / `linkedin-hook-extractor`) and use its mix: 4 direct, 4 adjacent, 2-4 outsized.
2. **Collect from 6 Sources (Daily Auto-Run, free/cheap first):**
   - **GitHub trending & releases:** check GitHub trending repos, fast star growth (stars/day), and major AI tool releases (`agent-reach.exe` github channel or GitHub search).
   - **Reddit, Hacker News & YouTube:** run `last30days` (`.claude/skills/last30days`, keyless `--no-browser-cookies`, `LAST30DAYS_ALLOW_ENGINE_PLAN=1 --auto-resolve`) + `agent-reach.exe` (youtube/reddit) + `yt-viral`.
   - **Web & AI news:** `firecrawl-search` / `firecrawl-competitive-intel` for newly launched AI tools, workflows, and announcements in the last 24-48 hours.
   - **Reel Radar inbox:** check `inspirations` where `status` in (`new`, `script`) via `sos-radar`.
   - **Competitors:** Instagram Apify actor `apidojo/instagram-scraper` (~$0.50/1,000 posts on free plan).
   - **Apify credit check (every run, BEFORE any Apify call; never trust an old note):** read `https://api.apify.com/v2/users/me/limits` (Apify MCP resource read; the cloud run may not have that tool: then just run the capped call, it is refused if credit is gone, and only a real refusal counts as "exhausted"). Left = `maxMonthlyUsageUsd` - `monthlyUsageUsd`. Free plan = $5 per cycle (cycle dates are in that reply; 17 Nov - 16 Dec 2026). **Run cap $0.20** (weekly broad-account scan $0.30), and never spend below $0.50 left. Only if the check itself fails or credit is under $0.50, skip Apify and say the real number in the run summary. A "credit used up" line in STATUS/old notes means nothing; the live number decides.
   - **Broad-reach lane (daily, user ask 28 Nov 2026):** topics every normal person needs, not only AI fans. Two parts:
     1. **Fresh (daily, ~$0.16):** `apify/instagram-search-scraper` `searchType: "popular"`, `searchLimit: 15`, 4 keywords picked each day (rotate) from `private/accounts/<id>/broad-keywords.md` (everyday jobs: resume, Excel, email, study, photo fixes, small-shop tasks, money, travel, health admin). Price $0.0027/result (checked 28 Nov); 4 x 15 = $0.16. Keep reels with views >= 5x the creator's median (ig-viral ranking).
     2. **Already trended (weekly, Sunday run, ~$0.25):** `apify/instagram-profile-scraper` or `apidojo/instagram-scraper` on the last 30 reels of 4-5 broad accounts from `broad-keywords.md` ("big broad accounts"); keep the top ones by outlier multiple. Old is fine: mark `shelfLife: "evergreen"`.
     Each kept idea gets `relatability` = plain question "would a non-tech person need this THIS WEEK?" (yes / maybe / no); `no` is dropped. Then apply the **"Claude can do this" frame**: restate the idea as "Claude can [do the everyday job] for you" (free, 1 prompt, visible result in 2 s), and only keep it if we can test it ourselves (LESSONS: real results only). Free text sources for the same frame (no Apify): `last30days` / Reddit "what do you use ChatGPT/Claude for", YouTube search "[job] with AI". The CTA is the account's one keyword (Porotta); this skill only writes the CTA line, it never builds the follower gate.
   - **Our own heaters & learnings:** check `learnings` and `accounts/<id>.voiceProfile` so topics match what already popped.
3. **Evaluate First-Mover, Relatability & Shelf Life (`tools/sos/radar.py`):**
   - **First-mover check:** check whether Malayalam / Indian AI creators have covered the topic yet:
     - `firstMover: "untapped"` -> *Nobody covered it yet (First mover)* (+8 pts)
     - `firstMover: "early"` -> *1-2 creators, still early* (+4 pts)
     - `firstMover: "saturated"` -> *Already everywhere (skip unless our angle is much stronger)* (-8 pts)
   - **Relatability (`relatabilityScore`, 0-100):** how relatable it is for a Kerala / Malayalam-English + AI tools audience and daily workflows.
   - **Shelf life (`shelfLife` + `expiresAt`):**
     - `"update"` (news, launch, new model/repo release): 24-48 hour window (`expiresAt` set).
     - `"trend"` (viral format, hot topic): 3-7 day window (`expiresAt` set).
     - `"evergreen"` (how-to, workflow, timeless tool guide): `expiresAt: null`.
   - **Engagement per view (added 28 Nov, display only, does not change the score):** for every competitor/popular reel add `likesPerView` and `commentsPerView` to its note (Apify gives likes, comments, views; sends and watch time of OTHER people's reels are invisible, so say "proxy"). Prefer, among equal picks, the one with the higher likes per view: it means the views came with approval, not just reach.
   - Run `python -m tools.sos.cli score-radar <items.json>` so live `update`/`trend` P1s automatically outrank `evergreen` P1s and expired items are flagged `tier: "expired"`.
4. **Deep dive (top 3 videos, PC only):** `python -m tools.sos.deepdive <video file or direct link> --out private/research/deepdive/<date>-<id>-<n> --source <post link>` -> `frames.jpg`, `transcript.json`, `card.md`. Also extract voice/hook learnings into `learnings` via `sos-learn`.
5. **Write Options & Auto-Draft Top Scripts in Learned Voice:**
   - Write `private/research/<date>-<id>.md` (sources with links + numbers).
   - Add top ranked topics to `options` (with `shelfLife`, `expiresAt`, `firstMover`, `storyFormat`, `why`).
   - For the top 2-3 P1 topics (especially live `update`/`trend` items), immediately write `scripts` docs (`en` + `mlen` in the user's learned `voiceProfile`, `hookScore` from `hookscore.py`, `shelfLife`, `expiresAt`, `firstMover`, `status: "draft"`) so the user wakes up with scripts ready to approve or film.
6. **Calendar & Runs Log:**
   - Plan with `content-strategy` + platform planner (`ig-plan` / `yt-plan` / `x-plan` / `linkedin-content-planner`).
   - Run `sos-learn` for anything learned or corrected.
   - ArtifactData `set runs/research-<YYYYMMDD-HHMM>` with a 1-line summary (`"Found 6 topics (2 GitHub repos, 2 reels, 2 updates), 3 scripts ready for your yes"`). Commit + push `private/`.
7. **Morning brief (last step of every daily run):** ArtifactData `set briefs/<YYYY-MM-DD>` (India date; a second run the same day overwrites it): `date`, `createdAt`, `summary` (one plain line: sources checked, topics found, scripts written, anything skipped, money spent), `sources` (names that worked), `top` (max 3, best first: `{ref: "options"|"scripts"|"inspirations", id, accountId, title, format, score, shelfLife, expiresAt, firstMover, what, why}`; `what` = what the thing actually IS and does, in plain everyday words a non-developer gets at once (e.g. "A Claude skill that draws clean diagram slides from one prompt"), never just the tool name; `why` = one short line on why now; live update/trend items before evergreen; never an expired item), `learned` (0-2 short lines from `learnings` written today), `newHooks` (count added to `hooks` today). The dashboard Home shows it as the Morning brief card; keep every text short.
   Every `options` doc also gets the same plain `what` line (what the tool/news/topic is, in simple words), so the user can choose or skip without looking it up.
   Every `options` doc in the brief's top 3 also gets `hook` (the opening line, one sentence), `concept` (3-5 short numbered lines: what the post shows, step by step, and how it ends) and `needs` (what the user must do or check first, e.g. test it ourselves, confirm a price; never invent numbers). The dashboard shows them in the popup that opens when the user taps a pick, with Approve / Skip. Missing = the popup says Claude writes the full idea after approval.
