# How the system works

One loop, run for every account. Each stage has its own README in `engine/`.

```
 research ──> strategy ──> create ──> APPROVE ──> publish ──> analytics
    ^                                   (user)                   │
    └───────────────────── lessons feed the next plan ───────────┘
```

| Stage | Does | Reads | Writes |
|---|---|---|---|
| research | Finds what is working now in each account's niche | niche + competitor list | trend notes, swipe file |
| strategy | Turns research into a weekly plan per account | trends, past results, voice | calendar slots |
| create | Writes scripts, captions, carousels, video | calendar slot, voice, platform skill | drafts + media |
| approve | The user says yes, edits, or rejects | drafts | approved queue |
| publish | Posts approved items at their time | approved queue | post IDs, links |
| analytics | Pulls numbers, names what worked and what to change | post IDs | weekly report, lessons |

## Who does what
- **Claude Code** (this repo) runs every stage. Cloud scheduled tasks run research, publish and analytics on a timer,
  so the PC can be off.
- **The dashboard** (a private Claude artifact page) is the user's screen: see the plan, approve drafts, read results,
  talk to Claude, leave requests. It keeps its own database that Claude reads and writes.
- **The user** approves, films, and does anything physical (logging in once per account).

## Accounts
Each account is a folder in `private/accounts/<account-id>/`: `profile.md` (platform, handle, niche, goal, cadence),
`voice.md` (how it sounds), `competitors.md`. Adding an account = copy `_template`, fill it, connect it in Composio.

## Data
- Public repo (this): the system only. No account data.
- Private repo (`private/`): accounts, voices, drafts, calendar, analytics history.
- Dashboard database: live working state (queue, approvals, messages). Claude mirrors anything durable into `private/`.
- Secrets: never in git. Platform logins stay inside Composio.
