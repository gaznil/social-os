# Stage 1 — Research

Finds what is working now, per account niche.

**Skills:** `last30days` (Reddit, Hacker News, GitHub, YouTube, arXiv — all free), the platform `*-viral` skills
(`ig-viral`, `yt-viral`, `x-viral`), `firecrawl-search` for the open web. Optional: Apify free monthly credit.

**In:** `private/accounts/<id>/profile.md` (niche) and `competitors.md`.
**Out:** `private/research/<date>-<account-id>.md` — top topics with source links, outliers ranked by
"multiple over the account's own median" (not raw views), hook formulas seen.

**Runs:** daily, as a cloud scheduled task. Never logs into anyone's account to collect data.
