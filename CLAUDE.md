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
  Ideas tab + model/effort picker to Phase 1; new Phase 2 = video studio (Prompt Guy from the
  dashboard), Phase 3 = research (Apify no-login competitor radar, reel deep dive, Agent Reach no-login channels,
  last30days). yt-dlp not installed; ffmpeg is.
- **30 Oct 2026 (round 3, user decisions):** (1) video = **Prompt Guy ONLY** (31 Oct: no Edit King / Motion King, no "Run it"); (2) **zero accounts now**: the user will create ONE account later, so Task 3 waits and the dashboard must
  work empty; (3) every format (carousel, story, reel, image, text, thread) previews in the dashboard's Approve tab;
  `story` format added to the plan (Task 2 Step 0); (4) model picker uses Claude's names: Haiku 5.5 / Sonnet 5.5 /
  Opus 5.5 + Low / Medium / High. **Agent Reach: INSTALLED by the user 30 Oct**, tested OK (YouTube + Reddit search,
  no login). Role = free read-only research (see engine/research README).
- **31 Oct 2026:** all 20 wishlist items APPROVED (docs/WISHLIST.md, with the user's music/voice/AI-video rules). Shorts generator copied as a method, not installed.
  **HANDOFF 30 Oct:** user switched chats. **Next = Task 2** (Step 0 story rule, then dashboard v1). Nothing else pending.

- **31 Oct 2026:** Task 2 Steps 0-4 + 6 DONE: story rule (28 tests), `docs/DATA.md`, dashboard v1 published
  (URL in `private/README.md`), settings/main + test post `posts/test-1` seeded. **Waiting on the user:** press Approve on
  the test card on their phone; then Claude checks `posts/test-1` shows approvedBy "dashboard" and deletes it. Then Task 3 (needs first account).
- **31 Oct 2026 (redesign v3, user ask):** dashboard = light, classy (BlueYard taste): 3D iridescent orb with orbiting
  platform logos, one-line heading + "Talk to Claude" -> Claude-style prompt box (model/effort, Save for later, Transcribe
  -> voice blob; real mic is blocked in artifacts, so it falls back to the phone keyboard mic), horizontal rail of 9 live
  channel cards (Showcase = labelled demo, Live = real queue), real brand logos (simple-icons 13.21.0) everywhere.
  Accounts tab has "Add account" -> writes `accounts/<id>` status `setup` + a `messages` doc; Claude's next run finishes
  setup (sos-account skill, Task 3). Not yet seen on a real screen by Claude; user checks on phone.
- **31 Oct 2026 (v4):** Claude-style model/effort menus (no native selects); voice mode = full screen, user's blob kept
  (blue/violet/pink/mint), reacts to incoming words + Claude's spoken reply (speechSynthesis). Artifacts have NO mic
  permission on this account (checked capability list 31 Oct) -> keyboard mic. "Live channels" = pinned section:
  vertical scroll moves the cards sideways.
- **31 Oct 2026 (v5, checked in Playwright desktop 1440 + phone 390):** fixed rail stretching the page (grid track
  minmax(0,1fr)) which had hidden the orb and killed the sideways scroll; orb now lit/glossy, orb above text on phones,
  cards bleed edge to edge. How to preview locally: wrap the page in a doctype file and serve it with Playwright
  `page.route(url, r => r.fulfill({path}))` (file:// and local servers are blocked).
- **31 Oct 2026 (v6, user choice):** LIGHT ONLY (user liked the light Playwright view; dark blocks removed). Control room
  is ONE pinned horizontal strip: hero panel (orb + heading + Talk to Claude + pipeline) -> "Live channels" title ->
  9 channel cards; vertical scroll moves it sideways. User reverted v5 then asked for it back (reapplied).
- **31 Oct 2026 (v7):** voice agent: hidden input fed by Win+H / keyboard mic, blob reacts per word, 2 s pause auto-sends,
  reply spoken with a free browser voice (female first: Neerja/Aria/Jenny/Sonia/Hazel..., picker top-right). Agent tools
  (sample tools): save_idea, leave_note_for_claude. It can never approve/publish. Keeps last 8 turns per voice session.
- **31 Oct 2026 (v8):** prompt box has TWO buttons: mic = plain transcribe into the box (no auto-send); round
  gradient "voice mode" button = the voice agent. Bigger orb in its own area above the pipeline; hero keeps its height
  when Claude opens. Background "threads": fixed canvas, 7 faint lines that bend with scroll, one platform-coloured dot rides each.
- **31 Oct 2026: DASHBOARD DESIGN SIGNED OFF by the user ("done dashboard design build and we move on").** v9 = voice
  screen fits short screens. Don't redesign unless asked. **Next:** finish Task 2 Step 5 (user presses Approve on
  `posts/test-1`, Claude verifies approvedBy "dashboard" then deletes it), then Task 3 (needs the user's first account:
  platform + one niche).
- **31 Oct 2026 (final design touches, v13-14):** voice mode has only ✕ + minimise (auto-send after 2 s pause, Enter
  sends); minimise = floating pill bottom-right, keeps listening/speaking while the page scrolls; voice list on top
  (z-index fix) and scrollable. Dashboard is published and live at the URL in `private/README.md`.
  **HANDOFF 31 Oct:** user moved to a new chat. **Next = Task 2 Step 5:** ask the user to tap Approve on the
  "TEST - do not publish" card, then `ArtifactData get posts/test-1` must show status "approved", approvedBy
  "dashboard", approvedAt set -> delete posts/test-1 -> Task 2 done. Then Task 3 (first account: platform + one niche).

- **31 Oct 2026: TASK 2 DONE.** User tapped Approve on `posts/test-1`; verified status "approved", approvedBy "dashboard",
  approvedAt set; test doc deleted. **Next = Task 3** (needs the user's first account: platform + one niche).

- **31 Oct 2026: ROADMAP REORDERED (user approved).** Phase 2 = research engine + style learning + per-account schedules
  screen; 3 = video studio + "one video -> all-platform pack"; 4 = results loop; 5 = more platforms. See plan Roadmap.
  **Next still = Task 3** (user gives first account: platform + niche).

- **31 Oct 2026: USER RULE: build every part now; the user adds/connects accounts themselves when they want.**
  Phase 1 skills written: `sos-account` (now also learns style from past posts -> voice.md + style.md, can save
  status `setup` before Composio connects), `sos-create`, `sos-publish` + `platforms/{linkedin,instagram}/PUBLISH.md`,
  `sos-inbox` (session-start rule added). Dry run: future approved post -> `due` returns [] (nothing posted). Tests OK.
  **Waiting on accounts (not on build):** Task 3 Step 3, Task 4 Step 2, Task 5 Step 5. **Task 6 (cloud publisher)
  needs the user's yes** to create a cloud scheduled task. **Next build = Phase 2 plan (research engine + schedules screen).**

- **31 Oct 2026 (Phase 2 build, part 1):** dashboard v15 published with a **Schedules tab** (`schedules` collection,
  docs/DATA.md): user adds/pauses/removes; Claude syncs real cloud tasks via new `sos-schedules` skill (creating one
  still needs the user's yes in chat). New `sos-research` skill (foundation files, Apify `apidojo/instagram-scraper`
  verified $0.50/1,000 posts on the FREE tier 31 Oct; free plan = $5/month credit, stops when used, no charge; Agent
  Reach for the rest; outliers -> ideas with "Why" -> calendar drafts). **Not yet built:** Phase 3 video studio + "one video -> pack", Phase 4 results (`sos-results` named but not written).

- **31 Oct 2026 (Phase 2, part 2): deep-dive tool DONE** (`tools/sos/deepdive.py`, 33 tests pass). Video file or
  direct link -> 6-frame contact sheet + timestamped transcript + card.md (Hook / Formula / Our version for Claude to
  fill). **User decision: transcription = ElevenLabs** (Scribe v2, key `ELEVENLABS_API_KEY` user variable, free plan
  ~12 min STT/month shared with voiceovers); local faster-whisper `small` (cached) is the automatic fallback. Live
  test passed via ElevenLabs. **Next build = Phase 3** (video studio + "one video -> all-platform pack"), then Phase 4 `sos-results`.
- **31 Oct 2026: skills wired everywhere (user ask: "if a skill exists, use it").** Each `sos-*` skill now opens with a
  skills rule and names the skill per step (research: last30days, ig/yt/x-viral, firecrawl, ads extractor, planners,
  llm-council; account: niche-content-strategist, profile scorers, linkedin-interviewer; create: writers, repurposers,
  humanizers incl. content-humanizer, frontend/canvas/banner design, prompt-guy for video). **`last30days` vendored** (`.claude/skills/last30days`, MIT, commit in THIRD_PARTY.md) + yt-dlp
  installed. Test run passed 31 Oct (user allowed it). Always run with `--no-browser-cookies`.
- **31 Oct 2026: USER RULE: video = Prompt Guy ONLY.** Social OS writes the video prompt and stops. It never runs
  Edit King, Motion King, faceless-explainer or HyperFrames; no "Run it" button. All notes fixed. Phase 3 video studio =
  brief/clip -> Prompt Guy prompt with Copy + "one video -> all-platform pack" for the text/image posts.
  **last30days test run PASSED** (free sources, no cookies: Reddit 6 threads + HN 6 stories in 8 s).

- **31 Oct 2026: TASK 3 STARTED, first account = Instagram `ig-ai-tools`** (handle in `private/` only). Public profile +
  22 posts read via Apify (~$0.09 of free credit); `private/accounts/ig-ai-tools/` has profile, voice, style (top reels,
  patterns). Dashboard `accounts/ig-ai-tools` status `setup`, postsPerWeek 3 (default). Composio Instagram link sent,
  connection `instagram_molt-inane` **ACTIVE** (31 Oct). User answers: on camera yes (this account), speaks Malayalam +
  sometimes Manglish (captions English), 3 posts/week as the minimum (user may post more any time). Dashboard account
  status `active`. **Next: sos-research first run for ig-ai-tools** (pillars/formats, competitors, outliers, ideas).

- **31 Oct 2026: research run 1 for ig-ai-tools, step 1 DONE.** `pillars.md` (5 topics, Claude chose the mix from past
  posts) + `formats.md` in `private/`. **User choice: more carousels -> 4 posts/week = 2 reels + 2 carousels**
  (dashboard postsPerWeek 4). Steps 2-5 DONE: 12 competitors in `competitors.md` (ig-viral mix: direct/adjacent/outsized),
  outliers ranked (ig-viral method, Apify ~$0.55), note `private/research/2026-10-31-ig-ai-tools.md`, 6 ideas `ideas/r1031-*`
  in the dashboard (3 carousels, 3 reels). Top pattern: "N secret ChatGPT codes/prompts" (264x). **Next: step 6** =
  sos-create drafts for the first week (2 reels + 2 carousels) from those ideas, waiting for the user's Approve.
  Note: ig-viral forbids scraping services; Social OS keeps Apify by design (public, no login, low volume) and uses ig-viral for picking + ranking.

- **31 Oct 2026: SELF-LEARNING LOOP ADDED (user ask).** New `sos-learn` skill + `LESSONS.md` (5 lessons from today).
  Method copied from claude-reflect / claude-reflect-system / okteto lessons (found via web search + GitHub connector);
  plugin NOT installed (review band is terminal-only, needs manual /reflect, changes Claude settings).
  sos-research now loads ig-viral & co. for competitor picking + ranking. **Next still: research step 6** (first week's drafts).

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
- **Skills first:** every `sos-*` skill starts with a skills rule and names the skill for each step; load them before the work,
  and use any other installed skill that fits better (then add it to `SKILLS.md`). Before writing or building, load the skill named in the platform/stage README. If a better one appears, compare
  by opening both (not by stars) and record the result in `SKILLS.md`.
- **Session start:** in every session in this project, run the `sos-inbox` skill first (it reads `LESSONS.md`).
- **Learn from every mistake:** any user correction, failed step or wasted spend -> `sos-learn` in the same turn: lesson in
  `LESSONS.md` + fix the skill that caused it + commit. The system improves itself; the user never repeats a correction.
- **Finding a system/skill to copy:** web search AND the GitHub connector (`search_repositories`, by stars); open the top 2-3, copy the best of each.
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
