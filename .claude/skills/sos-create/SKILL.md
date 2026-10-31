---
name: sos-create
description: Turn an idea, a need, a calendar slot or a video into ready drafts for one Social OS account, humanized and rule-checked, and put them in the dashboard for approval.
---
1. Read `platforms/<platform>/README.md` and load the writing skill it names (Instagram: ig-reel / ig-caption / ig-carousel / ig-story; LinkedIn: linkedin-post-writer; X: x-post / x-thread; YouTube: yt-script + yt-package). Use the account's `voice.md` and `style.md` wherever a skill asks for `~/.claude/<platform>/voice.md`.
2. Write the draft. Never invent numbers, clients or results; leave `{{your number}}` and say so.
3. Run the platform humanizer (ig-human / linkedin-humanizer / x-human) and apply its fixes.
4. Media: images rendered to PNG (1080x1350 for Instagram feed, 1080x1920 for stories) into `C:\Gaznil\social-os-media\<account-id>\`. Never put media in git.
5. Write the post JSON to the scratchpad and run `python -m tools.sos.cli check <file>`; put the result in `problems`. Fix and re-check until empty, or leave the problems for the user to see.
6. ArtifactData `set posts/<id>` with status `waiting`, `plannedAt` = next free posting window for that account (settings/main), all docs/DATA.md fields present.
7. Tell the user one line: what is waiting and where to approve it.
