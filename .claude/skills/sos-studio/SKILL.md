---
name: sos-studio
description: Turn a Studio request from the Social OS dashboard (a brief and/or a clip) into a paste-ready Prompt Guy video prompt, and for "pack" requests also draft one post per connected platform. Run from sos-inbox and in scheduled runs.
---
**Skills rule:** at each step load the skills named here (and in the platform README) before doing the work. If another installed skill fits a step better, use it too and add it to `SKILLS.md`.
**Learning rule:** read `LESSONS.md` before starting (skip if already read this session). Any correction from the user, failed step, wasted spend or workaround found -> run `sos-learn` in that same turn (lesson + fix this skill + commit).
**Video rule (user, 31 Oct):** video = Prompt Guy ONLY. This skill writes the prompt and stops. It never runs Edit King, Motion King, faceless-explainer, HyperFrames or any other video tool.

1. ArtifactData `query jobs` where status == "requested", oldest first. For each: `update` status `working`, `updatedAt` now.
2. Save the job to the scratchpad as JSON and run `python -m tools.sos.cli studio-check <job.json>`. Problems -> `update` status `failed`, `note` = the problems in one line; next job.
3. Clip (`clipUrl` set): get a local file into `C:\Gaznil\social-os-media\studio\<jobId>\` (never git).
   A file name = `C:\Gaznil\social-os-media\inbox\<name>`. A direct video link = use it as is. A post page (YouTube,
   Instagram, etc.) = `yt-dlp -o <folder>\video.mp4 <link>`; public Instagram reel that yt-dlp can't fetch ->
   `apify/instagram-scraper` with `directUrls` for its `videoUrl` (free credit, one post). Then
   `python -m tools.sos.deepdive <file> --out <folder>` for frames + timestamped transcript (read `frames.jpg` and `transcript.json`).
4. Test jobs (id starts `test-`) never run Prompt Guy: `update` `prompt` = "TEST - placeholder, no prompt written" and go to step 6.
   Real jobs (made by the user in Studio): load `prompt-guy`. Write ONE paste-ready prompt from the brief + transcript/frames + the account's
   `private/accounts/<accountId>/voice.md`, `style.md` and `formats.md` (on camera? language? length?). Realism rule
   (LESSONS 31 Oct): only claims we can show working. `model` set on the job -> do this step in a subagent on that model.
   `update` `prompt` = the prompt text (plain, no code fences).
5. Kind `pack`: ArtifactData `list accounts`, save to the scratchpad, run `python -m tools.sos.cli pack-plan <job.json> <accounts.json>`.
   For each target run `sos-create` (format from the plan, its own rewrite per account, never the same text twice on one
   platform, status `waiting`). Collect the post ids into `postIds`. Empty plan -> `note` "No other active accounts yet."
6. `update` status `done`, `note` = one plain line (what is ready, where), `updatedAt` now. A step that fails -> status
   `failed` with the reason in `note`, and run `sos-learn`.
7. Tell the user one line: the prompt is in Studio (Copy button), pack drafts are in Approve.
