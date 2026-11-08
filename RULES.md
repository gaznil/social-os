# RULES.md - the Social OS rulebook

One rule per task. Where installed skills disagree, this file wins. Sources and conflicts: `docs/skill-audit.md`.
Outside skills are used for their **tools and methods** (hook lists, scorers, counters, linters), never to overrule a line here.
Order of authority: the user's words > `LESSONS.md` > this file > any skill.

## Always (every platform, every format)
1. **Never invent** a number, client, result or source. Unknown -> `{{your number}}` and flag it. Every tip shown working with a real example we produced (realism rule).
2. **One idea per post. One ask per post** (comment a keyword, save, follow, or reply - one).
3. **Hook = first line, story format = body.** Pick a hook formula from the platform's hook file and ONE story format from `private/knowledge/storytelling-formats.md` for any script.
4. **Number-first beats question-first.** An exact number with a referent in line 1 when we have one. Never a bare question as line 1 on LinkedIn.
5. **Zero em dashes**, straight quotes, no invisible characters. No slop words (ig-human `slop.json` list).
6. **Natural rhythm, never forced.** Don't alternate long/short sentences on purpose; at most 2 standalone fragments per post; no "The result?" / "Plot twist:" reveals; no "It's not X, it's Y".
7. **No sincerity frames** ("let me be honest", "real talk"). State the fact flat.
8. **No reflex bait:** "follow for more", "tag someone", "thoughts?", "agree?".
9. **Voice:** the account's `private/accounts/<id>/voice.md` + `style.md`, wherever a skill asks for `~/.claude/<platform>/voice.md`.
10. **Copy the shape, never the words** of a competitor post. Attribute every swipe row.

## Hooks (how many, how checked)
| Where | Write | Check | Keep |
|---|---|---|---|
| Reel / Short / story-script | 3 hooks, 3 different formulas (`ig-reel/hooks.json`) | `hookscore.py` | top one; under 50 = write 3 more |
| YouTube long | 5 hooks (`yt-script/hooks.json`) | `hookscore.py` | top 2 shown |
| X post / thread post 1 | 3 hooks (`x-post/hooks.json`) | `x-post/hookscore.py` | top one; under 50 = 3 more |
| LinkedIn | 2-3 formulas picked by goal (`linkedin-post-writer` F1-F20) | linkedin-humanizer audit | one |
| Carousel cover | 3 covers, max 6 words each | ig-reel `hookscore.py` | top one |

## Instagram
- **Reel:** 15-45 s. Hook spoken + on screen by frame 1, inside 3 s. Frame change every beat (max 4 s). No intro/greeting. Ends on one ask. Run `beats.py` clean.
- **On-screen text:** 6 words max per card; 1080x1920 safe zone y 230-1440, right 230 px clear. Burned-in captions on the body.
- **Carousel:** 6-10 slides, 1080x1350, type 32 px+, numbered (3/8), handle on every slide, 120 px clear margin, cover 6 words, a standalone recap slide (the one people send), no slide over 25 words. Copy approved before rendering.
- **Story:** 3-7 frames, face or hand on frame 1, ask on frame 4, text inside y 250-1600.
- **Caption:** Reel = Job A (ask + context + search words; no second hook). Carousel/photo = Job B (line 1 is the hook, cut at a cliff in the first 125 chars). 2-3 search phrases in plain sentences. **Hashtags: 3** (platform cap 5), specific, never #viral/#fyp. No links. Emoji max 4 per 100 chars. Alt text on the cover. Run `caption.py`.
- **Comment-keyword ask is allowed** (one word, caps, also said in the video) -> note it for a Porotta DM automation.
- **Mix (user decision 31 Oct):** ig-ai-tools = 2 reels + 2 carousels a week. Other accounts: 4 posts, at least 2 reels.

## YouTube
- **Long video:** first 15 s confirms the title, opens a question, proves the payoff. No channel intro, no early subscribe ask. `[ON SCREEN: ...]` on every beat. Runtime at 150 words/min. One ask at the close.
- **Shorts:** made-for-Short = Reel rules above. Cut from a long video = 20-55 s, opens on a complete thought, new first line, loop point (`yt-shorts`).
- **Title:** 10 written, `title.py`, under 60 chars (subject inside the first 40), max 2 all-caps words, a number/name/date.
- **Thumbnail:** max 3 words, never the title's words, same promise. Made from the best frame of the video (plan v2).
- **Description:** first 2 lines = what it gives, in searched words; link next; then chapters (`yt-chapters`). **Tags: up to 15**, spellings and tool names only.
- **Cadence:** 3 uploads a week max (1 anchor + 1 cheap + Shorts cut from the anchor). Phase 1 = Reels reposted as Shorts by the user.

## X
- 1-3 lines, 280 weighted chars (`count.py`). Long post only with Premium; everything that matters above the fold.
- Thread: 5-12 posts, every post stands alone, no "A thread 🧵", links last, recap post standalone.
- **Hashtags: 0** (1 at most). **Link:** in a reply under the post. Written for replies/quotes/sends, never rage.
- Cadence: 5-7 posts + 1-2 threads a week. Posting = copy + open X (no free API).

## LinkedIn
- Hook inside the first 210 chars. Line 1 a statement or number, never a question, never "Here's what/how", never "Stop X, start Y".
- Length 900-1,300 chars by default. 1-2 sentence paragraphs with blank lines. Close with a specific question; P.S. only when real.
- One contrast and one triple max. A real stake or dated fact in every post.
- **Hashtags: 0-2 at the end. Link:** first comment. **No comment-gate** ("comment X to get Y") - penalised since March 2026.
- Cadence 3-5 posts a week, never 6+. Tue-Thu best for B2B.

## Facebook / Threads
- Facebook = Instagram caption rules (Job B), link allowed in body. Threads = X post rules, 500 chars, 1 topic tag (Threads' own limit - unverified, check before first post).

## Posting time
The hour matters far less than the first line (every pack agrees). Defaults until `sos-results` writes the account's `bestTimes`: Instagram 19:00 audience time, LinkedIn Tue-Thu 07:30-09:00, X weekday 08:00-13:00, YouTube = the channel's own best day. After 4+ weeks of numbers, `bestTimes` wins.

## Research
- Rank by **outlier multiple** = views / that account's median of its last 10-15 posts. Above 3x = signal, under 1.5x = ignore.
- Account mix: 4 direct, 4 adjacent, 2-4 outsized (format only). Most within 10x of our size. "Profiles I like" always kept.
- State sample size. 40 posts across 6 accounts supports a claim; 12 does not.
- Apify (public, no login, low volume) stays our reader by design; never log in, never automate likes/follows/DMs.

## Engagement (comments, replies, DMs)
Drafts only, the user sends them. 1-3 sentences, the specific thing, no "Great post", no pitching. Instagram keyword DMs after a comment = Porotta, not Social OS.

## Humanizer pass (one order for all)
1. Platform script (`ig-human` / `x-human` `humanize.py`) for invisible chars, typography, slop words.
2. Rewrite flagged structural lines by hand (rules 6-8 above).
3. `detect.py` must reach PASS. If only BURSTINESS fails, merge or split real sentences; never add a long/short seesaw.
4. LinkedIn: `linkedin-humanizer` (forensic + strict tiers, Pass 4 self-check) instead of 1-3.
5. Show the cleaned text and the score, never the score alone.
