# Social OS v2 - "social partner" (plan, 8 Nov 2026)

Status: WAITING FOR USER YES on this plan. Nothing built yet.

## The flow (one account at a time)

```
 [Account switch at the top of the dashboard] -> everything below works for that account only
        |
 START: three doors
   A. "Plan my week/month"     B. "One video about X / this repo"     C. "Here is my video"
        |                              |                                     |
        v                              v                                     |
 RESEARCH (always 4 sources)  ------------------------------                 |
   competitors (ig-viral/yt-viral/x-viral)                                   |
   X trends (x-pulse - free route to test first)                             |
   GitHub trends (agent-reach / firecrawl)                                   |
   Profiles I like (user's references, always included)                      |
   + topic/repo deep read for door B (firecrawl-deep-research, youtube transcripts)
        |                                                                    |
        v                                                                    |
 OPTIONS: 3-5 titles/concepts, each with its story format + why             |
        |  user picks one (or swaps a slot for own content)                  |
        v                                                                    |
 SCRIPT: written with one of the 10 story formats (Kallaway PDF)             |
   two versions with a toggle: English | Malayalam-English mix             |
        |  USER APPROVES SCRIPT  (gate 1)                                    |
        v                                                                    v
 PRODUCTION                                                       Prompt Guy edit prompt
   reel/short: film it, or Prompt Guy prompt; b-roll list (OpenMontage free sources)
   carousel: images from Codex image_gen (plain images, no text) -> slides designed in HTML
   thumbnail: Codex plain image -> designed thumbnail (yt-package + banner-design), never a generated poster
   all-platform versions: IG reel+carousel+caption, YT short+title+thumbnail, LinkedIn, X, Threads, FB
        |  USER APPROVES FINAL POSTS (gate 2, one tap each)
        v
 PUBLISH (Composio)  ->  RESULTS (sos-results)  ->  lessons feed the next research
```

Plan view (door A): week + month calendar; every slot has "Use my own content" (swap), "New options", "Remove".

## Build order (each part works alone)
1. **Skill audit + own rulebook** (biggest, first; see below).
2. **Dashboard v24:** account switch on top; Options screen; Script screen with EN | ML-EN toggle + Approve script;
   month calendar with swap; thumbnail + carousel previews.
3. **Research v2:** 4 sources every run (competitors, X trends, GitHub trends, Profiles I like) + topic/repo deep read.
4. **Writing v2:** options -> script in a story format, both languages.
5. **Production:** Codex image_gen for plain images; carousel + thumbnail designed on top; OpenMontage for b-roll
   sources (Archive.org, NASA, Wikimedia free; Pexels/Pixabay/Unsplash free keys) - install + test first.
6. **Versions for every platform** after script approval (existing pack-plan reused).

## Skill audit (step 1)
- Read every skill the system touches, fully: 57 vendored (~48K words) + ~25 global ones used (prompt-guy, humanizers,
  design, research). Each skill read whole, not skimmed.
- Output: `docs/skill-audit.md` = for every task (hook, caption length, hashtags, posting time, carousel slides, CTA,
  script length...) what each skill says, where they conflict, and the ONE rule Social OS uses (with source).
- Then build our own plugin `social-os`: one rulebook (`RULES.md`) + the sos-* skills rewritten to call outside skills
  only for their tools/methods, never for conflicting rules. Outside skills stay installed, untouched.

## Not decided / to check before building
- x-pulse X trends free? (test once). OpenMontage licence AGPL - fine for own use, never copied into the public repo.
- Codex image_gen uses the user's ChatGPT plan limits (no API key).
