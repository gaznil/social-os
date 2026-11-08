# Social OS

A Claude-run content system for many social accounts across Instagram, YouTube, LinkedIn, X, Facebook and Threads:
research, plan, write, make, approve, post, measure, repeat.

- How it flows: [SYSTEM.md](SYSTEM.md)
- Which skills it uses and why: [SKILLS.md](SKILLS.md)
- Per platform: [platforms/](platforms/)
- Per stage: [engine/](engine/)
- The dashboard: [dashboard/](dashboard/)
- Rulebook: [RULES.md](RULES.md)

As a Claude Code plugin (the 9 `sos-*` skills; they need this repo's files, so use it inside a clone):

```
/plugin install social-os --marketplace gaznil/social-os
```

Built to run on free tiers only. Account data lives in a separate private repo and is never committed here.

Vendored skills keep their own MIT licences, see [THIRD_PARTY.md](THIRD_PARTY.md).
