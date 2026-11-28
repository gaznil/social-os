# LESSONS — Social OS learns from its mistakes

Written by the `sos-learn` skill. Read at every session start (sos-inbox step 0). Newest first. One lesson per entry;
repeats get `seen xN`, not a new entry. Rules here are already copied into the skill named in "Fixed in".

## 2026-11-15 · MEDIUM · Opinions on hooks/offers need evidence
- **Mistake:** recommended a hook and a prize split ("2 winners x 3 months") from judgment only; user: "dont just guess".
- **Rule:** when the user asks "what do you think" about a hook, score every option with `ig-reel/hookscore.py` and show
  the numbers; for offers/prizes, search for data first and say plainly when none was found. Also check the prize can
  be delivered (Claude gift subscriptions were unavailable on 15 Nov 2026).
- **Fixed in:** this lesson (sos-create reads LESSONS at start).

## 2026-11-12 · HIGH · Paid promo scripts: only true claims, one ask
- **Mistake:** rewrote a brand's promo reel script and kept "I'm going / follow along" from their draft, then swapped in
  "you'll see them here first", a new promise the user would not keep. User wasn't attending and posts nothing after.
- **Rule:** before rewriting a sponsor's script, ask or know the deal: what is posted (reel/story), collab tag or not,
  is the user attending, any follow-up posts. Cut every personal claim that isn't true (use "if I were there..."),
  never add promises of future content, ONE ask (the brand's). Keep every fact the brand gave. Caption starts with #ad.
- **Fixed in:** this lesson (sos-create reads LESSONS at start).

## 2026-10-31 · HIGH · Build the whole system; the user tests it later
- **Mistake:** ended a turn pointing the user at approvals instead of building on.
- **Rule:** the job is to build every planned part now, end to end. The user uses it and says what to improve. Never stop to ask them to test; keep building the next phase. Their own actions (approve, film, add accounts) are theirs, done whenever.
- **Fixed in:** `CLAUDE.md` rules.

## 2026-10-31 · HIGH · A test checks the plumbing; it never makes creative work
- **Mistake:** the Phase 3 dry run (a TEST job) started a full Prompt Guy run: read the 703 prompts and MOTION.md and wrote
  a whole reel prompt, built on the Cluely v2 prompt. User: "who said to give prompt now?" and "v2 is 0/100".
- **Rule:** dry runs use a one-line placeholder marked TEST. A real prompt (or any creative output) is made only when the
  user asks for that piece. Never build on a prompt with no score in prompt-guy `log.md`; it is unproven.
- **Fixed in:** `.claude/skills/sos-studio/SKILL.md` step 4; Phase 3 plan Task 4; prompt-guy `SKILL.md` (unscored = unproven);
  v2 score in prompt-guy `log.md` + MOTION.md "Learned".

## 2026-10-31 · MEDIUM · Where to find good carousels
- **Mistake:** scraped the 12 competitors for carousels (~$0.65): they post reels, their "carousels" were event photo dumps.
  Then hashtag search (~$0.22): the free Apify plan returns only the newest posts (0-7 likes), never the top ones.
- **Rule:** carousel references come from carousel-first accounts: the user's "Profiles I like" picks, or accounts whose
  last 12 posts are mostly Sidecar (check with `apidojo` cover-only data first, cheap) before paying for slides.
  Never use hashtag search for "best" posts on the free plan.
- **Fixed in:** `.claude/skills/sos-research/SKILL.md` step 2.

## 2026-10-31 · HIGH · Carousels must be real, not invented
- **Mistake:** "5 ChatGPT photo codes" carousel was rejected: weak in every way. Called them "codes" but each slide showed
  a 3-line prompt; no real result shown; the idea was a pattern copied loosely, not something we tested.
- **Rule:** a carousel promises exactly what each slide shows (a "code"/"command" = one short line you can type).
  Every tip must be tested by us, with a real example (real screenshot or real before/after output). No result we
  didn't produce. Design from real competitor carousels in `C:\Gaznil\social-os-media\carousel-library\`, not from scratch.
  If we can't show it working, it isn't a post.
- **Fixed in:** `.claude/skills/sos-create/SKILL.md` step 2 + 4; `.claude/skills/sos-research/SKILL.md` step 5.

## 2026-10-31 · HIGH · A system-wide rule goes into every stage
- **Mistake:** the learning loop was first wired only into research + inbox; user: "wire it to the system".
- **Rule:** when the user asks for a behaviour for "the system", add it to every `sos-*` skill and `SYSTEM.md`, not just
  the stage being worked on. Check with `grep -c <rule> .claude/skills/sos-*/SKILL.md`.
- **Fixed in:** all `sos-*` skills ("Learning rule"), `SYSTEM.md` "Learning loop".

## 2026-10-31 · HIGH · Search GitHub too when looking for a system to copy
- **Mistake:** looked for a self-learning repo with web search only; the user had to add "use the GitHub connector and search".
- **Rule:** when hunting for an existing repo/skill to copy, run web search AND the GitHub connector (`search_repositories`,
  sort by stars), open the top 2-3 files, and copy the best part of each.
- **Fixed in:** `CLAUDE.md` rule "Skills first".

## 2026-10-31 · HIGH · Use the platform research skills
- **Mistake:** competitors were picked by plain web/keyword search; the user had to point out `ig-viral`.
- **Rule:** research = load the platform's viral skill first (`ig-viral` / `yt-viral` / `x-viral` / `linkedin-hook-extractor`):
  its account mix (4 direct, 4 adjacent, 2-4 outsized, most within 10x the account's size) and its median-multiple ranking.
- **Fixed in:** `.claude/skills/sos-research/SKILL.md` steps 1 + 3.

## 2026-10-31 · HIGH · Ask in plain words, or decide
- **Mistake:** asked the user to approve a 5-row topic mix with percentages; user: "I didn't understand".
- **Rule:** strategy splits (pillars, percentages) are Claude's call, from the account's own numbers. Ask only one plain
  either/or, with a real example post, when the answer truly belongs to the user.
- **Fixed in:** `.claude/skills/sos-research/SKILL.md` step 1.

## 2026-10-31 · MEDIUM · Finding Instagram competitors
- **Mistake:** Apify keyword "user" search returned tiny accounts (<10K); profile "related accounts" come back empty when logged out.
- **Rule:** use `apify/instagram-search-scraper` with `searchType: "popular"` (trending reels per keyword, ~$0.0027 each),
  take the owners whose reels hit, then `apify/instagram-profile-scraper` on 10-12 of them for followers + last 12 posts.
- **Fixed in:** `.claude/skills/sos-research/SKILL.md` step 1.

## 2026-10-31 · MEDIUM · Big Apify results
- **Mistake:** dataset items with captions overflow the chat; direct curl of the dataset needs an API key.
- **Rule:** call `get-dataset-items` in batches of 2 with `fields`; when it saves to a file, parse the saved files with one
  Python script into `private/research/raw/`. Never `cat > file` before a heredoc (it waits for input and hangs).
- **Fixed in:** `.claude/skills/sos-research/SKILL.md` step 2.

- **22 Nov 2026 (user):** A topic name alone is useless ("Claude diagram skill"). Every brief pick and option carries a plain `what` line: what the thing IS and does, in everyday words a non-developer gets at once, so the user can choose or skip without looking it up. Fixed in sos-research steps 5+7, docs/DATA.md, dashboard brief + Plan cards.

- **23 Nov 2026 (user):** Scripts were one hard-to-read text block, hook never scored, and Plan showed ideas and scripts as two separate lists. Rule: a script is built with the real workflow (ig-reel/ig-carousel formulas, `hookscore.py`, `beats.py`, story format, voice, humanizer), stored structured, and shown readable in ONE detail screen; Plan has ONE list of ideas+scripts (tap to open). Home and Plan share the same detail screen (`openItemSheet`). Fixed in sos-create step 2, docs/DATA.md, dashboard v29.

- **23 Nov 2026 (user):** Calendar slot panel: no button worked, Close included. Cause: inline `onclick="event.stopPropagation()"` on the drawer stops the click before it reaches the page's one delegated click handler. Rule: never use stopPropagation / inline onclick in the dashboard; backdrops close through the delegated handler (`.drawer-bg` check). After any panel change, click its buttons in Playwright (remove `#intro` and the `intro-wait` class first). Fixed in dashboard v30.

- **28 Nov 2026 (found while building today's shoot):** the cloud run wrote "this week a user reported..." for a GitHub issue that was opened 26 Oct (a month earlier), taken from a news line without opening the issue's date. Rule: before any script says "this week / today / just launched", open the source and read its date; if older, say "got reported" without a time word. Also the same run skipped Apify from a stale note. Fixed in sos-research step 3b ("check every date and number on its live source") and the routine prompt.
