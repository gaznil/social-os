---
name: sos-create
description: Turn an idea, a need, a calendar slot or a video into ready drafts for one Social OS account, humanized and rule-checked, and put them in the dashboard for approval.
---
**Skills rule:** at each step load the skills named here (and in the platform README) before doing the work. If another installed skill fits a step better, use it too and add it to `SKILLS.md`.

1. Read `platforms/<platform>/README.md` and load the writing skill it names (Instagram: ig-reel / ig-caption / ig-carousel / ig-story; LinkedIn: linkedin-post-writer; X: x-post / x-thread + twitter-algorithm-optimizer; YouTube: yt-script + yt-package + yt-seo + yt-chapters; Shorts: yt-shorts; Facebook: ig-caption / ig-repurpose + copywriting; Threads: x-post). One long piece into many: ig-repurpose / linkedin-repurposer / x-repurpose. Weak idea or hook -> `copywriting`. Use the account's `voice.md` and `style.md` wherever a skill asks for `~/.claude/<platform>/voice.md`.
2. Write the draft. Never invent numbers, clients or results; leave `{{your number}}` and say so.
3. Run the platform humanizer (ig-human / linkedin-humanizer / x-human; Facebook/Threads also `content-humanizer`) and apply its fixes.
4. Media: carousels/posters designed as HTML with `frontend-design` + the account's `style.md` (`canvas-design` / `banner-design` for single graphics), images rendered to PNG (1080x1350 for Instagram feed, 1080x1920 for stories) into `C:\Gaznil\social-os-media\<account-id>\`. Never put media in git. Video: `prompt-guy` writes the prompt first (user decision); on "Run it" -> `edit-king` (the user's footage), `motion-king` (from nothing), `faceless-explainer` (faceless accounts), `embedded-captions` for captions. Post asks people to comment a keyword -> note it so Porotta gets the matching DM automation.
5. Write the post JSON to the scratchpad and run `python -m tools.sos.cli check <file>`; put the result in `problems`. Fix and re-check until empty, or leave the problems for the user to see.
6. ArtifactData `set posts/<id>` with status `waiting`, `plannedAt` = next free posting window for that account (settings/main), all docs/DATA.md fields present.
7. Tell the user one line: what is waiting and where to approve it.
