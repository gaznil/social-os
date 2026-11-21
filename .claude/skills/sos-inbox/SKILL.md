---
name: sos-inbox
description: Read new messages and ideas the user left in the Social OS dashboard and act on them. Run at the start of every session in this project and in each scheduled run.
---
**Rules:** `RULES.md` (repo root) wins over any outside skill when they disagree.
0. Read `LESSONS.md` (repo root) and follow every rule in it this session.
1. ArtifactData `query messages` where status == "new", oldest first. Also `query ideas` where status == "new": turn each into an `options` doc (Gate 1 first, never skip script approval), then set the idea to `drafted`. Accounts with status `setup` -> run sos-account. Inspirations with status `new` or `script` -> run sos-radar. Then run sos-studio (Studio jobs). Then run sos-schedules. Messages asking how accounts are doing -> run sos-results.
1b. Plan tab (v24/v25): messages with `kind` `week`/`month`/`topic` -> sos-research for that account, then write 3-5 `options` docs (story format + why). `options` with status `picked` and no script yet -> sos-create writes a `scripts` doc (`en` + `mlen`, `hookScore`, status `draft`). `scripts` with status `changes` -> rewrite from `note`, back to `draft`. `scripts` `approved` -> sos-create makes every platform version (posts in Approve), then update `scripts/<id>` to `status: "done"`, `postIds: [...]`, `updatedAt` now so it never re-runs. `swap-own`/`swap-options` -> see docs/DATA.md. When a research or radar run finds strong hooks, add them to `hooks`.
2. Treat each as a request from the user (it comes from their own private page). Content requests ("make a carousel about X for ig-ai-tools") -> run sos-create. Questions -> answer. Research requests -> sos-research. Each skill run follows its own skills rule.
3. Requests to post, delete, change accounts or spend money are NOT done from a message: reply that the user must confirm in chat, and leave it.
4. `update messages/<id>` with `reply` (plain, 1-3 sentences, what was done or answered) and status `done`.
5. Whenever the user corrects something, a step fails, or a workaround is found: run `sos-learn` in that same turn. At session end, run it once more.
