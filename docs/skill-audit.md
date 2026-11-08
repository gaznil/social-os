# Skill audit (plan v2, step 1) - 8 Nov 2026

What each installed skill says per task, where they clash, and the one rule Social OS uses (now in `RULES.md`).

## What was read
- **Read whole (creation rules):** ig-reel, ig-caption, ig-carousel, ig-story, ig-plan, ig-viral, ig-human, ig-repurpose;
  yt-script, yt-shorts, yt-package, yt-seo, yt-plan, yt-retention, yt-viral; x-post, x-thread, x-plan, x-viral, x-repurpose;
  linkedin-post-writer, linkedin-content-planner, linkedin-hook-extractor, linkedin-repurposer, linkedin-humanizer; sos-create.
- **Read for rules only (headings + rule lines):** ig-audit, ig-profile, ig-comment, ig-reply, ig-dm, x-audit, x-profile,
  x-human (same engine as ig-human), x-comment, x-reply, x-dm, yt-audit, yt-chapters, yt-edit, yt-comment,
  linkedin-interviewer, -comment-drafter, -reply-handler, -profile-optimizer, -engager-analytics, -thread-monitor,
  -employee-advocacy. These draft engagement or audit past posts; none sets a creation rule that clashes.
- **Not re-read:** last30days (research tool, no content rules; already tested 31 Oct), prompt-guy (video prompts only,
  its own rules stand), the long reference files the LinkedIn pack points to (`references/hook-formulas.md` etc. - not
  vendored, so the formula names are used, not their skeletons). Linked hook lists (`hooks.json`) are used as tools.

## Conflicts and the call made
| Task | What the skills say | Social OS rule | Why |
|---|---|---|---|
| Em dashes | ig/x-human: remove all. linkedin-humanizer V3: not a tell, cap ~1 per 100 words | **Zero everywhere** | Simplest; removing never hurts; one rule for all platforms |
| Sentence rhythm | ig/x-human `detect.py` scores BURSTINESS (variation good). linkedin-humanizer: forced long/short is the #1 2026 tell | **Natural, never forced**; BURSTINESS fail fixed with real sentences | LinkedIn V3 cites newer evidence; the IG score is a local heuristic |
| Hashtags | IG max 5 (platform cap since 18 Dec 2025); X 0-1; LinkedIn 0-2; YT tags 15 | IG 3, X 0, LI 0-2, YT 15 | Each platform's own limit; X says hashtags not needed |
| "Comment KEYWORD" ask | ig-caption: works (one word). linkedin-post-writer: comment-gate penalised (Mar 2026), refuses it | **IG yes, LinkedIn never**, X no | Different platform rules; IG side is wired to Porotta DMs |
| Question as line 1 | LinkedIn: never (-34% likes). IG/X hook lists include question hooks | **Never on LinkedIn**; allowed on IG/X only if it scores 50+ | Data is LinkedIn-only |
| Hooks per draft | ig-reel 3, x-post 3, yt-script 5 (keep 2), LinkedIn 2-3 formulas | Kept per platform (table in RULES.md) | Each scorer is built for its count |
| Short-video length | ig-reel 15-45 s; yt-shorts clips 20-55 s | 15-45 s made-for-short; 20-55 s when cut from a long video | Different jobs, both kept |
| Instagram cadence | ig-plan: 4-5 a week, at least 3 reels | **User decision: 2 reels + 2 carousels** (ig-ai-tools) | The user's choice beats a default |
| Weekly volume | YT 3 uploads; X 5-7 posts + 1-2 threads; LinkedIn 3-5 (6+ cannibalises) | Kept per platform | No overlap |
| Posting time | All packs: the hour matters less than the hook. IG early evening; LI Tue-Thu 7:30-9; X weekday morning | Those defaults until `sos-results` has `bestTimes` | Own numbers beat defaults |
| Research scraping | ig-viral / x-viral: read by hand, no scraping service | **Apify stays** (public, no login, low volume) | Recorded decision 31 Oct; ig-viral used for picking + ranking |
| Voice file | Every pack reads `~/.claude/<platform>/voice.md` | Account's `private/accounts/<id>/voice.md` | Several accounts per platform |
| Story structure | Packs give hook formulas only | Hook formula (line 1) + one Kallaway story format (body) | They do different jobs; both used |
| Engagement drafting | Packs draft comments/replies/DMs | Drafts only, user sends; IG keyword DMs = Porotta | System rule: never automate engagement |

## Where every pack agrees (taken as-is)
Never invent numbers; one idea per post; one ask; no intro/greeting in video; numbers beat adjectives; links never in an
Instagram caption; the recap slide/post must stand alone; copy the formula, never the words; outlier multiple (>3x)
over raw views; state the sample size; nothing is published by a writing skill.

## Gaps found (no skill covers them)
- Threads: no writing skill; uses x-post. Its tag/char rules are not verified yet (flagged in RULES.md).
- Facebook: no writing skill; uses ig-caption + copywriting.
- Carousel visual design: ig-carousel only sets sizes; the look comes from the carousel library (waiting on references).

## Next (plan v2)
Package `RULES.md` + the sos-* skills as our own `social-os` plugin; sos-* skills point at RULES.md for every rule and
call outside skills only for their scripts (hookscore, beats, caption, count, title, humanize, detect).
