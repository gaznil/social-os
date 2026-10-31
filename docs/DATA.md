# Social OS data shape

The dashboard and every `sos-*` skill read and write exactly these fields.


- `accounts/{accountId}`: `platform`, `label` (shown in the dashboard, no handle needed), `niche`, `language`, `postsPerWeek` (number), `composioAccountId` (string or null), `status` (`setup` = added from the dashboard, Claude still has to make its private folder + Composio link | `active` | `paused`), `updatedAt` (ISO). Adding from the dashboard also writes a `messages` doc asking Claude to set it up.
- `posts/{postId}`: `accountId`, `platform`, `format` (`text`|`image`|`carousel`|`story`|`reel`|`video`|`short`|`thread`), `title` (YouTube only, else `""`), `caption`, `mediaUrls` (array of strings), `plannedAt` (ISO), `status` (see queue), `approvedBy` (`dashboard`|`chat`|null), `approvedAt` (ISO|null), `postedAt` (ISO|null), `platformPostId` (string|null), `permalink` (string|null), `error` (string|null), `problems` (array of strings from preflight), `updatedAt` (ISO).
- `messages/{messageId}`: `from` (`user`|`claude`), `text`, `status` (`new`|`done`), `reply` (string|null), `createdAt` (ISO).
- `ideas/{ideaId}`: `text`, `accountId` (string|null = any account), `source` (`user`|`research`|`plan`), `status` (`new`|`drafted`|`dropped`), `createdAt` (ISO).
- `jobs/{jobId}` (Phase 2; listed now so names stay stable): `tool` (`prompt-guy` = the only video tool|`sos-create`), `accountId` (string|null), `brief`, `inputs` (array of asset URLs or Drive links), `prompt` (string|null: Prompt Guy's output), `parentJobId` (string|null: unused, kept so names stay stable), `model` (`haiku`|`sonnet`|`opus`), `effort` (`low`|`medium`|`high`), `status` (`new`|`working`|`done`|`failed`), `output` (array of links), `note` (string|null), `createdAt`.
- `schedules/{scheduleId}`: `accountId` (string|null = all accounts), `kind` (`research`|`publish`|`results`), `every` (`daily`|`weekly` = Mondays), `time` (`HH:MM` India time), `status` (`requested` = added in the page, Claude must create the cloud job | `active` | `paused` | `remove` = Claude deletes the cloud job, then the row), `cloudTaskId` (string|null, set by Claude), `note` (string|null, set by Claude), `createdAt`, `updatedAt`.
- `competitors/{autoId}`: profiles the user liked. `link` (profile URL or @handle), `platform`, `accountId` (string|null = best fit), `note` (string|null; user writes why they like it, Claude overwrites with what it learned), `source` "user", `status` (`new` = Claude adds it at the next research run | `tracked` | `remove`), `createdAt`.
- `runs/{runId}`: `kind` (`publish`|`inbox`|`research`|`analytics`), `startedAt`, `finishedAt`, `summary` (one plain sentence).
- `settings/main`: `timezone` (`Asia/Kolkata`), `postingWindows` (array, default `["09:00","13:00","19:00"]`).

