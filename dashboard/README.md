# Dashboard

A private Claude artifact page: the user's one screen, phone or PC. No domain, no server.

**Tabs:** Today · Ideas · Approve · Calendar · Studio · Research · Accounts · Talk.

**How it works**
- Its own artifact database holds the live state: accounts, ideas, posts, jobs, research cards, messages.
  Claude Code reads and writes it; the page shows it live.
- **Ideas:** type or speak (phone keyboard mic) an idea, pick the account or "any". Claude turns it into drafts.
- **Studio:** drop a clip (in-page upload up to 20 MB; bigger files via the Google Drive folder "Social OS inbox"),
  pick Edit King / Motion King / Prompt Guy / faceless explainer, write the brief, pick model + effort. Results show here.
- **Research:** competitor cards with frames, transcript, formula; "Make this" turns one into an idea.
- **Talk:** instant answers from Claude on the page, with a picker: model (Fast = Haiku, Balanced = Sonnet,
  Best = Opus) and effort (low / medium / high). Bigger requests are saved as messages Claude Code picks up.
- **Voice:** the phone keyboard's mic in any text box (artifact pages cannot use the microphone on this account).

**Model + effort, two meanings:** in Talk they set the instant answer on the page. On a Studio or Ideas job they are
saved with the job, and Claude Code runs that job with a helper on that model and effort.

**Source:** `dashboard/index.html`. Published with the Artifact tool; its URL is in `private/README.md`.
