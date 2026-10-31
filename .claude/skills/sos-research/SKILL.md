---
name: sos-research
description: Find what is viral and trending in one Social OS account's niche (competitors, top reels/carousels/posts, audience questions), learn from it, and turn the best into ideas and calendar drafts for approval. Use on "research", "find trending ideas", a scheduled research run, or right after a new account is set up.
---
Read `engine/research/README.md` first. Never log in anywhere; public data only.

1. **Foundation (first run per account):** if `private/accounts/<id>/pillars.md` or `formats.md` is missing, write them from `profile.md`, `style.md` and 5 short questions to the user (3-5 content pillars; which formats this account makes). If `competitors.md` is empty, find 5-10 public accounts in the niche (search the platform via the sources below) and write them in.
2. **Collect (cheap first):**
   - Instagram: Apify actor `apidojo/instagram-scraper` (about $0.50 per 1,000 posts on the free plan; fallback `apify/instagram-scraper`, $2.70 per 1,000). Last 30 days, max 20 posts per competitor. Before each run estimate the results; the free plan is $5 a month and stops when used up, never charges. Over $1 in one run -> ask first.
   - YouTube / Reddit / GitHub / web: Agent Reach (`C:\Users\gazni\.local\bin\agent-reach.exe`), `last30days`, `yt-viral`, `x-viral`, firecrawl search.
3. **Rank:** outliers = views or likes >= 3x that competitor's median, or >= 5x its follower count on views. Note format (reel, carousel, story, text), hook (first line / first 2 s), length, posting day/time, audio name if shown.
4. **Deep dive (top 3, weekly, PC only):** `python -m tools.sos.deepdive <video file or direct link> --out private/research/deepdive/<date>-<id>-<n> --source <post link>` -> frames.jpg (6-frame sheet), transcript.json, card.md. Transcript = ElevenLabs Scribe v2 (key in the Windows user variable `ELEVENLABS_API_KEY`; free plan ~12 min/month, shared with voiceovers), falls back to local faster-whisper by itself. Fill the card's Hook, Formula (with blanks) and Our version. Load `ig-viral` / `yt-viral` / `linkedin-hook-extractor` for the platform.
5. **Write:** `private/research/<date>-<id>.md` (sources with links + numbers). For each strong pattern, ArtifactData `ideas` doc: `source: "research"`, `accountId`, `text` = the idea in the account's voice + "Why: <outlier link, its number>". Never copy a post; make our own version.
6. **Calendar:** if the account's next 14 days have fewer posts than `postsPerWeek`, run sos-create on the best ideas to fill the gaps (status `waiting` = needs the user's Approve).
7. ArtifactData `set runs/research-<YYYYMMDD-HHMM>` with one sentence ("ig-x: 6 ideas, 3 drafts waiting; top outlier 12x"). Commit + push `private/`.
