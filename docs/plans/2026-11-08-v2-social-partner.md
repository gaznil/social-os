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
   carousel: images = Codex image_gen (plain, no text) OR real images via OpenMontage sources/APIs -> slides designed in HTML
   thumbnail: best real FRAME from the video first; no good frame -> Codex image_gen improves that frame (frame as
     reference); then designed (yt-package + banner-design). Never a fully generated poster.
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

## Dashboard lessons from the user's reference carousel (8 Nov, @tenfoldmarc "You need a content dashboard", 9 slides
saved in `C:\Gaznil\social-os-media\carousel-libraryrom-gaznil	enfoldmarc-content-dashboard\`)
Add to dashboard v24 (with the account switch):
1. **Overview** greeting line with counts ("3 reels queued, 2 hooks heating") + 3 stat tiles with sparklines.
2. **Hook Vault (missing today):** every strong hook from competitors/trends/our winners, turned into a template
   ("Stop doing [X]. Start doing [Y]."), tagged by type (swap/build/claim/list/contrarian) + how often it hit;
   searchable; "Use this" drops it into the script step.
3. **Analytics:** views, saves, follows, profile visits over 7/30/90 days; a "heater" = post that beat the account's
   30-day median by 2x, top 5 with a one-line "why it popped".
4. **Competitor tracker:** weekly auto run (top 5 reels per tracked creator, transcribed, hook + on-screen text pulled)
   with "Save to Hook Vault".
5. **Scheduler:** one post -> pick platforms -> date/time -> caption auto-made from hook + angle + CTA. (We post via
   Composio, not Zernio.)
6. **Content calendar:** month grid, each slot = time + platform + format + hook; click -> side panel with full script
   and caption; plus our "swap for my own content".
7. **What's trending:** daily feed from fixed sources (AI company blogs, X lists, GitHub trending, niche RSS), each item
   auto-tagged Hook / Explainer / Skip; top 5 first; morning digest.
Design of the carousel itself (cream, terracotta, serif-italic accent word, mono labels, page counter, corner marks,
"Comment GUIDE" last slide) = a carousel template to copy for our own carousels.
