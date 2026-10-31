# Stage 3 — Create

Makes ideas and calendar slots into ready posts. Ideas come from three places: the user (dashboard Ideas tab, typed or
spoken with the phone keyboard mic), research cards ("make this"), and the weekly plan.

**Writing:** the platform skill (`ig-reel`, `ig-caption`, `yt-script`, `linkedin-post-writer`, `x-post`…), always
finished by the platform humanizer (`ig-human`, `linkedin-humanizer`, `x-human`; `content-humanizer` for Facebook/Threads).
**Graphics:** carousels/posters designed as HTML and rendered to PNG (1080x1350 for Instagram), `ig-carousel` for copy.

**Video studio (dashboard Studio tab, skill `sos-studio`) — Prompt Guy ONLY (user rule 31 Oct):** the user gives a
brief and/or a clip (a public link, or a file name in `C:\Gaznil\social-os-media\inbox\`) and taps "Get prompt" or
"Prompt + all-platform pack". That writes a `jobs` doc (docs/DATA.md). The next Claude run reads the clip with `deepdive`,
writes the paste-ready prompt with `prompt-guy` and shows it in Studio with a Copy button. It never runs Edit King, Motion
King or any video tool; the user takes the prompt wherever they want. A pack also drafts one post per active account
(`pack-plan`: Instagram carousel, LinkedIn/Threads/Facebook/YouTube text, X thread), each waiting in Approve.
Shot list for filming: grouped by setup changes, so one shoot covers several posts.

**Out:** a draft in the dashboard (text + media + account + planned time), status `waiting`.
Media files stay on the PC or Drive, never in git.
