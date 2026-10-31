---
name: sos-account
description: Add or update a Social OS account (private folder, dashboard record, Composio login, style learned from its past posts). Use when the user names a new account, changes one, or the dashboard has an accounts/<id> doc with status "setup".
---
**Skills rule:** at each step load the skills named here (and in the platform README) before doing the work. If another installed skill fits a step better, use it too and add it to `SKILLS.md`.
**Learning rule:** read `LESSONS.md` before starting (skip if already read this session). Any correction from the user, failed step, wasted spend or workaround found -> run `sos-learn` in that same turn (lesson + fix this skill + commit).

1. Account id = `<platform>-<short-niche>` in lowercase with dashes (e.g. `ig-ai-tools`). Ask only for what the user must decide: platform, niche, language, posts per week, on camera or not. No niche yet -> `niche-content-strategist` (big call: `llm-council`). Not on camera -> note it in `profile.md` so Prompt Guy writes faceless video prompts. If the dashboard already has `accounts/<id>` with status `setup`, read what it holds and ask only for what is missing.
2. Copy `private/accounts/_template/` to `private/accounts/<id>/`. Fill `profile.md`. Copy `voice-<platform>.md` to `voice.md` (Facebook uses the Instagram one, Threads the X one).
3. Style: if the account already has posts, learn from them. Ask for the profile link (or 3+ post links / pasted texts). Public profile reading needs a no-login route (Apify for Instagram, Agent Reach / web for YouTube, LinkedIn, X); never log in, never scrape behind a login. From the posts write `voice.md` (words, tone, hooks, emoji, length) and `style.md` (formats used, colours, fonts, cover style, what got the most reach). No posts yet -> interview with the 5 questions in the template (LinkedIn: `linkedin-interviewer`). Existing profile -> score it with `ig-profile` / `x-profile` / `yt-audit` / `linkedin-profile-optimizer` and show the user the top 3 fixes.
4. Composio: `COMPOSIO_SEARCH_TOOLS` for the platform, then `COMPOSIO_MANAGE_CONNECTIONS` action `add`, alias = account id. Give the user the link as a markdown link. After they say done, `list` and confirm ACTIVE. Store the id from `list` as `composioAccountId`. The user may connect later: then save the account with status `setup` and say so in one line.
5. ArtifactData `set accounts/<id>` with the docs/DATA.md fields (`label` = a name with no handle). Status `active` only when Composio is ACTIVE (or the platform is manual: X, Threads).
6. Commit + push `private/`. Never write handles or IDs into the public repo.
7. Run `sos-learn` if anything was corrected or failed.
