# LESSONS — Social OS learns from its mistakes

Written by the `sos-learn` skill. Read at every session start (sos-inbox step 0). Newest first. One lesson per entry;
repeats get `seen xN`, not a new entry. Rules here are already copied into the skill named in "Fixed in".

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
