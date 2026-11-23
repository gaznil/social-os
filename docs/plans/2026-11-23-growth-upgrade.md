# Growth section upgrade (user ask 23 Nov 2026)

Why: Growth shows only a followers line + 4 tiles (followers, views this week, posts this week, vs last week). User wants more.

## Design (decided, build in v31)
- **Metric tiles (tap one = chart switches to it):** Followers (+gained this week), Views, Reach, Interactions (likes+comments+shares+saves), Profile visits, Posts. Each with % vs the previous 7 days when that data exists.
- **One chart** for the selected metric, one line per account (generalise `growthBody` / `onGrowthMove`: they hard-code `followers`; make the field `ui.gmetric`).
- **Engagement breakdown** (this week): likes, comments, shares, saves as bars.
- **Top posts** (from `posts.metrics`, by views) + existing Heaters + best posting times (`accounts.bestTimes`).
- Showcase demo data must carry the new fields so Showcase looks full. Keep the Refresh bar (v27).
- Possible later (ask first): pull the account's last ~12 real posts + insights into a new collection so Top posts shows posts not made through Social OS.

## Data: new optional fields on `stats/{accountId}-{day}`
`reach`, `interactions`, `profileViews`, `accountsEngaged`, `likes`, `comments`, `shares`, `saves`, `followerGain` (net new followers that day). Add to docs/DATA.md, `tools/sos/results.py` growth maths + tests, sos-results skill step 4.

## Refresh button (extend `pullAccount` in dashboard/index.html; results come back in call order, so keep a `meta[i]` array instead of the slug counters)
Verified with real read calls on 23 Nov (Composio account ids are in the accounts docs):
- `INSTAGRAM_GET_USER_INFO` `{ig_user_id:"me", fields:"id,followers_count"}` -> `data.followers_count` (today's total).
- `INSTAGRAM_GET_USER_INSIGHTS` `{metric:["follower_count"], period:"day", metric_type:"time_series", since:"YYYY-MM-DD", until:"YYYY-MM-DD"}` -> `data.data[0].values[{end_time, value}]` = NET NEW followers per day (not the total). Backfill: followers(day d) = followersToday minus the sum of gains after d. Last day is partial.
- One call PER DAY (7 days back): `{metric:["views","reach","total_interactions","profile_views","accounts_engaged","likes","comments","shares","saves"], period:"day", metric_type:"total_value", since:<unix start of India day>, until:<min(start+86400, now)>}` -> `data.data[i].total_value.value` by `name`. (`views` has no time_series: total_value only.)
- Per posted post: `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` `{ig_media_id, metric:["views","reach","likes","comments","saved","shares"]}` -> `data.data[i].values[0].value` by `name`.
- YouTube: `YOUTUBE_QUERY_ANALYTICS` `{ids:"channel==MINE", startDate, endDate, metrics:"views,likes,comments,shares,subscribersGained,subscribersLost", dimensions:"day"}` -> `rows:[[day, ...]]`. YouTube Data API (channel stats, video list) hits Composio's shared quota ("quotaExceeded"), so YouTube followers stay empty; use gained minus lost as `followerGain`.
- Page calls Composio through the `mcp` capability: server name `Composio`, tool `COMPOSIO_MULTI_EXECUTE_TOOL`, args `{tools:[{tool_slug, account, arguments}], sync_response_to_workbench:false}`. A partly failed batch rejects `tool_error` with the envelope in `e.result` (already handled).

## Check before publishing
Playwright 390 px + 1200 px (recipe in `docs/plans/2026-11-23-dashboard-audit.md`), tap each tile, no sideways scroll; then the user presses Refresh once and Claude lists `stats` to confirm the new fields.
