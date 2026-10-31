---
name: sos-results
description: Pull the numbers for every active Social OS account (followers, views, per-post results), write the daily `stats` docs that feed the dashboard's Growth section, update best posting times, and add ONE change per account to its lessons. Use on "results", "how are we doing", or in the scheduled results run.
---
**Skills rule:** at each step load the skills named here (and in the platform README) before doing the work. If another installed skill fits a step better, use it too and add it to `SKILLS.md`.
**Learning rule:** read `LESSONS.md` before starting (skip if already read this session). Any correction from the user, failed step, wasted spend or workaround found -> run `sos-learn` in that same turn (lesson + fix this skill + commit).
**Read-only rule:** this skill only reads platform numbers. It never posts, likes, follows or replies.

1. ArtifactData `list accounts`; keep `status == "active"` (or the one account asked for). None -> write the run line "No active accounts yet." and stop.
2. Per account, through its Composio connection (`COMPOSIO_SEARCH_TOOLS` for the read tool of that platform; never guess a tool name):
   - Instagram: account followers + each posted item's insights (views/plays, reach, likes, comments, saves, shares).
   - LinkedIn: follower count and post stats when the API gives them; a member profile often gets none -> `note` it once, don't retry daily.
   - YouTube / Facebook: channel or page followers + per-video/post views, when connected.
   - X / Threads: manual accounts, skip (no free API).
   A read that fails -> keep going with the others; put the reason in the run summary.
3. For each posted item: ArtifactData `update posts/<id>` `metrics` = `{views, reach, likes, comments, saves, shares, checkedAt}` (missing numbers = null, never 0).
4. ArtifactData `set stats/<accountId>-<YYYY-MM-DD>` (India date) = `{accountId, date, followers, views, posts}`: views = new views since the last stats doc, posts = items posted that day. One doc per account per day; a second run the same day overwrites it.
5. Save posts + stats to the scratchpad as JSON. `python -m tools.sos.cli best-times <posts.json>` -> per account top hours, or null (under 6 measured posts: keep the default windows). Not null -> `update accounts/<id>` `bestTimes` = that list; sos-create plans new slots into those hours.
6. Weekly (Mondays, or when asked): per account, compare this week's best and worst post (load `dataviz` only if a chart helps you see it). Write ONE change to try next week at the top of `private/accounts/<id>/lessons.md` (dated, one line, with the two posts' numbers as the reason). Never more than one change per week per account.
7. Monthly (first run of the month): load `llm-council` and ask it to check the month's numbers + the four weekly changes; save its verdict under `private/accounts/<id>/reviews/YYYY-MM.md` and carry its one top fix into lessons.md.
8. Trending audio (Instagram reels): suggest up to 3 in the run summary as names only. The user adds audio in the app; never attach it by API.
9. ArtifactData `set runs/results-<YYYYMMDD-HHMM>` with kind `analytics` and a one-sentence summary ("2 accounts measured; IG followers +31 this week; best hour 19:00"). Commit + push `private/`.
