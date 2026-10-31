# YouTube

**Skills:** `yt-*` (11, from youtube-agent-skill).

| Need | Skill |
|---|---|
| Script with scored hook | `yt-script` |
| Title + thumbnail as one pairing | `yt-package` |
| Edit list from a transcript | `yt-edit` (then Prompt Guy writes the edit prompt) |
| Shorts hidden in a long video | `yt-shorts` |
| Description, tags, search queries | `yt-seo` |
| Chapters | `yt-chapters` |
| Week plan | `yt-plan` |
| What is working in the niche | `yt-viral` |
| Where viewers leave | `yt-retention` (needs the user's retention CSV export) |
| Comments | `yt-comment` |
| Whole-channel check | `yt-audit` |

**Publish:** Composio `youtube` toolkit — `YOUTUBE_MULTIPART_UPLOAD_VIDEO` (file must be staged, not a URL),
then `YOUTUBE_UPDATE_THUMBNAIL`. **Numbers:** `YOUTUBE_GET_VIDEO_DETAILS_BATCH`.

**Rules that bite**
- Daily upload quota is limited; a "quota exceeded" error only clears after ~24 h.
- Custom thumbnails need a verified channel (phone verification, free).
- Unaudited API uploads are no longer locked private (Google, 13 Oct 2026). If one locks, stop and tell the user.
