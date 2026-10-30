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

## Installed where
Vendored into this repo's `.claude/skills/` so every session and every cloud run has the same versions.
Sources and commits: `THIRD_PARTY.md`.
