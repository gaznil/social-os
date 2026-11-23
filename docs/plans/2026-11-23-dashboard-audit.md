# Dashboard audit (user ask 23 Nov 2026)

Why: the calendar side panel had NO working button (inline `onclick="event.stopPropagation()"` blocked the one delegated click handler). User: "maybe somewhere else also will have issues like this, audit and fix everything."

## Method (do in this order, fix as you go, one commit per group)
1. **Static sweep** of `dashboard/index.html`: grep `onclick=`, `stopPropagation`, `preventDefault` on click, `pointer-events`, `z-index` (overlays: `.sheet-bg`, `.drawer-bg`, `.voice`, `.tele`, `.intro`), early `return`s in the delegated click handler (`document.addEventListener("click"`), `!db` guards, buttons with `data-*` that no branch handles (list every `data-xxx` attribute, then check a handler exists), handlers with no matching button.
2. **Click-through test** (Playwright MCP, 390 px phone and 1200 px desktop, Showcase mode): visit every tab (Home, Plan x3 sub-tabs, Approve, Calendar, Studio, Accounts), click EVERY button/link/chip, and record: did something visibly change, any `pageerror`/`unhandledrejection`, any sideways scroll, any overlay that cannot be closed (Close, backdrop, Escape).
3. **Live-mode test:** stub `window.claude.use("db")` with an in-memory fake (via `page.addInitScript`) so the `!db` guards pass and the write paths run; check each write goes to the right doc and the UI updates.
4. **Report** what was broken / fixed / left (with the reason) in plain words; log lessons (`sos-learn`); update this file.

## Test recipe (works, used 23 Nov)
- Build a test copy: take `dashboard/index.html`, insert `window.__t={state,ui,openItemSheet};` before the LAST `</script>`, save in the scratchpad.
- `page.route('https://sos.test/', r => r.fulfill({path, contentType:'text/html'}))`, `goto('https://sos.test/')`, wait 2.5 s.
- Then `document.getElementById('intro')?.remove(); document.body.classList.remove('intro-wait')` (the welcome animation blocks clicks).
- Playwright code cannot `require('fs')`: serve JSON through more `page.route` entries and `fetch` it in the page.

## Open items from before
- **Refresh numbers button** (v27) not yet pressed by the user on the real dashboard. After the press: `ArtifactData list stats` must show docs with `pulledAt`.
- Home brief detail popup (v28) and Plan one-list + detail screen (v29) were checked only in a phone-sized preview, not tapped by the user yet.
