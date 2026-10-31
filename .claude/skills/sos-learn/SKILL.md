---
name: sos-learn
description: Social OS learning loop. Turn every user correction, failed step, wasted spend or found workaround into a lesson, and fix the skill that caused it, so the same mistake never happens twice. Run the moment it happens (same turn), and once at the end of each session.
---
Method copied from claude-reflect (BayramAnnakov, MIT), claude-reflect-system (haddock-development, MIT) and the
okteto lessons skill. No install, no review queue: lessons are applied at once and committed, so the user never has to run anything.

**When (signals):**
- HIGH: the user corrects or redirects ("use X", "not like this", "I didn't understand", "also do Y"), rejects a tool
  call, or names a skill/tool Claude should have used.
- MEDIUM: a step fails and a workaround works; something costs more time/credit than needed; the user approves an approach.
- LOW: a better option noticed but not proven.

**Do:**
1. Read `LESSONS.md`. If a lesson already covers it, sharpen that one (add `seen xN`); never add a duplicate.
2. Write one entry: date, signal, **Mistake** (specific), **Rule** (what to do instead, one or two lines), **Fixed in** (file).
3. HIGH and MEDIUM: also edit the skill or README that caused it (`sos-*` skill, platform README, `engine/*/README.md`)
   so the rule sits where the work happens. LOW: lesson only.
4. A lesson about how the user likes to work, true for every project -> also save it to Claude's global memory (feedback).
5. Commit + push (lesson + skill edit together).

**Never** change by lesson: the approval gate, zero-spend, public/private split, or anything in SAFETY. Those need the user's yes in chat.
At session end: scan this chat once for missed signals, then run steps 1-5.
