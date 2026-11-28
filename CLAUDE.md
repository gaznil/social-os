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

- **31 Oct 2026: SELF-LEARNING LOOP ADDED (user ask).** New `sos-learn` skill + `LESSONS.md` (6 lessons from today).
  Method copied from claude-reflect / claude-reflect-system / okteto lessons (found via web search + GitHub connector);
  plugin NOT installed (review band is terminal-only, needs manual /reflect, changes Claude settings).
  Wired into EVERY sos skill (account, research, create, publish, schedules, inbox) + SYSTEM.md "Learning loop". sos-research loads ig-viral & co. for competitor picking + ranking. **Next still: research step 6** (first week's drafts).
- **31 Oct 2026: USER ASK, design item 7 queued: Growth section** (after the horizontal scroll ends -> vertical, one still
  section, account switch buttons, followers/views graph). Spec in the plan roadmap row "4b"; built with Phase 4 `sos-results`.

- **31 Oct 2026: research step 6 DONE, week 1 drafts in Approve** (posts `w1-claude-commands` carousel Sun 1 Nov,
  `w1-stop-scrolling` reel Tue 3, `w1-photo-codes` carousel Thu 5, `w1-setup` reel Sat 7; all 19:00). Carousel PNGs in
  `C:\Gaznil\social-os-media\ig-ai-tools\` and uploaded as dashboard assets (`/_blob/<id>` in mediaUrls). Dashboard v16
  now declares `assets` (capabilities db, sample, user, assets) + carousel previews 4:5. v17: Live channel cards animate like Showcase (real slides slide, unfilmed reel plays its script as captions, text posts type out). Reels show the Manglish script in
  `problems` until the user films them. **Note for sos-publish:** `/_blob` URLs are not public; publish from the local PNGs
  (Composio staged files). **Next:** user taps Approve/Back to draft; films the 2 reels.

- **31 Oct 2026 (v18):** Live cards show a post with status `draft` as a blurred, shimmering card in its own format
  (carousel slides slide, reel frame, text skeleton). sos-create step 0 now writes the `draft` doc first so this shows.
  **USER ASK, NEXT BUILD: carousel design library** (user: current slides are too plain). Plan: (1) user drops reference
  carousels in `C:\Gaznil\social-os-media\carousel-library\from-gaznil\`; (2) Claude collects more (top carousels from the
  12 competitors via Apify, plus GitHub: Hainrixz/open-carrusel, FranciscoMoretti/carousel-generator, jtian7823-ux/infographic-carousel
  (10 layouts), roboshivam1/dark-tech-carousel-templates, open-design social-carousel; compare by opening, copy best);
  (3) build 8-12 reusable HTML layouts + rules in `templates/carousel/`, wire into sos-create step 4; (4) re-render week 1 carousels.

- **31 Oct 2026 HANDOFF:** carousel library WAITS for the user's references (they add them later). **Next build = Phase 3**
  (video studio: brief/clip -> Prompt Guy prompt + "one video -> all-platform pack"), then Phase 4 `sos-results`.
  Waiting on the user: Approve/Back to draft on week 1 drafts; film the 2 reels.

- **31 Oct 2026: user rejected `w1-photo-codes` ("weak and unrealistic in every way": "codes" were 3-line prompts, no real
  examples). Realism rule added to sos-create + LESSONS. Dashboard v19: Accounts tab has **"Profiles I like"** (`competitors`
  collection, docs/DATA.md); sos-research adds those picks first, always kept. Carousel scraping works
  (`apify/instagram-scraper` `images` = all slides) but our 12 competitors post no real carousels and free hashtag search
  gives only new posts (~$0.87 spent today, lesson saved). **Waiting on the user:** add 2-3 carousel profiles they like
  in "Profiles I like"; then Claude scrapes their slides into the carousel library and rebuilds the photo-codes idea
  (or drops it). Phase 3 still next after that.

- **31 Oct 2026 HANDOFF:** "Competitors & profiles I like" box = full competitors (all content, not only carousels);
  user adds picks later. **Phase 3 plan written:** `docs/plans/2026-10-31-phase-3-video-studio.md` (4 tasks, inline).
  **Next = Task 1** (`tools/sos/studio.py` + tests). Nothing waiting on the user except Approve on week 1 drafts + filming.

- **31 Oct 2026: PHASE 3 (video studio) DONE.** `tools/sos/studio.py` (`studio-check`, `pack-plan`; 42 tests pass), new
  `sos-studio` skill (wired into sos-inbox, SYSTEM.md, docs/DATA.md `jobs`, engine/create README), dashboard **v21 Studio tab**
  (brief + optional clip -> "Get prompt" / "Prompt + all-platform pack"; prompt shows with Copy). Dry run passed with a TEST
  placeholder; test job deleted. **User corrections:** a test never writes a real prompt ("who said to give prompt now?");
  Cluely reel prompt **v2 = 0/100** (logged in prompt-guy + MOTION.md; unscored prompts are unproven). LESSONS updated.
  **Next build = Phase 4 `sos-results`** (+ Growth section 4b). Waiting on the user: Approve on 3 week-1 drafts (first one
  Sun 1 Nov 19:00), film the 2 reels, add "Profiles I like".

- **31 Oct 2026: PHASE 4 + 4b (results + Growth) DONE.** `tools/sos/results.py` (`best-times`, `growth`; 48 tests pass),
  new `sos-results` skill (numbers via Composio, `stats` + post `metrics` + account `bestTimes`, ONE change a week,
  monthly llm-council), dashboard **v22 Growth section** under the Control room scroll (account buttons, followers line,
  4 tiles; checked at 390 px). Not run on real numbers yet: needs an active account with a Composio link.
  User asked: keep it inside Claude (no own domain); the Claude bar can't be removed. **Next = Phase 5** (more platforms).

- **31 Oct 2026: PHASE 5 (more platforms) BUILT.** PUBLISH.md for YouTube, Facebook, Threads (Composio has a `threads`
  toolkit, so Threads is automatic now; only X stays copy + open). Dashboard **v23**: "Approve + post now" (sets plannedAt
  now; the next publish run sends it). **Not done, needs the user:** Composio connections for YouTube/Facebook/Threads
  (only Instagram + LinkedIn are linked); the X Composio test (a real post = needs a yes in chat); "Porotta link"
  (meaning unclear, ask). All roadmap phases now built; nothing has run on real numbers yet.

- **1 Nov 2026: YouTube account `yt-ai-tools` started (user ask).** Claude cannot create a Google account or channel, so the
  user makes the channel (steps given in chat); Claude wrote the channel kit + Shorts rules in `private/accounts/yt-ai-tools/`
  and the dashboard account (status `setup`). Phase 1 = the user's Instagram reels posted as Shorts one at a time by hand
  (3-minute Shorts verified in Google Help); Phase 2 = long videos later. Composio YouTube ACTIVE (1 Nov), dashboard account active.
  **Next:** user makes the channel and finishes the Composio link -> set account `active`, `composioAccountId`; then sos-publish can upload.

- **1 Nov 2026: IDEA PARKED (user will say when ready): "run everything from the dashboard".** Findings: the page can call the user's
  connectors (`mcp` capability: Composio, Apify, Canva, Higgsfield) and has its own Claude (`sample`), so posting, research and text
  drafting can run from the page while it is open. The top bar is Claude's own frame, cannot be removed from page code (no hide
  option found; own hosting = loses free runtime, costs an API key). Untested: Composio YouTube upload from the page, video staging,
  browser ffmpeg for simple edits, Composio cloud sandbox for ffmpeg, a VS Code session as worker. Plan if resumed: test button first, Run log strip, Pause-everything button.
  **Nothing to build until the user says.** YouTube account `yt-ai-tools` is connected; the user posts Shorts by hand meanwhile.

- **2 Nov 2026 (OUTDATED, fixed 28 Nov):** Apify free credit was used up that cycle. The cycle reset 17 Nov (now $5, ends 16 Dec; checked live 28 Nov: $0.0017 used). Never trust this line: check `users/me/limits` live (see sos-research). Free sources still used: last30days (needs `LAST30DAYS_ALLOW_ENGINE_PLAN=1 ... --auto-resolve` when run
  inside Claude Code), Firecrawl, Agent Reach. Used today for the explainer page's first topic (Prompt Guy project).

- **8 Nov 2026: STORY FORMATS + NEW MAIN IDEA (user notes, discussing, not built yet).** Kallaway 10 story formats in
  `private/knowledge/` (wired into sos-create + sos-studio). User's purpose = "social partner", idea-first:
  (1) user idea / topic / GitHub repo -> research -> script -> **user approves the SCRIPT** -> versions for every platform
  incl. **carousel**; (2) user video -> Prompt Guy -> all versions; (3) self-found ideas from IG + GitHub trends + X trends
  (X free route unverified) using story formats; (4) week + month plan, every slot swappable for the user's own content.
  **Dashboard gets an account switch at the top: pick one account, the whole dashboard works only for it.** Plan v2 written: `docs/plans/2026-11-08-v2-social-partner.md` (waiting for user yes). Also asked: research 4 sources, options->script, EN + Malayalam-English toggle, Codex image_gen + OpenMontage (no Canva), thumbnails, full skill audit + own plugin.

- **8 Nov 2026 HANDOFF: plan v2 APPROVED by the user ("yes, start with audit").** Carousel images = Codex image_gen or
  real images via OpenMontage; thumbnail = best video frame, else Codex improves that frame, then designed. Dashboard
  lessons from the user's reference carousel added to the plan (Hook Vault, heaters, competitor tracker, scheduler,
  month calendar, trending feed). **Next (new chat) = Step 1 skill audit** (read all ~80 skills fully -> `docs/skill-audit.md`
  -> own `social-os` plugin + RULES.md). Then dashboard v24.

- **8 Nov 2026: plan v2 STEP 1 (skill audit) DONE.** ~50 skills read (creation skills whole, engagement/audit skills for
  rules) -> `docs/skill-audit.md` (13 conflicts, each with the call made) + `RULES.md` (one rule per task; beats any
  outside skill; wired into all 9 sos-* skills + rules here). Key calls: zero em dashes, natural rhythm, IG 3 hashtags,
  comment-keyword ask IG only (never LinkedIn). **Next = step 1b:** package RULES.md + sos-* as own `social-os` plugin,
  then dashboard v24 (account switch).

- **8 Nov 2026: plan v2 STEP 1b DONE.** Own plugin `social-os` = repo root is plugin + marketplace (`.claude-plugin/`),
  9 sos-* skills listed in place, `claude plugin validate .` passed, loads all 9 (~750 tokens always-on); 50 tests pass.
  Not installed (not needed inside the repo). **Next = step 2: dashboard v24** (account switch on top, Options screen,
  Script screen with EN | ML-EN + Approve script, month calendar with swap, previews; plus Hook Vault etc. from the plan).
  Two old research ideas (`r1031-tools-sheet`, `r1031-uninstall`) still `new`: left for the v2 options flow, not auto-drafted.

- **10 Nov 2026: plan v2 STEP 2 (dashboard v24) DONE + published.** Account switch in the header (every tab filters to
  one account; remembered per device), **Plan tab** (doors A week/month, B topic/repo, C -> Studio; Options to Pick/Drop;
  Scripts with English | Malayalam-English toggle + Approve script / Ask changes), **Hook Vault tab** (search + type chips,
  "Use this" -> idea), **Calendar = month grid** (tap a slot: Use my own content / New options / Remove) + the 14-day list.
  New collections `options`, `scripts`, `hooks` in docs/DATA.md; sos-inbox step 1b handles them. Checked in Playwright at
  390 px with fake data (no errors, no sideways scroll). Not built from the plan's list yet: analytics heaters, competitor
  tracker auto-run, trending feed (they need step 3 research v2). **Next = step 3: research v2** (4 sources every run).
- **21 Nov 2026: Social OS v25 + v26 (Quiet Studio OS, Reel Radar, Daily Auto-Run, Self-Learning & Shelf-Life Expiry) DONE.**
  1. **Engine & CLI (`tools/sos/`):** Fixed `MANUAL_PLATFORMS = {"x"}` (Threads is automatic via Composio), 1-7 story frames in
     `preflight.py` and `platforms/instagram/PUBLISH.md`, null-follower guard + `find_heaters` (`heaters` CLI: 2x+ median outliers
     and 90-day evergreen recycling) in `results.py`, and built `tools/sos/radar.py` (`score-radar` CLI: exact tracking-param
     cleaner, IG `/p/`+`/reel/`+`/reels/` deduplication, First-Mover bonus/penalty, Relatability score, and `update`/`trend`/`evergreen`
     Shelf-Life expiry engine where live trends outrank evergreen P1s and expired items sink to `tier: "expired"`).
  2. **Skills (`sos-radar`, `sos-research`, `sos-learn`, `sos-inbox`, `sos-results`, `sos-publish`):** Added `sos-radar` to
     `.claude-plugin/plugin.json` (10 skills total); upgraded `sos-research` to the 6-source Daily Auto-Run (GitHub trending/releases,
     Reddit/HN/YouTube, Web/AI news, Reel Radar, Competitors, Heaters); upgraded `sos-learn` + `sos-inbox` to extract structured
     voice/edit/hook rules from video transcripts (`deepdive.py`), caption inline edits (`editedFrom`), script notes (`note`),
     draft feedback (`feedbackNote`), and heaters into `learnings/{id}` and `accounts/{id}.voiceProfile`.
  3. **Dashboard v26 (`dashboard/index.html`):** Rebuilt into the **Quiet Studio OS** (6 tabs: `Home`, `Plan`, `Approve`,
     `Calendar`, `Studio`, `Accounts`) with multilingual Apple-style Welcome screen + Iris reveal, 3D Liquid-Glass Pearl Sphere
     orbit stage, removed dead v24 horizontal-scroll code and hidden `#threads` loop, added Shelf-Life & First-Mover badges
     everywhere (`Update · Nh left`, `Trend · Nd left`, `Evergreen`, `Expired · avoid` with **Remake as evergreen**), One-Glance
     Home (**Film Today** card with 1-tap Teleprompter, Expiring-Today warning banner, Daily Auto-Run strip, Heaters & Learnings),
     **What Claude learned** card in `Accounts` (with **Remove** button on every rule), **"Script top 3"** in Radar, **"Approve all clean"**
     + expired-post warning in Approve, and upgraded Teleprompter (active reading line, dimmed `[ON SCREEN]` cues, tap-to-pause,
     `localStorage` speed/font persistence).

- **22 Nov 2026: v26 LIVE + merged to main.** Antigravity built v26 (daily auto-run, self-learning, shelf life). Claude added a
  **Feedback button** (top bar -> `feedback` collection -> sos-inbox copies raw lines to `docs/dashboard-feedback.md` for
  Antigravity), fast-forwarded main, published to the same dashboard URL (artifact version 25). **Cloud routine created (user yes
  in chat 22 Nov):** "Social OS daily research (6 AM IST)", id `trig_01MUBE3T8MeXRUThWfz4XDbP`, cron `30 0 * * *` UTC, Sonnet 5.5,
  repos social-os + social-os-private, connectors Composio/Apify/Firecrawl. Runs without the PC; never posts. Test run started
  22 Nov (session `cse_013ppkXvUPU2ukheqhhQe7bd`): **check its log** (RemoteTrigger get_run_log) to confirm the cloud can reach
  ArtifactData; if not, it writes to `social-os-private/research/daily/`. Not in the cloud: ffmpeg/deepdive, Agent Reach, ElevenLabs key.

- **22 Nov 2026: Morning brief (user ask: phone-first, fast to scan).** Home top card reads `briefs/<date>` (sos-research step 7,
  routine step 4): max 3 picks with score / shelf-life / first-mover / one-line why + Pick/Skip; Expiring soon; Waiting for you;
  New this morning. Buttons: **Run research now** (opens the routine page via `schedules/daily-research.cloudTaskId`; the page
  cannot fire it itself) and **Discuss this brief** (Ask Claude gets the brief as context). Dashboard `schedules/daily-research`
  doc now links the cloud routine. Replaced the old auto-run strip + expiring banner. Checked at 390 px (Showcase), no errors.

- **22 Nov 2026 HANDOFF (user closed chat).** Done today: v26 live + main; Feedback button; daily cloud routine
  `trig_01MUBE3T8MeXRUThWfz4XDbP` (6 AM IST) TESTED OK (reads/writes dashboard DB, wrote 4 options + 3 scripts, push
  notification; Apify skipped = free credit used up; Reddit/HN APIs unreachable from cloud, front pages used; hook scores blank);
  Morning brief card with plain "What it is" + "Why now" lines (LESSONS 22 Nov); artifact icon = "planet" (claude.ai built-ins
  only, no custom image); PC shortcuts renamed "Social OS" with custom orb icon (`dashboard/icon/social-os.ico`).
  **Open / offered, not done:** (1) copy the 8 PC-only skills into the cloud (prompt-guy via its own repo as a routine source,
  others after licence check); (2) copy the user's working-style rules into the repo so cloud chats reply the same way;
  (3) "Connect" button with the Composio link on each account card; (4) dashboard link is "anyone with the link" (user's call
  in the Share menu); (5) Showcase mode keeps a stale account filter from localStorage (minor bug). Plan for Meta API / Porotta
  integration discussed and parked by the user. **Next:** user checks the Morning brief on phone, picks/skips the 3 picks.

- **22 Nov 2026 (user ask):** ig-ai-tools gets **pillar 6 "Marketing quick wins"** (25% of posts; goal = clients for Meta ads,
  SEO, web design/dev + position the user as a marketer). Simple tips, remakes of already-viral marketing reels, never complex.
  Rules in `private/accounts/ig-ai-tools/pillars.md`. Composio stays (Postiz cloud has no free plan; self-host needs a
  24/7 server + own platform apps). Saved Instagram posts: no API; only Meta's "Download your information" export.
  **Next:** competitors list needs 4-6 marketing creators (next research run; Apify credit used up until it resets).

- **23 Nov 2026: NEXT BUILD = Refresh button (user ask).** Growth section gets "Refresh": the page itself calls Composio
  (artifact `mcp` capability, load `artifact-capabilities` skill first) and pulls IG (`INSTAGRAM_GET_USER_INSIGHTS`,
  `INSTAGRAM_GET_IG_USER_MEDIA`, `INSTAGRAM_GET_IG_MEDIA_INSIGHTS`) + YouTube (`YOUTUBE_QUERY_ANALYTICS` ids `channel==MINE`,
  `YOUTUBE_LIST_CHANNEL_VIDEOS`, `YOUTUBE_GET_VIDEO_DETAILS_BATCH`) into `stats` + post `metrics` (docs/DATA.md), shows
  "Updated N min ago". Read-only. Test a tiny call from the page first; if blocked, fallback = button writes a `messages`
  doc kind `refresh` and the daily run / next chat pulls. Built in Claude Code (not Antigravity: it can't publish or test
  artifact capabilities). Tool list verified via Composio 22 Nov: both connections ACTIVE.

- **23 Nov 2026: v27 REFRESH BUTTON BUILT + PUBLISHED (artifact version 29).** Growth section has "Refresh numbers" + "Updated N min ago".
  The page calls Composio itself (`mcp` capability, server name "Composio", tool `COMPOSIO_MULTI_EXECUTE_TOOL`), read-only:
  IG followers + yesterday/today views + per-post insights; YouTube views per day (+ per video). Writes `stats/<acct>-<day>` (`pulledAt`)
  and post `metrics`. Shapes checked with real read calls 23 Nov. **YouTube limits (23 Nov):** Data API quota exceeded on Composio's side
  (channel stats + video list refused), so YT followers stay empty and only Analytics views come through. First press asks the user's OK for
  the Composio connector. **Not yet pressed by the user.** If a press fails, fallback = button writes a `messages` doc kind `refresh`.
  **Next:** user presses Refresh once on the dashboard (Home, Growth section); Claude then lists `stats` to confirm.

- **23 Nov 2026 (v28, user ask):** tapping a Morning brief pick opens a detail popup (what it is, why now, opening line, the idea, what to check first, Approve / Skip). Backfilled `hook`/`concept`/`needs` on today's 3 options; sos-research step 7 + docs/DATA.md now require them for the top 3.

- **23 Nov 2026 (v29, user ask):** Plan = ONE list "Ideas & scripts" (tap a card -> detail screen shared with the Home brief: idea, hook options with virality scores, beat-by-beat script with EN | Malayalam-English toggle, caption, fill-in chips, Approve / Ask changes / Teleprompter). Approving a script also sets its option to `picked`. The 5 draft scripts were rebuilt with ig-reel `hookscore` + `beats` (hook 75-100, scored by the heuristic, not a guarantee). sos-create step 2 now requires the structured format. Checked at 390 px (no sideways scroll, toggle works). **Next:** user opens Plan, taps an idea, reads/approves a script.

- **23 Nov 2026 (v30):** calendar side-panel buttons fixed (stopPropagation bug). **USER ASK, NEXT BUILD: full dashboard audit** (every button, every tab, overlays, phone + desktop). Plan + test recipe: `docs/plans/2026-11-23-dashboard-audit.md`. Also still unpressed by the user: Refresh numbers (v27).

- **23 Nov 2026: USER ASK, NEXT BUILD: Growth section upgrade** (more metrics: reach, interactions, profile visits, engagement breakdown, top posts, tile-switches-chart). Plan + verified Composio call shapes: `docs/plans/2026-11-23-growth-upgrade.md`. Dashboard audit plan: `docs/plans/2026-11-23-dashboard-audit.md`. Do Growth first, then the audit.

- **23 Nov 2026: v31 GROWTH UPGRADE BUILT.** 6 metric tiles (Followers, Views, Reach, Interactions, Profile visits, Posts); tap one and the chart switches to it (`ui.gmetric`). New: engagement breakdown bars, Top posts by views, best posting times, % vs last week. Refresh now pulls 7 days of IG/YT numbers into the new optional `stats` fields (docs/DATA.md; `growth_metrics` in results.py, 3 new tests pass). Checked in Playwright at 390 + 1200 px (all tiles tapped, no errors, no sideways scroll); real Composio call shape for daily follower gains re-verified (end_time date = that day). **Published (artifact version 33).** **Not yet pressed by the user on live data.** Next: dashboard audit (`docs/plans/2026-11-23-dashboard-audit.md`).

- **23 Nov 2026: v32 PUBLISHED (artifact version 34, user ask).** Every text box grows with its text (max 60% of screen); "Your angle" is now a box with no length limit; Radar URL box shows "N links found"; typed text is kept on the phone (auto-save on every key + when switching apps + a Save button), cleared after Add to Radar; Radar account = tick one or more accounts (`inspirations.accountIds`). Radar cards show the idea (`title` + new `concept`) instead of the raw URL; unread ones say "Not read yet". sos-radar + docs/DATA.md updated. Checked at 390 px in Playwright (no errors). **Next:** run sos-radar on the ~21 pasted reels so cards show their ideas (Apify credit may be used up; check first).

- **23 Nov 2026: USER ASKS, NEXT BUILD (nothing started; user's weekly limit near):** (1) fetch ALL the user's posted reels + numbers (Composio Instagram, free) and save them; keep saving every new post; give improvement advice from them. (2) Read the ~96 radar links in batches of 20-25 (rules in sos-radar "User's saved links": topic over views, merge same-topic duplicates, carousels = slides, old/low-view still OK). (3) Compare each radar idea with the user's own posts: flag "already posted" / clash, or suggest a fresh angle. (4) Tool reels: research better / newer / free / official alternatives so our version is more helpful. (5) Improve every time, but ASK the user before any big change (idea, tool, style). Radar reading needs the PC (deepdive + ElevenLabs/whisper); the cloud run can't watch video.

- **28 Nov 2026: BROAD-REACH LANE + APIFY SKIP FIXED (user yes in chat).** Found: the 28 Nov cloud run never tried Apify (it
  trusted the stale 2 Nov line). Routine prompt `trig_01MUBE3T8MeXRUThWfz4XDbP` rewritten: Apify allowed, caps $0.20/run
  ($0.30 Sunday), 4 keywords x 15 popular reels (`apify/instagram-search-scraper` `popular`, $0.0027/result), weekly scan of
  broad accounts, "would a non-tech person need this this week?" filter, "Claude can do this" frame. Keywords + idea bank:
  `private/accounts/ig-ai-tools/broad-keywords.md`. sos-research step 2 updated. **Not done, needs checking first:** the
  follower gate (Porotta `create_automation` follow check? Meta rules on comment-and-follow asks?). **Next:** read the
  29 Nov run log (RemoteTrigger get_run_log) to confirm Apify ran and what it cost.

- **28 Nov 2026: RADAR BATCH 1 of 4 DONE (reels 1-24 of the 96 saved links).** Method that works (free): yt-dlp (no cookie flag; plain `yt-dlp` works) -> video+caption; local Whisper small on ffmpeg-piped audio (faster-whisper's own decoder is broken with av 19, so audio goes in as a numpy array; ffmpeg is NOT on the bash PATH, add the WinGet Gyan folder); 3 Sonnet agents read ~8 reels each; 2 Sonnet agents verify real tool names/prices/licences + better alternatives; Claude scores (`score-radar`) and writes. Cards saved to dashboard `inspirations` (status scored/merged, `toolCheck` line), files in `private/research/radar/`. Script used: scratchpad build1.py/mkwrites.py (rebuild from this note if lost). **Next: batch 2 = reels 25-48** (sorted by createdAt), then 3, 4; ask the user the questions at the END of each batch only. Still pending from the 23 Nov asks: own-posts archive (Composio) + clash check against it (only the 22 old posts are known so far).

- **28 Nov 2026: REACH DESIGN BUILT (user yes; additive, nothing replaced).** Algorithm facts checked: top signals = watch time,
  likes per reach, sends per reach (trade press quoting Mosseri, Jan 2025; metrics confirmed in Meta API docs). Instagram said (Jun 2024,
  via Social Media Today, not on a live IG page) it won't recommend content that explicitly asks for shares/comments/tags and reels over 90 s
  -> NO spoken send-asks; send trigger is built into content. Built: `results.py` `signal_rates`/`scorecard` + CLI `scorecard` (heaters keep
  old shape + add `signalMultiples`; 3 new tests; 5 old deepdive tests fail only for lack of ffmpeg, same before my change), RULES.md "Reach design",
  sos-create step 2b (`scripts.reach` = sendTrigger/retentionDevice/saveReason), sos-results (reel-only watch-time call, scorecard), sos-research
  (likes/comments per view display), docs/DATA.md (`archive/{accountId}` doc, metrics `avgWatchSec`/`skipRate`). Dashboard **v33 (artifact version 35)**:
  "Reach signals" box under Growth + Refresh pulls watch time/skip in a separate reel-only call. Units verified with a real read: watch time = ms,
  skip rate = %. Own 50 posts archived (`private/accounts/ig-ai-tools/archive/`, db `archive/ig-ai-tools`) + `reach-baseline.md`: reels with skip rate under 50%
  reached ~14x more people (median 92.8K vs 6.5K at 60%+). **Not done:** keyword-comment CTA risk left as is (user's call); Approve/Plan screens do not show
  `scripts.reach` yet; the dashboard Refresh reel call is untested on a real press; reel length unknown so no watch %; **X trending is NOT fetched**
  (no X source in sos-research; free route unverified) and Apify popular-reels broad lane first runs 29 Nov 6 AM. Radar saved links (~96) still unread.

- **28 Nov 2026 (user answers after batch 1):** KEEP EVERYTHING; only prioritise by score, remove an idea only if there is truly no way to make it (unverified tool names get found first; overpromising claims get corrected honestly in our version; clashes with the user's own posts get a new angle). Questions go to the user once at the END of each batch. **Batch 2 (reels 25-48) is already downloaded + transcribed** (`private/research/radar/`, 34 transcripts in total; the rest are carousels/failed fetches to check). **Resume in a new chat with: "continue social os radar batch 2".** Steps: run the same pipeline on batch 2 (agents read, agents verify tools, score, save to `inspirations`), commit, then ask the end-of-batch questions.

- **28 Nov 2026 (later): ONE-RUN SYSTEM + SHOOT-TODAY PICK (user: "one run finds everything, prioritise, I'm fogged, find what is off").** Audit found: only 1 old waiting post (`w1-setup`, planned 7 Nov, stale), 8 draft scripts + 14 options unapproved, 3 rejected posts; the 28 Nov cloud run skipped Apify from a stale note and wrote "this week" for a GitHub issue opened 26 Oct. Fixed: routine prompt rewritten (one run: sources + broad lane + scored radar cards + clash check vs own `archive` + ONE ranked list + `Shoot today:` pick; never watches video, never touches radar cards a PC chat is working on), sos-research step 3b, LESSONS entry. **X trending = not worth building** (trends24.in: bare entertainment/politics hashtags, no context; X posts need a paid API). **Today's shoot: `scripts/d1128-skill-red-flags`** (3 skill red flags, hook 87, corrected facts, `reach` filled; user must Approve in Plan, then Teleprompter). Wi-Fi radar idea tested: this PC is on a phone hotspot (2.4 GHz ch 6, 238 ms), so it can't be filmed today and the "10x" claim stays unverified. Another PC chat owns radar batches 2-4 ("continue social os radar batch 2"). **Next:** read the 29 Nov 6 AM run log (did Apify run? does the brief start with `Shoot today:`?), then the dashboard should show `suggestedDay` and `scripts.reach` on Plan/Approve cards.

- **28 Nov 2026: RADAR BATCH 2 of 4 DONE (reels 25-48).** 24 cards scored + saved to `inspirations` (batch 2; Hallmark merged into MotionSites). Method as batch 1 (yt-dlp, Whisper on ffmpeg-piped audio, 3 read agents, 2 verify agents, `score-radar`). Cards/verify files in `private/research/radar/batch2-*.json`. Carousel `5vobic...` slides NOT read (yt-dlp can't fetch it); `13wuu...` Hindi reel topic unknown (needs a human watch); `8812z...` repo unnamed. Firecrawl credits ran out (agents used gh + WebSearch). outlierMultiple left at the 1.5 default (creator medians not fetched). **Resume with: "continue social os radar batch 3"** (reels 49-72, still `new`; download+transcribe first with the same steps).

- **28 Nov 2026: RADAR BATCH 3 of 4 DONE (reels 49-72).** 21 cards scored + saved to `inspirations` (batch 3; 59 merged into 60 LLM Council, 52 merged into 69 Agency Agents). 3 NOT done, still `new`: `whicbzqwka3ecct9z75k` (57), `8ys1ouh6vg0s1lorgp0q` (64) (download failed), `rpboek64d1cdgjrentju` (72, carousel, slides not read). Unreadable audio (need a human watch): 50, 52, 59, 67; thin: 53, 66. All old posts (26-30 days) set to `evergreen` (expiresAt null) so none expire; tiers P3/skip because outlier is the 1.5 default. Facts found: Kimi K3.1 Pro launched 23 Oct (not "last week"); Hallmark officially 22 themes (not 50); "Harvey" original repo not found, look-alike repos = malware risk; UPI zero-fee only small payments, self-hosted gateways unlicensed. Files `private/research/radar/batch3-*`; fetch script `batch3-fetch.py` (use `python -m yt_dlp` + full ffmpeg path). **Resume with: "continue social os radar batch 4"** (reels 73-96 + the 3 leftovers).

- **28 Nov 2026 HANDOFF (user closing this chat):** ranked list of ideas saved at `private/research/ranked-2026-11-28.md` (10 scored + 4 expired; radar batch 1 only). **No calendar placed.** The user will make or ask for the WEEK PLAN themselves AFTER all 4 radar batches are done (other chat: "continue social os radar batch 2"); they say which ideas + days, Claude then sets the slots. Today's film script is ready: `scripts/d1128-skill-red-flags` (Plan tab, user approves). Open items: read the 29 Nov 6 AM run log (Apify ran? brief starts with `Shoot today:`? the broad lane cost); show `suggestedDay` + `scripts.reach` on Plan/Approve cards; user presses Refresh numbers once (Growth); follower gate still unchecked (Porotta follow check, Meta rules); stale post `w1-setup` (planned 7 Nov) and 8 unapproved draft scripts left for the user.

- **28 Nov 2026: RADAR BATCH 4 of 4 DONE (21 of the last 27 saved links).** 21 cards scored + saved to `inspirations` (batch 4; `o72oq...` merged into `qkrnr...`, both GitHub design/animation libs). Top (all P3): Claude skill finder 47, 4 free Claude Code plugins 45, career-ops job hunter 43, Hypit 41, rest `skip` (old posts set `evergreen`, outlier default 1.5, so low = low priority only). **Network dropped mid-run**: re-ran the fetch script, which skips finished reels; the shell had no internet during verification, so repo stars/licences are WebSearch snapshots, marked unverified. NOT done, still `new`: `whicbzqwka3ecct9z75k`, `rpboek64d1cdgjrentju`, `2qwpa4szsm5x42568131`, `26vqnvu7veugyd90ficn`, `46jm7yp9kx251oswmx6a` (carousels: slides not readable by yt-dlp) and `cuzkliquv143yqr344je` (download failed). Needs a human watch: `p6a2e1`, `hmq1q3`, `ohy36e`, `tf28gk`. Facts found: Instinct's "talks at $10B" is stale (raised $1B at $10B 28 Sep 2026); Artemis is 99%+ on AndroidWorld only; MiroFish is AGPL and needs two keys; BuildPartner `/improve-system` not found anywhere (do not install). Files `private/research/radar/batch4-*`. **Radar is now batches 1-4 done**; next = the 6 leftovers, then the end-of-batch questions.

## 3. WHERE THINGS LIVE
- This folder: `C:\Projects\social-os` = github.com/gaznil/social-os (PUBLIC).
- `private\` = github.com/gaznil/social-os-private (PRIVATE), its own git repo, ignored by this one.
- Platform rules + which skills to use: `platforms/<platform>/README.md`.
- Pipeline stages: `engine/<stage>/README.md` (research, strategy, create, publish, analytics).
- Dashboard: `dashboard/` (artifact page source; its live data sits in the artifact database, not in git).
- Skill choices and rejected options with reasons: `SKILLS.md`. Licences of vendored skills: `THIRD_PARTY.md`.

## 4. RULES
- **Build mode (user, 31 Oct):** build every planned part end to end without waiting; the user uses it later and says what to improve. Never pause the build for their approvals or tests.
- **Approval gate:** nothing is published until the user approves that exact post (dashboard "Approve" or a yes in chat).
- **Public repo hygiene:** no account names, handles, voices, drafts, numbers, IDs or secrets in this repo. They go in `private/`.
  Secrets go nowhere in git: platform logins live in Composio, keys in git-ignored `.env` files only.
- **Voice files:** the vendored skills look for `~/.claude/<platform>/voice.md`. Use the active account's
  `private/accounts/<account-id>/voice.md` instead, every time.
- **One niche per account.** Never post the same content to two accounts on the same platform (spam rules = bans).
- **Never automate** likes, follows, mass comments or cold DMs. Instagram replies/DMs after a comment = Porotta, not this system.
- **Posting only through official APIs** (via Composio). No browser automation, no password sharing, no scraping behind logins.
- **Rulebook:** `RULES.md` = one rule per task; it beats any outside skill (audit: `docs/skill-audit.md`).
- **Own plugin:** `.claude-plugin/plugin.json` lists every `sos-*` skill (no copies; paths into `.claude/skills/`). A new
  `sos-*` skill must be added there; `tests/test_plugin.py` fails otherwise. Inside this repo the skills load as project
  skills, so the plugin is NOT installed here (installing = a Claude settings change = needs the user's yes).
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
