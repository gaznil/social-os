---
name: sos-publish
description: Post every approved, due Social OS post through Composio and write results back to the dashboard. Use on "publish", in the scheduled publisher run, or when the user approves something for now.
---
1. ArtifactData `query posts` where status == "approved". Save them as JSON in the scratchpad.
2. `python -m tools.sos.cli due <file>` -> the list to post now. `check` again; any problem -> status `failed`, `error` = the problems, skip it.
3. For each: set status `posting` first (so a second run can't double-post), then follow `platforms/<platform>/PUBLISH.md` with the account's Composio connection.
4. Success -> status `posted`, `platformPostId`, `permalink`, `postedAt`. Failure -> status `failed`, `error` = one plain sentence + the platform's error code.
5. ArtifactData `set runs/<publish-YYYYMMDD-HHMM>` with a one-sentence summary ("Posted 2, 1 failed: Instagram quota").
6. Never post a doc whose status is not `approved`. Never touch X or Threads (manual: copy + open app).
