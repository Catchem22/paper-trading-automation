# Trading Automation - Discord Thread Project Note

Created: 2026-05-21 00:05 CDT
Source: Discord thread `Trading Automation`
Related: [[Project Index]], [[Automation Log]], [[Hermes Agent Operating Notes]]

## Objective

Build a safe, paper-only swing-trading automation workflow that can use a brokerage paper API, propose/manage trades with strict risk controls, and report outcomes back to Discord with minimal manual intervention.

## Current status

- Paper-trading automation is active through Hermes cron as **Alpaca paper swing-trading multi-agent pipeline**.
- The pipeline is configured as **paper only** and delivers reports back to the originating Discord thread.
- The cron schedule was changed from once daily to **4 weekday runs per day**.
- The Hermes dashboard now has an **Automations** page so scheduled jobs can be seen and managed visually.

## Operational references

Scheduler and dashboard identifiers are intentionally excluded from this repository. Use the authorized operations environment to view or manage the current paper-trading schedule.

## Decisions

- Start with **paper trading only**, not live trading.
- Do not grant or use unrestricted brokerage permissions.
- Prefer a phased setup:
  1. Read-only verification
  2. Paper trading
  3. Human-approved live-style execution
  4. Limited automation only after stable paper results
- Use strict risk controls:
  - Small-account bankroll logic even if the paper account has a large default balance
  - Long-only by default
  - No options, crypto, shorts, margin, penny stocks, or leveraged products by default
  - Require protective stop / trailing-stop behavior
  - Allow `NO_TRADE` when conditions or risk limits fail
- Use a multi-agent paper pipeline pattern:
  - Researcher
  - Trader
  - Confirmer / risk gate
  - Placer
- Do not create recursive scheduled jobs; keep one durable recurring cron job.

## Automation changes completed

### Automations dashboard

The dashboard Automations page was made more useful/interactable:

- Sidebar route: **Automations**
- Backward-compatible `/cron` route kept
- Job list visible
- Refresh button
- Search/filter box
- Status filter dropdown
- Showing X of Y counter
- Expandable job details
- Copy job ID
- Copy prompt
- Pause/resume
- Trigger now
- Delete
- Busy states for action buttons

Validation performed at the time:

- Browser check of the local Automations interface
- Alpaca paper automation visible
- Details expand/collapse worked
- Search/filter worked
- Browser console showed no JS errors
- TypeScript check passed
- Targeted ESLint passed for the changed Automations page file

### Cron schedule

Updated the Alpaca paper swing-trading automation from once daily to four weekday runs:

```cron
45 8,10,12,14 * * 1-5
```

Runs at:

- 8:45 AM
- 10:45 AM
- 12:45 PM
- 2:45 PM

using the server timezone.

## Paper trading run notes recalled from prior sessions

- The pipeline verified Alpaca paper endpoint usage before account/order operations.
- Alpaca paper endpoint expected/verified as `paper-api.alpaca.markets`.
- Read-only checks used account, positions, and open orders endpoints before placement.
- Secrets and raw account identifiers were not printed.
- Existing paper positions/orders have included ETFs such as `XLF`, `XLE`, and `SCHD`, with trailing-stop protection.
- A later run produced `NO_TRADE` because the small-bankroll risk policy already had enough open positions/orders.
- Stooq data access became unreliable due to API-key/captcha requirements; Yahoo Finance chart data was used successfully for market context.

## Open questions

- Should the 4 daily runs remain at 8:45, 10:45, 12:45, and 2:45 server time, or should they be aligned explicitly to Eastern market time?
- Should the pipeline have separate modes for:
  - morning scan,
  - midday position review,
  - afternoon stop/order review,
  - end-of-day summary?
- Should any trades require Discord approval before placement, or is paper-only autonomous placement acceptable under the existing risk policy?
- Should paper-account buying power be reset/rebalanced to match the intended strategy bankroll rather than relying on internal `$1,000` strategy-bankroll constraints?

## 2026-05-26 strategy update from the trading operator

New operating requirements:

- The system **can hold more than 4 open positions**.
- The full `$1,000` strategy bankroll should be intentionally utilized instead of leaving most of it idle.
- Add a profit-capture route because a prior weekend position was up, then later sold by trailing stop; the automation should try to capture weekly highs instead of only relying on trailing stops.
- Explore preset limit-sale behavior around weekly highs or realistic profit targets.
- Allocate **20% of the `$1,000` strategy bankroll** to penny-stock opportunities.
- Track and learn from smart buys/sells and bad buys/sells.
- At the start of every automation run, read relevant Obsidian project/context notes.
- At the end of every automation run, update Obsidian with decisions, outcomes, lessons, and open follow-ups.

Proposed portfolio buckets:

- `$800` core swing-trading bucket:
  - ETFs / liquid stocks / higher-quality setups.
  - Multiple smaller positions allowed.
  - Target near-full deployment when market conditions are acceptable.
- `$200` penny-stock bucket:
  - Max total exposure: 20% of bankroll.
  - Smaller position sizes, stricter liquidity/spread filters, and stricter loss caps.
  - Penny-stock trades should be tagged separately in logs and post-trade review.

Proposed exit routing:

- Keep protective stop/trailing stop as downside protection.
- Add profit-capture evaluation for each open position:
  - weekly high / 5-day high proximity,
  - unrealized gain percentage,
  - momentum fade signals,
  - time-in-trade,
  - market regime / overnight-weekend risk.
- Consider staged exits:
  - partial limit sell near weekly high or target zone,
  - trailing stop for remainder,
  - end-of-week risk reduction if a position is up but momentum is weakening.
- Avoid placing unrealistic sell limits at stale highs; targets should be adjusted using current price, ATR/range, liquidity, and spread.

Obsidian context loop requirement:

- Pre-run: read this project note plus any strategy/log notes under the Trading Automation project folder.
- During run: include which notes were read in the final report.
- Post-run: append a concise run log with:
  - market regime,
  - positions/orders before action,
  - candidates considered,
  - buys/sells/holds/rejections,
  - whether each decision looked smart/bad/uncertain based on available evidence,
  - lessons for future runs,
  - redacted order IDs only if operationally useful.

## 2026-05-27 correction — target limit must be paired with protection

The trading operator observed that visible limit sell orders for weekly max / weekly-high targets were not present, meaning the system was still relying too heavily on trailing stops and would not reliably capitalize gains.

Updated rule:

- Every new buy must receive a profit-capture target and protective downside exit in the same run after fill verification.
- Preferred structure is bracket/OCO-style: take-profit limit sell near a realistic weekly-high/target zone plus protective stop-loss.
- If Alpaca does not support a true trailing stop inside bracket/OCO, use fixed stop-loss plus later automated stop raises/replacements as synthetic trailing behavior.
- For one-share positions, do not skip the target solely because partial exits are impossible; use full-position target+stop structure or explicitly report why it cannot be safely placed.
- EOD audit must call out any position that is trailing-only or missing a target limit.

Cron updates:

- Main trading job `e20806d8bea2` renamed to `Alpaca paper swing-trading multi-agent pipeline v3 target+stop`.
- EOD audit job `e71ae2d739ff` updated to audit target+stop quality and flag trailing-only coverage as incomplete unless clearly justified.

## 2026-05-27 correction — no-purchase tracking and research expansion

The trading operator clarified that the automation should **not force buys**, but it should treat repeated no-purchase outcomes as a signal to broaden research.

Updated rule:

- Track `NO_CORE_BUY` and `NO_PENNY_BUY` separately each scheduled trading run.
- Log the reason for no purchase: cap full, no quality setup, spread too wide, low volume, no catalyst, already held/no averaging down, poor market conditions, unsafe order structure, or data unavailable.
- If there are 3 consecutive no-buys in an under-target bucket, expand research beyond the base watchlist.
- If there are 5 consecutive no-buys in an under-target bucket, explicitly report `RESEARCH_EXPANDED` and list the additional scans/sources used.
- Expanded research should increase discovery only; it must not loosen risk gates, penny-stock filters, or target+stop requirements.

## 2026-06-11 strategy update — Balanced v4.1

The trading operator observed that the paper bot had become **too conservative** after Defensive v4: recent target sells harvested winners and protected capital, but left the managed strategy exposure too low and the system too quick to sit in cash.

Durable update:

- Active mode changed from **Defensive v4** to **Balanced v4.1**.
- Trading remains **paper-only** unless separately and explicitly authorized otherwise.
- Main cron job `e20806d8bea2` is now `Balanced Paper Swing Trading v4.1 - Rebuild Exposure`, scheduled `45 8 * * 1-5`.
- EOD audit cron job `e71ae2d739ff` is now `Paper Trading EOD Audit Report - Balanced v4.1`, scheduled `10 16 * * 1-5` and read-only.
- Balanced v4.1 keeps OCO target + protective stop requirements, no averaging down, symbol/bucket cooldowns, and explicit `NO_TRADE` permission when gates fail.
- Under-deployment rule: if total managed strategy exposure is below about `$500`, the main job should broaden research and prefer one valid core buy rather than defaulting to cash, while still respecting setup quality and risk gates.
- Core entries can be **B+** quality when under-deployed, but should return to **A-grade** once exposure is healthier.
- Selective **non-biotech penny-stock** buys are allowed inside the `$200` penny sleeve when filters pass; risky biotech/FDA-binary penny buys remain disabled unless manually approved.
- Max new buys per main run is normally **2 total**: at most one core and one penny, only when both are valid.

Related updated notes: [[Trading Strategy Rules]], [[Buy Sell Lessons]], [[Trading Run Log]].

## Next actions

- [x] Update the cron prompt so every run reads related Obsidian Trading Automation notes before deciding. Implemented 2026-05-26; job `e20806d8bea2` renamed `Alpaca paper swing-trading multi-agent pipeline v2` and now loads `paper-trading-automation` + `obsidian` skills with file/web/terminal/delegation/session_search toolsets.
- [x] Update the cron prompt so every run appends a run log / learning note to Obsidian before final report. Implemented 2026-05-26 via mandatory `Trading Run Log.md` and `Buy Sell Lessons.md` updates.
- [x] Revise risk policy: allow more than 4 positions while keeping total strategy exposure capped at `$1,000`. Captured in `Trading Strategy Rules.md`.
- [x] Implement target allocation: `$800` core swing bucket and `$200` penny-stock bucket. Captured in `Trading Strategy Rules.md` and cron prompt v2.
- [x] Add sell-route logic for weekly-high/profit-capture limit sells, partial exits, and weekend risk review. Captured in `Trading Strategy Rules.md` and cron prompt v2.
- [x] Add buy/sell quality tracking: smart buy, bad buy, smart sell, bad sell, uncertain, with reasons. Captured in `Buy Sell Lessons.md`, `Trading Run Log.md`, and cron prompt v2.
- [ ] Confirm whether the four daily runs should use server time or market/Eastern time.
- [ ] Consider splitting the 4 daily runs into purpose-specific prompts instead of identical full trade-decision runs.
- [ ] Review recent paper-trading outcomes and decide whether to keep autonomous paper placement or switch to proposal-only reports.
