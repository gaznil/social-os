# Social OS data shape

The dashboard and every `sos-*` skill read and write exactly these fields.


- `accounts/{accountId}`: `platform`, `label` (shown in the dashboard, no handle needed), `niche`, `language`, `postsPerWeek` (number), `composioAccountId` (string or null), `status` (`active`|`paused`), `updatedAt` (ISO).
- `posts/{postId}`: `accountId`, `platform`, `format` (`text`|`image`|`carousel`|`story`|`reel`|`video`|`short`|`thread`), `title` (YouTube only, else `""`), `caption`, `mediaUrls` (array of strings), `plannedAt` (ISO), `status` (see queue), `approvedBy` (`dashboard`|`chat`|null), `approvedAt` (ISO|null), `postedAt` (ISO|null), `platformPostId` (string|null), `permalink` (string|null), `error` (string|null), `problems` (array of strings from preflight), `updatedAt` (ISO).
- `messages/{messageId}`: `from` (`user`|`claude`), `text`, `status` (`new`|`done`), `reply` (string|null), `createdAt` (ISO).
- `ideas/{ideaId}`: `text`, `accountId` (string|null = any account), `source` (`user`|`research`|`plan`), `status` (`new`|`drafted`|`dropped`), `createdAt` (ISO).
- `jobs/{jobId}` (Phase 2; listed now so names stay stable): `tool` (`prompt-guy` = DEFAULT|`edit-king`|`motion-king`|`faceless-explainer`|`sos-create`), `accountId` (string|null), `brief`, `inputs` (array of asset URLs or Drive links), `prompt` (string|null: Prompt Guy's output), `parentJobId` (string|null: the Prompt Guy job a "Run it" job came from), `model` (`haiku`|`sonnet`|`opus`), `effort` (`low`|`medium`|`high`), `status` (`new`|`working`|`done`|`failed`), `output` (array of links), `note` (string|null), `createdAt`.
- `runs/{runId}`: `kind` (`publish`|`inbox`|`research`|`analytics`), `startedAt`, `finishedAt`, `summary` (one plain sentence).
- `settings/main`: `timezone` (`Asia/Kolkata`), `postingWindows` (array, default `["09:00","13:00","19:00"]`).

