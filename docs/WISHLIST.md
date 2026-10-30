# Wishlist — "if only my system could…" (30 Oct 2026)

Each item: the wish, the free way to get it, and what was checked. Status: PROPOSED until the user says yes; then it
moves into a phase in `docs/plans/`.

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
