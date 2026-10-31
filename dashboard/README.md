# Dashboard

A private Claude artifact page: the user's one screen, phone or PC. No domain, no server.

**Growth (v22):** under the Control room scroll; account buttons, followers line, 4 tiles, fed by `stats` (sos-results).

**Tabs:** Today · Ideas · Approve · Calendar · Studio · Research · Accounts · Talk.

**How it works**
- Its own artifact database holds the live state: accounts, ideas, posts, jobs, research cards, messages.
  Claude Code reads and writes it; the page shows it live.
- **Ideas:** type or speak (phone keyboard mic) an idea, pick the account or "any". Claude turns it into drafts.
- **Approve:** every format previews the way it will look: carousel slides, story frames (9:16), reel/video player,
  image, text posts and threads.
- **Studio (Prompt Guy first):** drop a clip (in-page upload up to 20 MB; bigger files via the Google Drive folder
  "Social OS inbox") + a brief. Prompt Guy writes the paste-ready prompt and it shows here with a Copy button.
  Prompt Guy only: no "Run it", Social OS never runs Edit King / Motion King (user rule 31 Oct).
- **Research:** competitor cards with frames, transcript, formula; "Make this" turns one into an idea.
- **Talk:** instant answers from Claude on the page, with pickers named like Claude's own: model Haiku 5.5 /
  Sonnet 5.5 / Opus 5.5 and effort Low / Medium / High. Bigger requests are saved as messages Claude Code picks up.
- **Accounts:** starts empty; every tab works with zero accounts.
- **Voice:** the phone keyboard's mic in any text box (artifact pages cannot use the microphone on this account).

**Model + effort, two meanings:** in Talk they set the instant answer on the page. On a Studio or Ideas job they are
saved with the job, and Claude Code runs that job with a helper on that model and effort.

**Source:** `dashboard/index.html`. Published with the Artifact tool; its URL is in `private/README.md`.
