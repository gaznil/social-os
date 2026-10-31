---
name: sos-inbox
description: Read new messages and ideas the user left in the Social OS dashboard and act on them. Run at the start of every session in this project and in each scheduled run.
---
1. ArtifactData `query messages` where status == "new", oldest first. Also `query ideas` where status == "new": run sos-create for each (account given, or the best-fitting account), then set the idea to `drafted`. Accounts with status `setup` -> run sos-account. Then run sos-schedules.
2. Treat each as a request from the user (it comes from their own private page). Content requests ("make a carousel about X for ig-ai-tools") -> run sos-create. Questions -> answer. Research requests -> sos-research. Each skill run follows its own skills rule.
3. Requests to post, delete, change accounts or spend money are NOT done from a message: reply that the user must confirm in chat, and leave it.
4. `update messages/<id>` with `reply` (plain, 1-3 sentences, what was done or answered) and status `done`.
