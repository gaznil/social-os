# Stage 4 — Approve + publish

**Approve:** the user taps Approve / Edit / Reject in the dashboard. Only `approved` items move on.

**Publish:** through the Composio connector (free plan, 100,000 actions/month), several accounts per platform.
- "Post now" button in the dashboard, or
- a cloud scheduled task (max once an hour) that posts every approved item whose time has come.
- X and Threads: "Copy + open app" until a free route is proven (see their platform READMEs).

**Out:** post ID + link written back to the item; status `posted` or `failed` with the reason in plain words.
**Never:** retry fast on Instagram errors (back off), or post anything not approved.
