1. `FACEBOOK_LIST_MANAGED_PAGES` -> the page id for this account (store it in the account folder; Pages only, never a profile).
2. Image: `FACEBOOK_CREATE_PHOTO_POST` (url + message). Several images: `FACEBOOK_CREATE_MULTI_PHOTO_POST` (photo_urls + message).
   Video/reel: `FACEBOOK_CREATE_VIDEO_POST` (file_url = direct MP4 link, description). Text only: search Composio for the Page feed-post tool.
3. Result `post_id` (PageID_PostID) = platformPostId. `FACEBOOK_GET_POST` -> permalink_url.
4. Graph errors 4, 17, 613 = rate limit: mark failed, never fast-retry.
