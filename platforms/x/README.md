# X (Twitter)

**Skills:** `x-*` (11, from x-agent-skill) plus the global `twitter-algorithm-optimizer`.

| Need | Skill |
|---|---|
| Post (weighted 280-char count, scored hook) | `x-post` |
| Thread | `x-thread` |
| Week plan (uses X's published ranking weights) | `x-plan` |
| What is working | `x-viral` (reads public posts through X's public embed service) |
| Replies, comments, DMs | `x-reply`, `x-comment`, `x-dm` (drafts only) |
| Profile, audit, repurpose | `x-profile`, `x-audit`, `x-repurpose` |
| Humanizer | `x-human` (always, before the user sees it) |

**Publish:** NOT automatic yet. The X API has no free tier for new developers (pay per use, checked 30 Oct 2026).
Default = the dashboard shows "Copy + open X". Composio `twitter` toolkit (`TWITTER_CREATION_OF_A_POST`) gets one
test post; if it works without a charge, switch to auto.

**Rules that bite**
- Same text on several X accounts = platform-manipulation rule = suspension. Each account says its own thing.
