1. `INSTAGRAM_GET_USER_INFO` -> ig_user_id. `INSTAGRAM_GET_IG_USER_CONTENT_PUBLISHING_LIMIT` -> stop if quota is used up (result list is under response.data.data).
2. Image: `INSTAGRAM_POST_IG_USER_MEDIA` (image_url without `?`, or image_file staged) + caption -> container id.
   Carousel: one container per image, then `INSTAGRAM_CREATE_CAROUSEL_CONTAINER`. Reel: media_type REELS + video.
   Story (1-7 frames in `mediaUrls`): create and publish one `STORIES` container per frame in order (wait 30 s per frame before `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH`).
3. Wait 30 s (video: poll the container until FINISHED), then `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` with creation_id.
4. On error 9007 wait 60 s and publish again once. On error 9 ("too many actions") stop and mark failed: never fast-retry.
5. `INSTAGRAM_GET_IG_MEDIA` -> permalink.
