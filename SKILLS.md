# Skill choices — compared, not guessed

Checked 30 Oct 2026 by opening each repo (file lists, SKILL.md size, scripts, tests, required keys). Stars are noted
but never decided anything alone. Re-check when a pack updates or a new contender appears.

## Picks

| Area | Pick | Why it won | Lost to it |
|---|---|---|---|
| Instagram | `Jakeschincariol/instagram-agent-skill` (MIT, 13 skills, ~3.7K stars) | 5 runnable Python tools with no dependencies (hook scorer, beat timer, caption linter, humanizer, swipe-file ranker); its own accuracy test is published; no keys | `sergebulaev/instagram-skills` (publishing tied to Publora, a paid scheduler); `social-media-skills/skills` (106 skills, prompt-only, thin per platform) |
| YouTube | `Jakeschincariol/youtube-agent-skill` (MIT, 11 skills, ~3.7K stars) | 6 runnable tools incl. retention-export reader, edit decision list, chapter validator; no keys | `eat-pray-ai/yutu` (good YouTube CLI/MCP, but needs our own Google OAuth app; Composio already does upload) |
| LinkedIn | `sergebulaev/linkedin-skills` (MIT, 12 skills, ~5.4K stars) | Deepest instructions (post writer 14 KB vs 4 KB), 11 test files, eval suite; works free in draft mode | `Jakeschincariol/linkedin-agent-skill` (li-post is a short prompt + hook list, no script) |
| X | `Jakeschincariol/x-agent-skill` (MIT, 11 skills, young: ~1 month) | Runnable tools: weighted character counter, hook scorer, public-embed reader; same voice format as IG/YT | `sergebulaev/x-skills` (prompt-only, publishing via Publora) |
| Trend research | `mvanhorn/last30days-skill` (~66K stars) | Free sources: Reddit, Hacker News, GitHub, YouTube (yt-dlp), arXiv; stores findings and runs watchlists | `Panniantong/Agent-Reach` (free channels overlap; Instagram/X need it to copy your Chrome logins = account risk); `ScrapeCreators/social-media-research-skills` (needs a paid key) |
| Strategy, copy, analytics | `coreyhaines31/marketingskills` (~57K stars) | Already installed globally: content-strategy, copywriting, analytics, ab-testing | `social-media-skills/skills`, `blacktwist/social-media-skills` (broader, shallower) |
| Publishing | Composio connector (already in Claude) | Free plan 100,000 actions/month, managed logins, several accounts per platform, Instagram/Facebook/YouTube/LinkedIn/X tools | Postiz (needs a server + own developer apps), Publora (15 posts/month free), PostLake/PublishQ/1Social (paid APIs) |
| Video | Motion King, Edit King, HyperFrames (already installed) | Local, free, already tuned to the user | `Jakeschincariol/video-production-skills` (same HyperFrames base, less tuned) |
| Instagram DMs/replies | Porotta (the user's own app) | Already live | — |

## Not found
- **Facebook** and **Threads**: no free, quality pack exists. Candidates found either post through browser automation
  (`Hao0321/claude-skill-social-post`, ban risk) or through paid publishers. Use the Instagram pack for writing and
  Composio for posting; revisit later.

## Round 2 (30 Oct 2026) — the ChatGPT-chat repos, opened and mined for ideas

Not installed whole; the useful parts are built into our own `sos-*` skills.

| Repo | What we take | What we leave and why |
|---|---|---|
| `w-avw/instagram-viral-reels-research-claude-skill` | The deep-dive method: two filters (views >= 5x followers, plus a niche view floor), a 6-frame contact sheet of each reel, Whisper transcript checked to start at 0.0 s, strip it to a formula with blanks, write our version | Its data path (Agent Reach + OpenCLI reusing your logged-in Chrome) |
| `thejmvai/claude-viral-radar` | Competitor library page: storyboard frames, transcript, hook analysis, ranked "plays you can copy", plus a "hot across the niche" tab | Its Instagram collection needs a logged-in browser session |
| `bendemartin97/claude-content-kit` | Per-account foundation files from an interview (`pillars.md`, `formats.md`), shot list grouped by setup changes, weekly review ending in exactly one change (`lessons.md`), recycling one shoot into second cut + story + carousel + quote card | Remotion: HyperFrames + Edit King already do this here |
| `Panniantong/Agent-Reach` | Install it, use only the no-login channels (web, YouTube, GitHub) | Instagram/X need it to copy a Chrome login; Instagram data comes from Apify instead (no login) |

## Research data sources
| Source | Gives | Cost |
|---|---|---|
| Apify `apify/instagram-reel-scraper` (official, no login) | Competitor reels: views, likes, comments, caption, video link | ~$0.0026/reel; free plan $5/month credit = ~1,900 reels |
| Apify `apify/instagram-scraper` | Profiles (follower counts for the 5x filter), posts, hashtags | ~$0.0027/result, same credit |
| `last30days` | Reddit, Hacker News, GitHub, YouTube trends | Free |
| Agent Reach | Web pages, YouTube subtitles, GitHub | Free |
| yt-dlp + ffmpeg + faster-whisper (local) | Frames + transcripts for the deep dive | Free (ffmpeg installed; yt-dlp + faster-whisper to install) |
| Skipped: `x-read`, `x-pulse` | X research through Grok | Needs a paid xAI key |

## Already installed, now part of the system
| Skill | Used for |
|---|---|
| `llm-council` | Big calls: picking a niche, a new format, a pivot (5 advisors argue it out) |
| `niche-content-strategist` | Choosing each new account's niche and pillars |
| `faceless-explainer` | Accounts where the user does not appear on camera |
| `edit-king`, `talking-head-recut`, `embedded-captions` | The user's own footage: cut, graphics, captions |
| `motion-king`, `music-to-video` | Videos made from nothing, beat-synced promos |
| `prompt-guy` | A paste-ready video prompt instead of a finished video |
| `competitive-ads-extractor` | What competitors run as paid ads (Meta ad library) |
| `blog-repurpose` | Best posts into gaznil.com blog articles |
| `content-humanizer` (in `~/.agents/skills`) | Second humanizer for Facebook/Threads text |
| `dataviz` | Dashboard charts |
| Porotta (own app, API) | After an Instagram post with "comment KEYWORD", auto-create the matching DM automation |

**Language note:** the humanizer scripts are tuned for English. For Malayalam posts the account's `voice.md` and the
user's review carry the weight.

## Installed where
Vendored into this repo's `.claude/skills/` so every session and every cloud run has the same versions.
Sources and commits: `THIRD_PARTY.md`.
