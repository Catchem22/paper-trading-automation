# Trading Strategy Rules

Updated: 2026-06-11 — Balanced v4.1 automation

Related: [[Trading Automation - Discord Thread Project Note]]

## Scope and safety

- This system is **paper trading only** unless the trading operator gives separate explicit live-trading authorization.
- Brokerage endpoint must resolve to Alpaca paper: `paper-api.alpaca.markets`.
- Never print or store API keys, secret keys, account IDs, account numbers, tokens, passwords, or raw credentials.
- Use the configured Alpaca environment variables only; report missing variable names, not values.
- Before any order placement, re-read account, positions, and open orders.
- Always allow `NO_TRADE` when conditions, data freshness, or risk gates fail.

## Strategy bankroll

The automation manages a **$1,000 strategy bankroll**, regardless of larger paper-account buying power.

Target allocation:

| Bucket | Target | Purpose |
|---|---:|---|
| Core swing bucket | $800 / 80% | Liquid stocks/ETFs and higher-quality swing setups |
| Penny-stock bucket | $200 / 20% | Smaller high-risk/high-reward penny-stock opportunities |

The prior fixed limit of four open positions is retired. The new rule is **risk/exposure based**, not position-count based.

## Balanced v4.1 overlay — active as of 2026-06-11

This overlay replaces the most restrictive Defensive v4 behavior. It keeps the paper-only safety rules, OCO exits, and no-chase discipline, but intentionally avoids sitting too far under-deployed after winners are harvested.

- Trading remains **paper-only**.
- Schedule is **one main trading run per weekday** plus one read-only end-of-day audit.
- New risky **biotech penny-stock** buys are disabled by default. Existing biotech penny positions may only be held, target-filled, stopped, or de-risked through verified OCO coverage. No averaging down.
- Selective **non-biotech penny-stock** buys are allowed inside the $200 penny sleeve when liquidity, spread, volume, catalyst/setup, and exit-plan gates pass.
- New core buys require at least a **B+ quality** setup when total managed exposure is below about $500, and an **A-grade** setup when exposure is already above about $500.
- Max new buys per main run: **2 total**, normally **1 core + 1 penny** if both buckets have valid setups. Do not force two buys when only one bucket has quality.
- Do not immediately replace a stopped-out position. Apply a 2-trading-day cooldown for the same symbol and highly similar risk buckets.
- Do not re-enter the exact same symbol on the same day after a target fill. Profit capture is success; do not chase. Related but not identical symbols may be considered only with fresh evidence and clean reward/risk.
- Rebuild exposure rule: if total managed exposure is below about **$500**, actively broaden research and prefer one valid core buy rather than defaulting to cash, provided the candidate fits the size/risk rules.
- Do not add core exposure unless current core exposure is at least about **$75 below** the $800 core target and the candidate still fits the $75–$150 normal position guide.
- Core setup requirements:
  - liquid ETF or larger/quality stock with tight spread,
  - relative strength or clean pullback/reclaim versus SPY and relevant sector/peer,
  - volume confirmation or credible catalyst,
  - no obvious near-term earnings/FOMC/high-impact event risk when applicable,
  - realistic reward/risk of at least **1.5:1** using planned target and stop,
  - not a recent stop-out or same-day exact-symbol target-fill chase,
  - immediate full-position OCO target-limit plus protective stop-loss coverage after fill.
- Relative-value/arbitrage research is read-only unless the trading operator explicitly promotes a strategy to paper execution. Reject anything dependent on sub-second latency, margin, shorting, options, crypto transfers, or unverifiable prices.

## Core swing bucket

- Target exposure: up to $800.
- Position size guide: $75–$150 each, adjusted by setup quality and remaining bucket capacity.
- Multiple open positions are allowed when total strategy exposure remains within the $1,000 bankroll.
- Prefer liquid ETFs/stocks with clean technical setups, sector strength, and manageable spreads.
- Avoid margin, shorts, options, crypto, and leveraged products by default.

## Penny-stock bucket

- Target/max exposure: $200 total.
- Position size guide: $25–$75 each, with $40–$75 preferred when the setup quality is high and remaining penny-sleeve capacity allows it.
- Penny stock definition: generally under $5/share.
- Stricter filters required:
  - sufficient volume/liquidity,
  - spread not excessive versus position size,
  - no obvious halt/delisting risk if detectable,
  - no risky biotech/FDA-binary setup unless the trading operator manually approves it,
  - no obvious reverse-split/pump-newsletter trap if detectable,
  - clear catalyst or technical setup,
  - explicit exit plan before entry.
- No automatic averaging down.
- Tag every penny-stock decision as `bucket: penny` and `risk_level: high`.

## Utilization rule

The automation should try to deploy most of the $1,000 when market conditions are acceptable. Cash drag should be reported each run.

Do not force trades just to reach 100% exposure. If the risk gate rejects candidates, hold cash and explain why.

## Exit manager / gain capture

Every run must evaluate existing positions before placing new buys.

Allowed exit-manager decisions:

- `HOLD`
- `RAISE_STOP`
- `TAKE_PARTIAL_PROFIT`
- `SELL_LIMIT_AT_TARGET`
- `SELL_MARKET`
- `NO_ACTION`

Profit-capture inputs:

- entry price,
- current price,
- unrealized gain/loss,
- current week high / 5-day high,
- prior week high / 10-day high when useful,
- recent range or ATR-like volatility estimate,
- momentum fade signals,
- time in trade,
- day-of-week / weekend risk,
- existing open sell orders.

Preferred behavior:

- **Every new buy must receive an exit structure in the same run immediately after fill verification.** Do not leave a new position with only an entry and no profit target.
- Preferred full-position structure: use a bracket/OCO-style exit with a take-profit limit near a realistic weekly-high/target zone plus a protective stop-loss.
- Important Alpaca constraint: do not assume a true trailing stop can be combined with a take-profit limit on the same shares. If Alpaca rejects trailing stop as an OCO/bracket leg, use a fixed stop-loss leg and have later automation runs raise/replace that stop as a synthetic trailing stop.
- If the position size supports splitting safely, the system may allocate part of the position to a target limit and part to trailing-stop protection, but it must not leave the total position uncovered or create duplicate sell orders that exceed quantity.
- For one-share ETF positions, choose a full-position bracket/OCO target+stop or choose a target limit with a hard stop plan; do not skip the target solely because partial exits are not possible.
- Keep protective stops/trailing or synthetic trailing stops as downside protection.
- If a position is up and approaching a realistic weekly-high/target zone, place or maintain a limit sell near that target, not just a passive trailing stop.
- If price is up but not yet at target, consider tightening/raising the stop while preserving the take-profit target when API order structure allows it.
- If Friday/near weekend and the position is up but momentum is weakening, consider partial profit-taking, target-limit exit, or tighter/raised stop.
- Avoid stale/unrealistic targets. Weekly-high targets should be adjusted for current price, spread, liquidity, and volatility.
- Never place duplicate sell orders that exceed the available position quantity after accounting for open sell orders.

## Decision quality tracking

Every run should classify important actions and non-actions:

- `SMART_BUY`
- `BAD_BUY`
- `SMART_SELL`
- `BAD_SELL`
- `SMART_HOLD`
- `BAD_HOLD`
- `UNCERTAIN`
- `NO_CORE_BUY`
- `NO_PENNY_BUY`

Do not over-classify too early. New buys are usually `UNCERTAIN` until later follow-through confirms whether the thesis worked.

## No-purchase tracking and research expansion

Do **not** force buys just to hit exposure targets. A clean `NO_CORE_BUY` or `NO_PENNY_BUY` is acceptable when candidates do not pass the risk gate.

However, the automation must track repeated no-purchase outcomes separately for the core bucket and penny-stock bucket:

- Log every run's core decision as `CORE_BUY`, `NO_CORE_BUY`, or `CORE_EXIT_ONLY`.
- Log every run's penny decision as `PENNY_BUY`, `NO_PENNY_BUY`, or `PENNY_EXIT_ONLY`.
- Include the reason: cap full, no quality setup, spread too wide, volume too low, catalyst missing, already held/no averaging down, market conditions poor, order-structure unsafe, or data unavailable.
- Maintain rolling counts from recent Trading Run Log entries, especially last 3 and last 5 scheduled trading runs.

Escalation rule:

- If there are **3 consecutive `NO_CORE_BUY`** outcomes while core exposure is below target by at least about $75, broaden core research beyond the base ETF/watchlist universe.
- If there are **3 consecutive `NO_PENNY_BUY`** outcomes while penny exposure is below target by at least about $50, broaden penny research beyond the base penny watchlist.
- If there are **5 consecutive no-buy outcomes** in either bucket, explicitly report `RESEARCH_EXPANDED` and document the additional sources/screens used.

Expanded research can include:

- fresh sector rotation / industry ETF scans,
- high-relative-volume gainers and reclaim setups,
- liquid small/mid-cap breakouts,
- earnings-gap continuation candidates after event risk is known,
- unusual-volume scans,
- finviz/market-watch style top gainers/relative volume lists,
- current news/catalyst search,
- additional penny-stock symbols only after liquidity, spread, volume, and catalyst checks.

Even after research expansion, trades still require the same risk gate and target+stop exit plan. Expanded research should increase opportunity discovery, not loosen safety rules.

For each decision, save:

- timestamp,
- symbol,
- action,
- bucket (`core` or `penny`),
- thesis,
- entry/exit plan,
- risk plan,
- order intent/result with identifiers redacted if present,
- classification,
- lesson.

## Required Obsidian context loop

At start of every automation run, read relevant files in this folder, including at minimum:

- `Trading Automation - Discord Thread Project Note.md`
- `Trading Strategy Rules.md`
- `Trading Run Log.md`
- `Buy Sell Lessons.md`

At completion, append a new section to `Trading Run Log.md` and add durable lessons to `Buy Sell Lessons.md` when applicable.

Final Discord report must mention which Obsidian notes were read and whether notes were updated.
