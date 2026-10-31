1. Video must be a local file: stage it with Composio's file upload (s3key). A link is not enough.
2. `YOUTUBE_MULTIPART_UPLOAD_VIDEO` with title (post `title`), description (caption), tags (from `yt-seo`), categoryId
   (`YOUTUBE_LIST_VIDEO_CATEGORIES` once per account, store in the account folder), privacyStatus `public` -> video id.
3. Thumbnail in `mediaUrls[1]` -> `YOUTUBE_UPDATE_THUMBNAIL` (verified channel only; failure here = note, not a failed post).
4. permalink = `https://www.youtube.com/watch?v=<id>` (Shorts: `https://www.youtube.com/shorts/<id>`).
5. "quota exceeded" -> mark failed, stop all YouTube posts for 24 h. A video locked private -> stop and tell the user.
