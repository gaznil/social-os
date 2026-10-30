# Stage 3 — Create

Makes ideas and calendar slots into ready posts. Ideas come from three places: the user (dashboard Ideas tab, typed or
spoken with the phone keyboard mic), research cards ("make this"), and the weekly plan.

**Writing:** the platform skill (`ig-reel`, `ig-caption`, `yt-script`, `linkedin-post-writer`, `x-post`…), always
finished by the platform humanizer (`ig-human`, `linkedin-humanizer`, `x-human`; `content-humanizer` for Facebook/Threads).
**Graphics:** carousels/posters designed as HTML and rendered to PNG (1080x1350 for Instagram), `ig-carousel` for copy.

**Video studio (dashboard Studio tab):** the user drops a clip (small clips upload in the page; big ones go in the
Google Drive folder "Social OS inbox") and picks a tool:
| Tool | When |
|---|---|
| Edit King | the user's own footage: cut, captions, graphics, music, 16:9 → 9:16 |
| Motion King | a video made from nothing |
| Prompt Guy | just a paste-ready prompt for another video tool |
| faceless-explainer | a faceless account's explainer |
Each request is a `jobs` doc with the chosen model and effort. Video jobs run on the PC (ffmpeg, HyperFrames), so they
start when a Claude Code session is open; the result comes back to the Studio tab, then becomes a draft for approval.
Shot list for filming: grouped by setup changes, so one shoot covers several posts.

**Out:** a draft in the dashboard (text + media + account + planned time), status `waiting`.
Media files stay on the PC or Drive, never in git.
