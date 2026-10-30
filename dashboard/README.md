# Dashboard

A private Claude artifact page: the user's one screen, phone or PC. No domain, no server.

**Tabs:** Today · Accounts · Calendar · Approve · Analytics · Talk.

**How it works**
- Its own artifact database holds the live state: accounts list, calendar, drafts, approvals, results, messages.
  Claude Code reads and writes it; the page shows it live.
- **Talk:** quick answers from Claude right on the page (rewrite, more hooks). Bigger requests are saved as
  messages that Claude Code picks up in its next session or scheduled run.
- **Voice:** the phone keyboard's mic in any text box (artifact pages cannot use the microphone on this account).
- **Post now:** calls the Composio connector from the page, with the user's own login.

**Source:** the page file lives here (`dashboard/index.html`). Published with the Artifact tool; its URL is recorded
in `private/README.md` (not here, the URL is private).
