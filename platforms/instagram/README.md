# Instagram

**Skills:** `ig-*` (13, from instagram-agent-skill). Always run `ig-human` on every caption/script before it reaches the user.

| Need | Skill |
|---|---|
| Reel script + hook score + beat timing | `ig-reel` |
| Caption (feed-preview check, 5-hashtag cap) | `ig-caption` |
| Carousel (1080x1350) | `ig-carousel` |
| Stories | `ig-story` |
| Week plan | `ig-plan` |
| What is working in the niche | `ig-viral` (reads public posts at human speed, never scrapes logged in) |
| Profile score | `ig-profile` |
| Post-mortem | `ig-audit` |
| Turn one long piece into many | `ig-repurpose` |
| Comments, replies, DMs | `ig-comment`, `ig-reply`, `ig-dm` (drafts only; live auto-replies = Porotta) |

**Publish:** Composio `instagram` toolkit — create container (`INSTAGRAM_POST_IG_USER_MEDIA`), then publish
(`INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`). Carousels: `INSTAGRAM_CREATE_CAROUSEL_CONTAINER`.
**Numbers:** `INSTAGRAM_GET_IG_MEDIA_INSIGHTS`.

**Rules that bite**
- Account must be Creator or Business (free switch in the Instagram app).
- 100 API posts per account per 24 h. Wait between create and publish; fast retries trigger "too many actions".
- Media must be a clean URL with no `?query`, or a Composio-staged file.
- Max 5 hashtags (Instagram rule since 18 Dec 2025).
