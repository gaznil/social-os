---
name: sos-schedules
description: Sync the dashboard's Schedules screen with real Claude cloud scheduled tasks (create, pause, resume, remove). Run inside sos-inbox, or when the user adds a schedule.
---
**Learning rule:** read `LESSONS.md` before starting (skip if already read this session). Any correction from the user, failed step, wasted spend or workaround found -> run `sos-learn` in that same turn (lesson + fix this skill + commit).
1. ArtifactData `list schedules`. For each row by status:
   - `requested`: needs the user's yes **in chat** for that exact schedule (it runs on its own). On yes, load the `schedule` skill and create a recurring cloud task in an environment with repos `gaznil/social-os` + `gaznil/social-os-private`. Prompt by kind: research -> "Run sos-research for <accountId or every active account>. Then run sos-inbox."; publish -> "Run sos-publish. Then run sos-inbox."; results -> "Run sos-results for <accountId or all>." Time is India time (UTC+5:30); cloud tasks run at most once an hour. Then `update` the row: `status: "active"`, `cloudTaskId`, `note: null`.
   - `paused`: pause/disable that cloud task. `active` with a cloudTaskId that is paused: resume it.
   - `remove`: delete the cloud task (the user asked for it on the page; still confirm in chat once), then `delete` the row.
2. If cloud tasks can't reach ArtifactData or Composio (Task 6 test), write that in the row's `note` in plain words.
3. Never create a schedule the user did not add or approve.
4. Run `sos-learn` if a cloud task failed or the user changed a schedule.
