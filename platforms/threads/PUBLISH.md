1. `THREADS_GET_PUBLISHING_LIMITS` -> stop if the post quota is used up.
2. `THREADS_CREATE_POST` with media_type: text/thread = `TEXT` (text <= 500 bytes; a longer piece goes in `text_attachment`),
   image = `IMAGE` + image_url, video = `VIDEO` + video_url, 2-20 images = `CAROUSEL` + carousel_items. Public URLs only.
   A `thread` format: first part with `THREADS_CREATE_POST`, each next part with `THREADS_CREATE_REPLY` (reply_source `owned`).
3. Never use `THREADS_CREATE_AND_SHARE_POST` (it also posts an Instagram story the user did not approve).
4. Returned id = platformPostId; `THREADS_GET_POST` -> permalink. Numbers: `THREADS_GET_POST_INSIGHTS`.
