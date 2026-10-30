# LinkedIn

**Skills:** `linkedin-*` (12, from linkedin-skills). Run `linkedin-humanizer` on every post before the user sees it.

| Need | Skill |
|---|---|
| Post | `linkedin-post-writer` |
| Hooks from what already worked | `linkedin-hook-extractor` |
| Week plan | `linkedin-content-planner` |
| Interview the user to find stories | `linkedin-interviewer` |
| Turn one piece into posts | `linkedin-repurposer` |
| Comments on others / replies on ours | `linkedin-comment-drafter`, `linkedin-reply-handler` |
| Profile | `linkedin-profile-optimizer` |
| Who engages | `linkedin-engager-analytics`, `linkedin-thread-monitor` (need a free Apify token, optional) |

The pack can auto-post through Publora. We don't use that: Publora keys stay empty and posting goes through Composio.

**Publish:** Composio `linkedin` toolkit (already connected) — `LINKEDIN_CREATE_LINKED_IN_POST`; images via
`LINKEDIN_INITIALIZE_IMAGE_UPLOAD` first.

**Rules that bite**
- One personal profile per person. Extra "accounts" must be company pages the user admins.
- Personal-post numbers are probably not available through the API: plan for the user to paste them, or a screenshot.
