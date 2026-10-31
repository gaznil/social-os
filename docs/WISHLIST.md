# Wishlist — "if only my system could…" (30 Oct 2026)

Each item: the wish, the free way to get it, and what was checked. Status: ALL APPROVED by the user 31 Oct 2026 ("add all"). Each goes in the phase named; the phase plan file gets the detail.

| # | The wish | Solution | Checked | Fits phase |
|---|---|---|---|---|
| 1 | "Drafts that sound more like me every week" | When the user edits a draft before approving, diff draft vs final and fold the changes into that account's `voice.md` (build ourselves) | Our own design | 1 (with sos-create) |
| 2 | "Test a reel before my followers see it" | Instagram **trial reels** through the official API: `trial_params.graduation_strategy` = `SS_PERFORMANCE` (auto-shares to followers if it does well) or `MANUAL` | Meta docs, IG User Media reference. One developer forum report says API trial reels stopped reaching non-followers: test before relying on it | 4 |
| 3 | "Post when my followers are online" | Instagram `online_followers` insight (hourly, last 30 days) sets each account's posting windows automatically | Meta docs, Account Insights | 5 |
| 4 | "Turn one long video into many shorts" | Method from `Anil-matcha/AI-Youtube-Shorts-Generator` (5.6K stars, open-source Opus Clip alternative): transcript → highlight picking (Claude does this) → ffmpeg 9:16 crop → captions; built from `yt-shorts` + Edit King | Repo listing | 2 |
| 5 | "B-roll without filming it" | Pexels API: free, commercial use, no credit needed; Edit King / Motion King pull matching clips | pexels.com/api + licence page. Needs a free Pexels key (user signs up once) | 2 |
| 6 | "Tell me on my phone" | The Telegram bot that already exists (@porotta_gz_bot): "3 drafts waiting", "posted", "failed", "competitor reel went viral" | Bot + token already on this PC (Porotta notes) | 1 |
| 7 | "Never post a wrong AI-news claim" | `blog-factcheck` (installed) checks every claim in news posts against sources before the draft reaches the user | Skill installed | 1 (with sos-create) |
| 8 | "Know if the hook works before I film" | A viewer panel: 10 small Haiku personas built from the account's audience rate the hook and say where they would scroll away (idea from `Jakeschincariol/founder-skill`'s 100-buyer panel) | Uses Claude usage only, no money | 3 |
| 9 | "Get paid: brand deals" | Media kit built from real stats; find brands that sponsor creators in the niche (`lead-research-assistant`, Apify); pitch emails as Gmail **drafts** the user sends (`dm-outreach-writer`) | Skills + Gmail connector installed | 5 |
| 10 | "Reach both Malayalam and English audiences" | One idea → a Malayalam and an English version (`blog-translate`), for one account or a twin account | Skill installed | 3 |
| 11 | "Remind me to shoot" | Shoot days from the shot list go into Google Calendar | Calendar connector connected | 2 |
| 12 | "Which YouTube thumbnail wins?" | YouTube's own Test & Compare (up to 3 titles + thumbnails); the system prepares the 3 variants | YouTube Help; only "eligible creators" get it | 4 |
| 13 | "Never repeat myself by accident" | Topic memory: before drafting, check the account's last 60 days of posts and research for the same topic | Our own design | 1 (with sos-create) |

## Wanted but no free, safe way exists (checked or known)
- **Trending audio list for Reels:** no official API; scraping it needs logins. Skip.
- **Your own AI voice for faceless videos:** good voices are paid; local voices were rejected on 4 Oct 2026 ("worst").
- **Shadowban checker:** no reliable source; tools that claim it guess.
- **AI-generated video clips:** Higgsfield/Krea credits are near zero; revisit once there is income.

## User decisions 31 Oct 2026
- #4 shorts generator: NOT installed. It needs a MuAPI key or an OpenAI/Gemini key. We copy its method instead: local faster-whisper + Claude picks highlights + ffmpeg/OpenCV 9:16 crop. Free.
- #8 viewer panel: OK. Costs no money, only light Claude usage (Haiku).
- Music: use it unless it is 100% sure to hurt reach. The API cannot attach Instagram-library songs, so: trending audio found via Apify (reel/hashtag scrapers return the audio name, ~$0.0026/result) -> the draft is flagged "post from the Instagram app with sound X" (manual step). Otherwise royalty-free music baked into the video.
- Voice: ElevenLabs is connected (free plan: 10k credits/month, non-commercial + attribution). Use for faceless voiceovers, sparingly; paid plan only once there is income.
- AI video (Google Flow, kaze.ai: Seedance, Kling): the user generates these by hand. Use only when the user asks, or suggest it when it is clearly best and let the user decide. Prompt Guy writes the prompts.

## Round 2 additions (approved with the rest)
| # | Wish | Solution | Phase |
|---|---|---|---|
| 14 | Collab posts | Instagram API `collaborators` param on posts/reels (in Meta's media reference) + collab finder (Apify) + `ig-dm` pitch | 4 |
| 15 | See the grid before posting | Dashboard grid preview: next 9 covers in Instagram's 3:4 grid crop | 1 |
| 16 | Film faster | Teleprompter view of the approved script in the dashboard (phone) | 2 |
| 17 | Save inspiration from the phone | Inspiration inbox: paste any reel/video link -> deep-dive card (Apify by URL, Agent Reach for YouTube) | 3 |
| 18 | Old winners work again | Evergreen recycling: best posts older than 90 days come back as a new variant | 5 |
| 19 | Profile looks pro | Bio rewrite (`ig-profile`), story highlight covers, profile picture check | 1 |
| 20 | Trending sound | Flag above (manual sound add in the app) | 3 |

## Covers and formats (confirmed in the system)
Reel cover: designed 1080x1920 with the important part inside the centre 3:4 area (grid shows 3:4, 1080x1440); sent with the API `cover_url`. Carousels 1080x1440 (3:4) or 1080x1350. Stories 1080x1920. YouTube thumbnails 1280x720 (`yt-package` + render). LinkedIn carousels = PDF document posts (check Composio supports documents in Phase 4).
