---
name: sos-learn
description: Social OS self-learning engine. Learns system rules from mistakes/corrections AND continuously learns the user's speaking style, Manglish mix, banned phrases, winning hooks, and content preferences from their videos, caption edits, script change requests, rejections, and analytics heaters — writing visible cards to the dashboard's "What Claude learned" section.
---
**Rules:** `RULES.md` (repo root) wins over any outside skill when they disagree.
Method copied from claude-reflect (BayramAnnakov, MIT), claude-reflect-system (haddock-development, MIT) and the okteto lessons skill. Lessons are applied at once and surfaced in the dashboard's **"What Claude learned"** section (where the user can inspect or delete any wrong learning with one tap).

### Part A — Content & Voice Self-Learning (Dashboard `learnings` + `accounts.voiceProfile`)

Run whenever any of these 5 signals appears (in `sos-inbox`, `sos-account`, `sos-research`, `sos-radar`, `sos-create`, `sos-results`):
1. **User's own videos & transcripts (`tools/sos/deepdive.py`):** extract opening phrases, pace (words/sec), Malayalam-to-English ratio, recurring transition words, energy, and camera framing.
2. **Inline caption/title edits (`posts.editedFrom` != `posts.caption`):** diff `editedFrom` vs `caption` to see words deleted, shortened sentences, hashtag changes, or tone shifts -> clear `editedFrom: null` after recording the learning.
3. **Script "Ask changes" (`scripts.note`) & Post "Back to draft" (`posts.feedbackNote`):** turn the user's feedback note into a permanent voice/style rule so they never have to give the same note twice.
4. **Approvals, Drops & Rejections (`options`/`ideas` `dropped`, `posts` `rejected`, `inspirations` `skipped`):** note which topics, hooks, or formats the user consistently skips vs picks first.
5. **Post performance (`sos-results` + `python -m tools.sos.cli heaters <posts.json>`):** record which hook types, story formats, lengths, and IST posting hours beat `>= 2x` median views.

**How to save a Content/Voice learning:**
- Update `private/accounts/<accountId>/voice.md` and `style.md`.
- ArtifactData `set learnings/<learningId>` with `{accountId, category: "voice"|"edits"|"hooks"|"topics"|"timing", text: "<1 clear rule>", source: "<e.g. Video #14 transcript | Caption edit on post X | 4.2x Heater>", createdAt}`.
- ArtifactData `update accounts/<accountId>` `voiceProfile` = `{tone, manglishMix, commonPhrases: [...], bannedWords: [...], winningFormats: [...], updatedAt}`.
- Before writing any script or caption, query `learnings` for that `accountId`: if a learning doc was deleted by the user in the dashboard (Remove button), remove that rule from `voice.md`/`style.md` too.

### Part B — Engine & Skill Self-Learning (`LESSONS.md`)

**When (signals):**
- HIGH: the user corrects or redirects ("use X", "not like this", "also do Y"), rejects a tool call, or names a skill/tool Claude should have used.
- MEDIUM: a step fails and a workaround works; something costs more time/credit than needed; the user approves an approach.
- LOW: a better option noticed but not proven.

**Do:**
1. Read `LESSONS.md`. If a lesson already covers it, sharpen that one (add `seen xN`); never add a duplicate.
2. Write one entry: date, signal, **Mistake** (specific), **Rule** (what to do instead, one or two lines), **Fixed in** (file).
3. HIGH and MEDIUM: also edit the skill or README that caused it (`sos-*` skill, platform README, `engine/*/README.md`) so the rule sits where the work happens. LOW: lesson only.
4. A lesson about how the user likes to work, true for every project -> also save it to Claude's global memory (feedback).
5. Commit + push (lesson + skill edit together).

**Never** change by lesson: the approval gate, zero-spend, public/private split, or anything in SAFETY. Those need the user's yes in chat.
At session end: scan this chat once for missed signals, then run Parts A and B.
