# Stage 1 — Research

Finds what is working now, per account niche. Never logs into anyone's account to collect data.

**Sources (all free tiers, see `SKILLS.md`):** Apify official Instagram scrapers (no login), `last30days`
(vendored; free keyless: Reddit, Hacker News, GitHub, Polymarket, YouTube), Agent Reach (web, YouTube, GitHub only), `yt-viral` / `x-viral`,
`firecrawl-search`, `competitive-ads-extractor` for paid ads.

**Agent Reach jobs (free, no login):** what's trending on YouTube for the niche (`youtube search`, view counts),
subtitles of top videos to study hooks and structure (`youtube subtitle`), what the audience asks and complains about
(`reddit search` / `reddit subreddit`), new AI tools and repos (`github search`), reading any link (`read <url>`).
Command: `C:\Users\gazni\.local\bin\agent-reach.exe` (not on PATH). Output is JSON.

**Competitor radar (daily, light):** for each account's `competitors.md`, pull new posts → rank by multiple over that
account's own median → keep outliers (>= 5x followers on views, or >= 3x the account median).

**Deep dive (on the top 3 outliers per week):** download the video (Apify link or yt-dlp), ffmpeg 6-frame contact
sheet, transcript via ElevenLabs Scribe v2 (local faster-whisper fallback; tool: `tools/sos/deepdive.py`), strip it to a formula with blanks, write our version
in the account's voice. One card per reel.

**Out:** `private/research/<date>-<account-id>.md`, and `research` docs in the dashboard (Research tab: frames,
transcript, formula, "make this" button that turns it into an idea).

**Runs:** radar daily as a cloud scheduled task; deep dive weekly, on the PC (needs ffmpeg + whisper).
