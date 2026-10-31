1. `LINKEDIN_GET_MY_INFO` -> author id (cache it in the account doc as `authorUrn` after the first run).
2. With an image: `LINKEDIN_INITIALIZE_IMAGE_UPLOAD` (top-level `owner` = author), PUT the bytes to the upload URL (201 with empty body = success).
3. `LINKEDIN_CREATE_LINKED_IN_POST` with author + commentary (+ image). Save the returned id.
4. `LINKEDIN_GET_POST_CONTENT` to read it back; a 403 here is NOT a failure if step 3 returned an id.
