# Trading Run Log

Related: [[Trading Automation - Discord Thread Project Note]] · [[Trading Strategy Rules]] · [[Buy Sell Lessons]]

This note is append-only operational context for the Alpaca paper swing-trading automation. Do not store secrets, account numbers, account IDs, API keys, tokens, passwords, or raw credentials.

## Run log format

Each automation run should append:

```text
## YYYY-MM-DD HH:mm TZ — Scheduled paper run

Context notes read:
- ...

Market context:
- ...

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: $... / $800
- Penny exposure / target: $... / $200
- Cash/unutilized strategy bankroll: $...
- Open positions:
- Open orders:

Candidates reviewed:
- Core:
- Penny:

Actions:
- Buys:
- Sells:
- Stop/limit updates:
- Holds:
- Rejections / NO_TRADE reasons:
- No-purchase tracking:
  - Core decision: `CORE_BUY|NO_CORE_BUY|CORE_EXIT_ONLY`; reason:
  - Penny decision: `PENNY_BUY|NO_PENNY_BUY|PENNY_EXIT_ONLY`; reason:
  - Rolling pattern checked: last 3 / last 5 scheduled trading runs:
  - Research expanded this run? `yes|no`; sources/screens if yes:

Exit manager:
- Weekly-high / profit-capture checks:
- Trailing stop changes:
- Weekend risk actions:

Decision quality tags:
- SMART_BUY:
- BAD_BUY:
- SMART_SELL:
- BAD_SELL:
- SMART_HOLD:
- BAD_HOLD:
- UNCERTAIN:

Lessons / next run watchlist:
- ...
```

## 2026-05-26 14:18 CDT — Strategy v2 implementation note

The trading operator approved the Strategy v2 plan. The automation should now manage a $1,000 paper strategy bankroll with more than four open positions allowed, $800 core swing allocation, $200 penny-stock allocation, weekly-high/profit-capture exit routing, and an Obsidian start/end context loop.


## 2026-05-26 14:49 CDT — Scheduled paper run

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Yahoo chart data showed broad risk-on conditions: SPY, QQQ, IWM, XLK, SMH, XLI, XLY, and XLV above key moving averages, with QQQ/IWM/XLI near current 5-day highs.
- Existing energy position XLE had sold earlier by trailing stop; current core holdings IGV/SCHD/XLF remained profitable but lightly exposed.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $706.38 / $800
- Penny exposure / target: about $62.18 / $200
- Total strategy exposure: about $768.55 / $1,000
- Cash/unutilized strategy bankroll: about $231.45
- Open positions: BBAI, IGV, MVIS, SCHD, TLT, XLF, XLI, XLV, XLY
- Open orders: protective trailing-stop sell orders exist for each open position; identifiers redacted.

Candidates reviewed:
- Core: XLI, XLV, XLY, TLT, QQQ, IWM, XLK, SMH, SLV. Selected XLI/XLV/XLY/TLT to increase utilization while diversifying away from existing IGV/XLF/SCHD and avoiding over-concentration in stretched mega-cap/semiconductor exposure.
- Penny: BBAI, MVIS, KULR, OPEN. Selected small BBAI and MVIS starter positions due to sub-$5 price, high volume, constructive short-term technicals, and strict penny-sleeve sizing. Rejected KULR as too extended/volatile for this run; rejected OPEN because it remained below key moving averages.

Actions:
- Buys: XLI 1 share limit buy filled near $174.54; XLV 1 share filled near $148.89; XLY 1 share filled near $119.37; TLT 1 share filled near $85.08; BBAI 8 shares filled near $4.12; MVIS 45 shares filled near $0.651.
- Sells: no new discretionary sells; XLE had already filled via existing trailing stop earlier in the day near $58.16.
- Stop/limit updates: new protective trailing stops placed for all new buys: XLI 4%, XLV 4%, XLY 4%, TLT 3%, BBAI 10%, MVIS 12%.
- Holds: IGV, SCHD, XLF held with existing trailing-stop protection.
- Rejections / NO_TRADE reasons: no full NO_TRADE; partial cash kept because remaining opportunities were either overextended or would push core exposure above target.

Exit manager:
- Weekly-high / profit-capture checks: IGV, SCHD, XLF are profitable and within roughly 1% of recent highs, but each has only 1 share and already has trailing-stop protection, so no duplicate sell/target orders were placed.
- Trailing stop changes: new stops were added after the new buy fills; existing stops were left intact to avoid duplicate/excess sell orders.
- Weekend risk actions: none; Tuesday run, not near weekend.

Decision quality tags:
- SMART_BUY: XLI, XLV, XLY, TLT, BBAI, MVIS — exposure increased inside the $1,000 bankroll and bucket caps, with protective stops added.
- SMART_SELL: XLE existing trailing-stop exit protected the account from a weakening energy setup, although it appears to have realized a small loss versus recent entries.
- SMART_HOLD: IGV, SCHD, XLF — profitable/lightly sized and protected.
- UNCERTAIN: all new buys until follow-through is known.

Lessons / next run watchlist:
- Watch whether newly added core positions hold above their 5-day ranges or immediately reject near highs.
- Watch BBAI and MVIS closely; penny sleeve is intentionally small and should not be averaged down automatically.
- Next run should consider profit-capture limit targets if IGV/SCHD/XLF or the new ETF positions push to fresh 5-day highs with fading momentum.

## 2026-05-26 16:10 CDT — End-of-day paper audit

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market/account context:
- Alpaca endpoint verified as paper-only host `paper-api.alpaca.markets`.
- Read-only audit only: account, positions, open orders, and today's fill activities inspected; no orders submitted.
- Paper account status active; raw account identifiers redacted.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $705.92 / $800
- Penny exposure / target: about $62.61 / $200
- Total strategy exposure: about $768.53 / $1,000
- Unused strategy bankroll / cash drag: about $231.47
- Open positions: BBAI, IGV, MVIS, SCHD, TLT, XLF, XLI, XLV, XLY
- Open orders: trailing-stop sell orders exist for all 9 open positions; no separate profit-target/limit-exit orders were open.

Today's paper actions/fills:
- Buy fills: XLI 1, XLV 1, TLT 1, XLY 1, BBAI 8, MVIS 45 total via two fills.
- Sell fill: XLE 1 sold by existing trailing stop.
- Open protective orders: trailing stops for BBAI, IGV, MVIS, SCHD, TLT, XLF, XLI, XLV, XLY.

Exit manager:
- Weekly-high/profit-capture review: IGV, SCHD, TLT, XLF, XLI, and XLY were within roughly 1% of 5-day highs; XLV within roughly 1.2%; MVIS within roughly 3%; BBAI still about 9.8% below its 5-day high.
- Stop placement quality: good coverage; every open position appears protected by a trailing-stop order sized to the full open position.
- Profit-capture quality: incomplete; no open target/limit exits exist, so positions near 5-day highs are still relying only on trailing stops. Single-share ETF positions cannot partial out cleanly, so next runs should consider either target limit exits or raised/tighter trailing stops when price is near weekly highs.
- Weekend risk: no immediate Friday/weekend action needed today.

Decision quality tags:
- SMART_BUY: XLI, XLV, TLT, XLY, BBAI, MVIS remain tentatively smart because they increased utilization inside bucket limits and were immediately protected with stops.
- SMART_SELL: XLE trailing-stop sale reduced exposure to a weakening holding, though it may have given back earlier upside.
- SMART_HOLD: holding protected IGV/SCHD/XLF/TLT/XLI/XLY is reasonable while paper positions are small and near highs.
- UNCERTAIN: all new buys and the choice not to add profit-target limits yet; needs next-run follow-through.

Lessons / next run watchlist:
- Utilization improved but still leaves about 23% of the $1,000 bankroll idle; next trade run can add only if quality setups appear and stops/exit plans are ready.
- Penny exposure is safely under the $200 sleeve; do not average down BBAI/MVIS automatically.
- Add explicit profit-capture route for near-high single-share ETF positions: target limit sell or tighter trailing stop, not just passive trailing stops.

## 2026-05-27 14:45 CDT — Scheduled paper run

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Alpaca endpoint was verified as paper-only host `paper-api.alpaca.markets`; account, positions, open orders, and recent fills were checked before action and re-checked before placement.
- Yahoo chart data showed broad risk-on conditions: SPY, QQQ, IWM, XLK, XLI, XLY, and TLT were above short moving averages and close to 5-day highs. XRT showed constructive retail momentum above 5/10-day averages. Penny candidates were mixed: BBAI remained strong and liquid; OPEN had high volume and a fresh reclaim attempt but remained high-risk.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $790.66 / $800
- Penny exposure / target: about $112.26 / $200
- Total strategy exposure: about $902.92 / $1,000
- Cash/unutilized strategy bankroll: about $97.08
- Cash-drag reason: remaining cash preserved because adding another whole-share core ETF would exceed or crowd the $800 core cap, and penny sleeve still requires selective high-risk entries only.
- Open positions: BBAI, IGV, MVIS, OPEN, SCHD, TLT, XLF, XLI, XLV, XLY, XRT.
- Open orders: protective trailing-stop sell orders exist for BBAI, IGV, MVIS, OPEN, SCHD, TLT, XLF, XLI, XLV, XLY, and XRT. XLI initially did not appear in the final open-order summary, so the run re-checked the paper account and added a 4% trailing stop for XLI; verification confirmed the XLI stop was active.

Candidates reviewed:
- Core: XRT, XLU, XLP, VNQ, SLV, XLK, QQQ, IWM. Selected XRT as a one-share core add because it fit remaining core capacity and showed momentum above short moving averages. Rejected QQQ/IWM/XLK/SMH due to whole-share price/cap fit or concentration; rejected XLU/XLP/VNQ as lower urgency than XRT; rejected SLV due to weaker short-term trend.
- Penny: OPEN, KULR, BBAI, MVIS, SOUN, LUNR. Selected small OPEN starter position due to sub-$5 price, high volume, momentum reclaim, and explicit stop plan. Rejected KULR as too extended/volatile near a wide intraday range; rejected SOUN and LUNR as not penny sleeve under current price definition; no averaging down in MVIS.

Actions:
- Buys: XRT 1 share filled near $84.01; OPEN 10 shares filled near $4.83.
- Sells: no market or target sells placed.
- Stop/limit updates: BBAI trailing stop tightened from 10% to 6%; XLY trailing stop tightened from 4% to 2.5%; new protective trailing stops placed for XRT at 5%, OPEN at 10%, and XLI at 4% after missing-stop verification.
- Holds: IGV, MVIS, SCHD, TLT, XLF, XLI, XLV held; no duplicate target orders were placed over existing trailing-stop coverage.
- Rejections / NO_TRADE reasons: no full NO_TRADE. Additional trades rejected to stay inside the $1,000 strategy bankroll, $800 core cap, and $200 penny cap.

Exit manager:
- Weekly-high / profit-capture checks: XLY was up about 1.7% and within about 0.5% of its 5-day high, so the stop was tightened to reduce giveback risk. BBAI was up about 7.6% and liquid, so the penny-stock stop was tightened from a wide 10% trail to a 6% trail. TLT and XLI were near 5-day highs but were not meaningfully profitable enough for target exits. IGV/SCHD/XLF/XLV were held with existing protection.
- Trailing stop changes: BBAI and XLY trailing stops were canceled/recreated tighter; XRT and OPEN stops were added after fills; XLI missing-stop coverage was repaired and verified.
- Weekend risk actions: none; Wednesday run, not immediate Friday/weekend risk.

Decision quality tags:
- SMART_BUY: XRT — improved core utilization without breaching bucket cap and had immediate stop protection.
- SMART_BUY: OPEN — small high-risk penny starter stayed inside sleeve with high volume and immediate stop protection.
- SMART_HOLD: IGV, MVIS, SCHD, TLT, XLF, XLI, XLV — exposure remained within policy and no duplicate/excess sell orders were placed.
- SMART_SELL: BBAI and XLY stop-tightening actions were profit-capture/risk-reduction actions, not direct sells.
- UNCERTAIN: XRT and OPEN buy outcomes; BBAI/XLY tightened stops need follow-through to prove whether they protected gains without cutting winners too early.

Lessons / next run watchlist:
- Re-check XLI stop coverage next run because this run had to repair a missing protective stop after the initial final summary.
- Watch XRT follow-through above its 5-day breakout range; invalidation is a failure back under the recent breakout/5-day low zone.
- Watch OPEN closely; no averaging down, and penny exposure remains intentionally capped below $200 until quality improves.
- Tighter trailing stops are the cleanest profit-capture route for single-share positions when partial exits are impossible.

## 2026-05-27 16:10 CDT — End-of-day paper audit

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market/account context:
- Alpaca endpoint verified as paper-only host `paper-api.alpaca.markets`.
- Read-only audit only: account, positions, open orders, and today's activities were inspected; no orders submitted.
- Paper account status active; raw account identifiers redacted.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $792.73 / $800
- Penny exposure / target: about $111.35 / $200
- Total strategy exposure: about $904.09 / $1,000
- Unused strategy bankroll / cash drag: about $95.91
- Open positions: BBAI, IGV, MVIS, OPEN, SCHD, TLT, XLF, XLI, XLV, XLY, XRT
- Open orders: 11 open sell trailing-stop orders; every open position has visible protective trailing-stop coverage.

Today's paper actions/fills:
- Buy fills observed after today's start: XRT 1 share near $84.01; OPEN 10 shares total near $4.83 across two fills.
- No EOD audit orders were submitted.

Exit manager:
- Weekly-high/profit-capture checks: TLT, XLI, and XLY were within roughly 0.2% of their 5-day highs; IGV and SCHD were within roughly 1%; XLV/XLF/XRT were about 1.0%–1.8% below; BBAI/MVIS/OPEN were about 4%–5% below recent highs.
- Stop placement quality: good; BBAI 6%, XLY 2.5%, TLT/SCHD/XLF 3%, IGV/XLI/XLV 4%, XRT 5%, OPEN 10%, MVIS 12% trailing stops were visible.
- Profit-capture quality: improved versus prior audit because BBAI and XLY were tightened during the scheduled run, and XLI missing-stop coverage was repaired. Still no separate target/limit exits are open; for one-share positions, next runs should choose between tighter stops and realistic target exits when near highs.
- Weekend risk: no immediate Friday/weekend action needed today.

Decision quality tags:
- SMART_BUY: XRT and OPEN remain tentatively smart because they improved utilization inside the $1,000 bankroll, respected bucket caps, and received immediate stops.
- SMART_HOLD: Holding the protected core positions is reasonable while exposure is near target and no duplicate sell orders are needed.
- SMART_SELL: BBAI/XLY stop tightening from the afternoon run remains a smart profit-capture/risk-reduction action.
- UNCERTAIN: OPEN and XRT follow-through, plus whether tight stops preserve gains without premature exits.

Lessons / next run watchlist:
- Cash drag is now under 10% of the managed bankroll and is acceptable unless high-quality candidates appear; do not force penny exposure just to fill the sleeve.
- Re-check XLI stop coverage again next run because it was repaired today and should remain visible.
- Watch TLT/XLI/XLY near 5-day highs for target exits or tighter stops; avoid relying only on passive trailing stops if momentum fades.

## 2026-05-27 16:40 CDT — Scheduled paper run

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Alpaca endpoint verified as paper-only host `paper-api.alpaca.markets`; account, positions, open orders, and recent fills were checked before action and re-checked before placement.
- Yahoo chart data showed broad risk-on conditions with SPY/QQQ/IWM near 5-day highs. Existing positions BBAI, XLY, XLI, IGV, SCHD, TLT, XLF, and XLV were close enough to recent highs to require target/stop review.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $792.45 / $800
- Penny exposure / target: about $111.85 / $200
- Total strategy exposure: about $904.30 / $1,000
- Cash/unutilized strategy bankroll: about $95.70
- Cash-drag reason: core bucket is effectively full; penny sleeve has capacity but screened penny candidates did not justify adding risk without stronger catalyst/data.
- Open positions: BBAI, IGV, MVIS, OPEN, SCHD, TLT, XLF, XLI, XLV, XLY, XRT
- Open orders after action: OCO target+stop exits for BBAI, XLI, and XLY; trailing-stop protection remains for IGV, MVIS, OPEN, SCHD, TLT, XLF, XLV, and XRT.

Candidates reviewed:
- Core: XLU, XLP, SLV, XLK, QQQ, IWM, SOUN, LUNR. Rejected for new buys because core exposure is already near the $800 cap, several candidates were too expensive for remaining capacity, and this run prioritized exit quality.
- Penny: KULR, BBAI, MVIS, OPEN. BBAI was already profitable and selected for target+stop upgrade; KULR was volatile/extended, MVIS and OPEN were already held and not eligible for averaging down.

Actions:
- Buys: none.
- Sells/order upgrades: canceled the prior trailing-only sell orders for XLY, BBAI, and XLI, then replaced them with full-position Alpaca paper OCO exits: XLY target limit $122.74 + stop $118.73 for 1 share; BBAI target limit $4.58 + stop $4.04 for 8 shares; XLI target limit $175.96 + stop $170.20 for 1 share. Post-action verification showed the OCO limit parents accepted and protective stop legs held.
- Stop/limit updates: upgraded three trailing-only positions to target+stop structures; no duplicate/excess sell coverage was left for those symbols.
- Holds: IGV, MVIS, OPEN, SCHD, TLT, XLF, XLV, and XRT held with existing trailing-stop protection.
- Rejections / NO_TRADE reasons: no new buy; risk gate rejected new exposure because core is near cap and penny candidates were not strong enough.

Exit manager:
- Weekly-high / profit-capture checks: XLY was profitable and near its 5-day high, BBAI was up about 6.6%, and XLI was near its 5-day high; all three were upgraded from trailing-only to explicit target+stop OCO coverage.
- Remaining trailing-only positions: IGV, SCHD, TLT, XLF, XLV, XRT, OPEN, and MVIS still lack visible target limits. They retain protective trailing stops. Next runs should continue phased upgrades where profitable/near-high and safe, while avoiding wholesale cancellation/replacement risk.
- Weekend risk actions: none; Wednesday run.

Decision quality tags:
- SMART_SELL: XLY, BBAI, XLI order upgrades — moved from trailing-only coverage to explicit profit-capture target plus protective stop without exceeding owned quantity.
- SMART_HOLD: no new buys while core exposure is near the $800 cap and total utilization is already about 90%.
- UNCERTAIN: whether the new target prices are hit before stop legs; monitor follow-through.

Lessons / next run watchlist:
- Alpaca paper OCO exits worked for full-position target+stop coverage on whole-share/tiny positions; use this as preferred v3 upgrade path when a position is profitable or near recent highs.
- Next run should inspect OCO leg status for BBAI/XLI/XLY and continue phased upgrades for high-priority trailing-only positions only when it can be done without leaving gaps or duplicate sell coverage.


## 2026-05-27 16:45 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; read-only account, positions, open orders, and recent fills were checked before action. Account identifiers and credentials redacted.
- SPY $750.46 vs 5d high $752.13 (-0.2% from high); QQQ $729.45 vs 5d high $733.32 (-0.5% from high); IWM $290.37 vs 5d high $291.72 (-0.5% from high)

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: $790.91 / $800
- Penny exposure / target: $111.25 / $200
- Total strategy exposure: $902.16 / $1,000
- Cash/unutilized strategy bankroll: $97.84
- Cash-drag reason: total utilization is about 90.2%; core bucket has only about $9.09 remaining, while penny capacity is reserved for stronger catalysts rather than forced averaging down.
- Open positions and exit coverage:
- BBAI 8 (penny) value~$34.96 target=yes stop=yes
- IGV 1 (core) value~$93.04 target=no stop=yes
- MVIS 45 (penny) value~$28.79 target=no stop=yes
- OPEN 10 (penny) value~$47.50 target=no stop=yes
- SCHD 1 (core) value~$32.55 target=yes stop=yes
- TLT 1 (core) value~$85.30 target=yes stop=yes
- XLF 1 (core) value~$51.42 target=no stop=yes
- XLI 1 (core) value~$174.30 target=yes stop=yes
- XLV 1 (core) value~$148.79 target=yes stop=yes
- XLY 1 (core) value~$121.55 target=yes stop=yes
- XRT 1 (core) value~$83.96 target=no stop=yes
- Open order count after verification: 11

Candidates reviewed:
- Core:
- XLU: watchlist momentum/defensive rotation — price $45.14, 5-day high $45.64; core bucket capacity only $9.09 (confidence medium)
- XLP: watchlist momentum/defensive rotation — price $84.58, 5-day high $86.07; core bucket capacity only $9.09 (confidence low)
- VNQ: watchlist momentum/defensive rotation — price $96.92, 5-day high $97.71; core bucket capacity only $9.09 (confidence medium)
- SLV: watchlist momentum/defensive rotation — price $67.50, 5-day high $69.75; core bucket capacity only $9.09 (confidence low)
- XLK: watchlist momentum/defensive rotation — price $184.43, 5-day high $186.26; core bucket capacity only $9.09 (confidence medium)
- QQQ: watchlist momentum/defensive rotation — price $729.45, 5-day high $733.32; core bucket capacity only $9.09 (confidence medium)
- IWM: watchlist momentum/defensive rotation — price $290.37, 5-day high $291.72; core bucket capacity only $9.09 (confidence medium)
- SOUN: watchlist momentum/defensive rotation — price $8.08, 5-day high $8.84; core bucket capacity only $9.09 (confidence low)
- Penny:
- KULR: penny sleeve catalyst/momentum screen — price $4.72, avg volume 3,924,249; no averaging down on existing holdings (confidence medium)
- BBAI: penny sleeve catalyst/momentum screen — price $4.37, avg volume 51,858,835; no averaging down on existing holdings (confidence medium)
- MVIS: penny sleeve catalyst/momentum screen — price $0.64, avg volume 5,338,294; no averaging down on existing holdings (confidence medium)
- OPEN: penny sleeve catalyst/momentum screen — price $4.75, avg volume 39,289,517; no averaging down on existing holdings (confidence medium)

Actions:
- Buys: none.
- Sells/order upgrades:
- SCHD: upgraded trailing/stop-only sell coverage to OCO target $32.84 + stop $31.60 for 1 share(s); canceled 1 prior sell order(s).
- TLT: upgraded trailing/stop-only sell coverage to OCO target $85.98 + stop $82.31 for 1 share(s); canceled 1 prior sell order(s).
- XLV: upgraded trailing/stop-only sell coverage to OCO target $150.02 + stop $143.58 for 1 share(s); canceled 1 prior sell order(s).
- Holds:
- IGV: held with protective stop but no visible target limit; queued for phased v3 upgrade when safe.
- MVIS: held with protective stop but no visible target limit; queued for phased v3 upgrade when safe.
- OPEN: held with protective stop but no visible target limit; queued for phased v3 upgrade when safe.
- XLF: held with protective stop but no visible target limit; queued for phased v3 upgrade when safe.
- XRT: held with protective stop but no visible target limit; queued for phased v3 upgrade when safe.
- Rejections / NO_TRADE reasons:
- NO_NEW_BUY: strategy utilization $902.16 is already near-full; core capacity $9.09; penny capacity $88.75 reserved for higher-quality catalysts.
- V3 incomplete target coverage remains: IGV, MVIS, OPEN, XLF, XRT

Exit manager:
- Weekly-high / profit-capture checks: prioritized trailing-only positions near recent highs or profitable enough for full-position OCO target+stop coverage.
- Target-limit coverage missing after this run: IGV, MVIS, OPEN, XLF, XRT.
- Protective stops missing after this run: none.
- Weekend risk actions: none; Wednesday run.

Decision quality tags:
- SMART_SELL: SCHD target+stop upgrade
- SMART_SELL: TLT target+stop upgrade
- SMART_SELL: XLV target+stop upgrade
- SMART_HOLD: BBAI protected/monitored
- SMART_HOLD: IGV protected/monitored
- SMART_HOLD: MVIS protected/monitored
- SMART_HOLD: OPEN protected/monitored
- SMART_HOLD: SCHD protected/monitored
- SMART_HOLD: TLT protected/monitored
- SMART_HOLD: XLF protected/monitored
- SMART_HOLD: XLI protected/monitored
- SMART_HOLD: XLV protected/monitored
- SMART_HOLD: XLY protected/monitored
- SMART_HOLD: XRT protected/monitored

Lessons / next run watchlist:
- OCO target+stop upgrades can be phased across trailing-only positions after cancel/re-read/replace/verify; avoid adding independent target orders over full-quantity trailing stops.
- Next run should inspect OCO leg status for BBAI, SCHD, TLT, XLI, XLV, and XLY, then continue phased upgrades for IGV/XLF/XRT or penny names only if safe and without duplicate sell quantity.


## 2026-05-28 08:46 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, and recent fills were checked before action and re-checked before each replacement. Credentials and account identifiers were not recorded.
- Broad ETF backdrop from Yahoo chart data remained near recent highs but softer than prior run: SPY about 0.4% below 5-day high, QQQ about 0.8% below, IWM about 1.1% below. No new buy was needed before exit-quality repair.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $640.99 / $800
- Penny exposure / target: about $110.09 / $200
- Total strategy exposure: about $751.08 / $1,000
- Cash/unutilized strategy bankroll: about $248.92
- Cash-drag reason: XLV target filled before/during this run, reducing core exposure; this run prioritized completing v3 target+stop coverage over immediately redeploying fresh cash.
- Open positions: BBAI, IGV, MVIS, OPEN, SCHD, TLT, XLF, XLI, XLY, XRT
- Recent fill observed: XLV 1 share sold at target near $150.02; identifiers redacted.

Candidates reviewed:
- Core: IGV, XLF, XRT were already held and selected for exit-structure upgrade; XLU/XLP/XLK/SPY/QQQ/IWM stayed watchlist only because no new exposure was needed before fixing exits.
- Penny: MVIS and OPEN were already held and selected for target+stop upgrade despite being down; KULR/SOUN/LUNR watched but rejected for new buy due to volatility/price fit and because penny sleeve should not be forced.

Actions:
- Buys: none.
- Sells/fills: XLV target OCO leg filled near $150.02 before/during the run, realizing the planned profit-capture exit and removing XLV from open positions.
- Stop/limit updates: upgraded IGV, XLF, XRT, MVIS, and OPEN from trailing-only coverage to full-position Alpaca paper OCO target+stop exits after cancel/re-read/replace/verify.
  - IGV: target $95.20 + stop $91.25 for 1 share.
  - XLF: target $52.01 + stop $49.59 for 1 share.
  - XRT: target $85.50 + stop $82.75 for 1 share.
  - MVIS: target $0.6600 + stop $0.5786 for 45 shares.
  - OPEN: target $4.94 + stop $4.35 for 10 shares.
- Holds: BBAI, SCHD, TLT, XLI, XLY retained verified OCO target+stop coverage.
- Rejections / NO_TRADE reasons: NO_NEW_BUY. The risk gate rejected fresh buys until all exits were repaired and because new cash from XLV should be redeployed only into quality setups, not forced.

Exit manager:
- Weekly-high / profit-capture checks: all open positions now have visible target-limit profit capture and protective stop-loss coverage via OCO structure.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Note: the first OCO attempt used an invalid Alpaca payload shape and was rejected safely; trailing stops were immediately repaired, then the corrected `take_profit.limit_price` OCO structure was submitted and verified.
- Weekend risk actions: none; Thursday morning run, but next runs should monitor Friday/weekend exposure and decide whether to tighten stops if momentum fades.

Decision quality tags:
- SMART_SELL: XLV target exit filled; this is exactly the v3 profit-capture behavior requested.
- SMART_SELL: IGV, XLF, XRT, MVIS, OPEN OCO upgrades; they replaced trailing-only coverage with explicit target+stop coverage without duplicate sell quantity.
- SMART_HOLD: no new buys while exit quality was being repaired and fresh cash needed better confirmation.
- UNCERTAIN: MVIS/OPEN targets and stops; both are still below entry and need follow-through or disciplined stop execution.

Lessons / next run watchlist:
- Correct Alpaca paper OCO payload for existing-position exits requires `take_profit.limit_price` plus `stop_loss.stop_price`; a top-level `limit_price` alone is rejected.
- Next run can consider redeploying some of the freed core cash after confirming all OCO exits remain open and market/candidate quality is acceptable.
- Watch MVIS/OPEN closely; do not average down automatically. Watch IGV/XRT for target fills near recent highs.

## 2026-05-28 10:45 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, and recent fills were checked before action and re-checked before placement/replacement. Credentials and account identifiers were not recorded.
- Yahoo chart data showed broad ETFs still near short-term highs: SPY about 0.04% below its 5-day high, QQQ about 0.11% below, and IWM about 0.14% below. VNQ and XLK were above short moving averages and near 5-day highs.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target after action: about $749.24 / $800
- Penny exposure / target after action: about $27.63 / $200
- Total strategy exposure: about $776.87 / $1,000
- Cash/unutilized strategy bankroll: about $223.13
- Cash-drag reason: multiple target exits earlier in the morning freed capital; this run redeployed only into two liquid core ETF setups with explicit exits, leaving unused bankroll because penny sleeve candidates did not justify forced risk and core remains below but close to target.
- Open positions after action: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY.
- Recent target fills observed: BBAI sold at target near $4.58, OPEN sold at target near $4.94, IGV sold at target near $95.20, XRT sold at target near $85.50, and XLV had sold at target near $150.02 earlier.

Candidates reviewed:
- Core: VNQ and XLK selected because each was liquid, above short moving averages, near 5-day highs, and fit remaining core capacity after target exits. XLP/XLU stayed watchlist; XLP was acceptable but the run avoided over-deploying after two fills, and XLU was weaker versus its short-term averages.
- Penny: KULR, BBAI, MVIS, and OPEN reviewed. No new penny buy: BBAI/OPEN already hit targets and were no longer held, MVIS remains held and is not eligible for automatic averaging down, KULR remained extended/volatile.

Actions:
- Buys: VNQ 1 share filled near $97.03; XLK 1 share filled near $187.11.
- Sells/fills: no discretionary market sells. Target fills from earlier open OCO exits were observed for BBAI, OPEN, IGV, XRT, and XLV.
- Stop/limit updates: initial bracket buy exits for VNQ and XLK did not show visible stop coverage after fill verification, so the run canceled the visible target-only sell coverage and replaced it with full-position OCO exits:
  - VNQ target $98.47 + stop $93.61 for 1 share.
  - XLK target $189.94 + stop $180.58 for 1 share.
- Holds: MVIS, SCHD, TLT, XLF, XLI, XLY held with verified target+stop OCO coverage.
- Rejections / NO_TRADE reasons: no penny add and no additional core add after VNQ/XLK; cash preserved because forced penny risk or over-deployment after fresh target fills would reduce decision quality.

Exit manager:
- Weekly-high / profit-capture checks: all open positions now show visible target-limit profit capture and protective stop-loss coverage.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Important repair: bracket acceptance was not treated as sufficient. VNQ/XLK were re-read after fill, target-only visibility was detected, and both were repaired to OCO target+stop coverage before ending the run.
- Weekend risk actions: none yet; Thursday midday. Next runs should reassess Friday/weekend risk and consider tighter stops only if momentum fades.

Decision quality tags:
- SMART_SELL: BBAI, OPEN, IGV, XRT, and XLV target exits — profit-capture behavior worked as designed.
- UNCERTAIN: VNQ and XLK buys — good setup/exit structure, but outcomes need follow-through; XLK size is above the normal $75–$150 guide but still inside the core bucket and total strategy cap.
- SMART_HOLD: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLY held with verified OCO exits and no duplicate sell quantity.
- SMART_HOLD: keeping about $223 unused rather than forcing lower-quality penny/crowded entries.

Lessons / next run watchlist:
- Bracket buys still require post-fill verification of both exit legs; repair immediately if stop coverage is not visible.
- Watch VNQ/XLK target/stop OCO legs and verify they remain paired.
- Penny sleeve is mostly cash after BBAI/OPEN target exits; only redeploy if a clean high-liquidity catalyst appears. Do not average down MVIS automatically.

## 2026-05-28 12:47 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, clock, and recent fills were checked read-only before any decision. Market clock was open. Credentials and account identifiers were not recorded.
- Broad ETF backdrop remained constructive and near highs: SPY about 0.03% below 5-day high, QQQ about 0.01% below, and IWM about 0.22% below. This supported holding existing protected exposure but also increased re-entry/chasing risk after morning target fills.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $749.56 / $800
- Penny exposure / target: about $27.30 / $200
- Total strategy exposure: about $776.86 / $1,000
- Cash/unutilized strategy bankroll: about $223.14
- Cash-drag reason: core bucket has only about $50 remaining, below the normal $75-$150 core position guide unless using a very small ETF add; penny sleeve has capacity but clean candidates did not justify chasing immediately after target exits or averaging down MVIS.
- Open positions: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY.
- Recent fills observed: VNQ and XLK buys from the prior run; target exits earlier today for BBAI, OPEN, IGV, XRT, and XLV. Identifiers redacted.

Candidates reviewed:
- Core: XLP, XLU, VNQ, XLK, XLF, XLI, XLY, TLT, SCHD, SLV, QQQ, IWM. XLK/XLY/TLT/XLI remained near 5-day highs and already held; XLP was acceptable but would exceed remaining core capacity under whole-share sizing; XLU and SLV were weaker versus short averages; QQQ/IWM were too large for the small-bankroll structure.
- Penny: KULR, BBAI, OPEN, MVIS, SOUN, LUNR. BBAI was liquid and near highs but had just hit target, so immediate rebuy was rejected as chase risk. MVIS remained held and below short averages, so no averaging down. KULR was high-risk/volatile; OPEN/SOUN/LUNR were above the penny-stock price definition for this sleeve.

Actions:
- Buys: none.
- Sells: none submitted by this run.
- Stop/limit updates: none needed; all open positions already had visible target-limit profit capture and protective stop-loss coverage.
- Holds: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, and XLY held with verified OCO target+stop coverage.
- Rejections / NO_TRADE reasons: NO_NEW_BUY because utilization is already about 77.7%, core capacity is too small for most clean whole-share core adds, and penny candidates did not pass the strict liquidity/spread/catalyst/exit-quality filter without chasing.

Exit manager:
- Weekly-high / profit-capture checks: all open positions show visible target-limit and stop-loss OCO coverage. XLY, TLT, XLK, and XLI are closest to recent highs and should be watched for target fills or Friday stop-tightening decisions.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: none yet; Thursday midday. Next run should reassess Friday/weekend risk and consider tightening/raising stops only if momentum fades or targets remain just out of reach.

Decision quality tags:
- SMART_HOLD: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY — all had verified target+stop coverage and no duplicate sell quantity.
- SMART_HOLD: no new buys after target fills; preserved capital instead of chasing BBAI/OPEN immediately after exits or forcing low-quality penny exposure.
- UNCERTAIN: VNQ/XLK follow-through from the prior run and whether near-high OCO targets on XLY/TLT/XLI/XLK fill before stops.

Lessons / next run watchlist:
- Do not automatically rebuy a penny name immediately after a target fill just because it remains liquid and near highs; require a fresh setup and avoid chase entries.
- Next run should verify all OCO legs remain paired, watch for target fills in XLY/TLT/XLI/XLK, and reassess Friday/weekend stop-tightening if momentum fades.

## 2026-05-28 14:46 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, and recent fills were checked read-only before decisions. Market clock was open. Credentials and raw account identifiers were not recorded.
- Broad ETF backdrop remained risk-on/near highs from Yahoo chart data: SPY about 0.03% below 5-day high, QQQ about 0.08% below, and IWM about 0.13% below. This supports holding protected exposure but increases chase risk for fresh entries.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $749.25 / $800
- Penny exposure / target: about $28.06 / $200
- Total strategy exposure: about $777.31 / $1,000
- Cash/unutilized strategy bankroll: about $222.69
- Cash-drag reason: core capacity is only about $50.75, below normal $75-$150 core position guide except for weaker small ETF adds; penny sleeve has capacity, but BBAI/OPEN just hit targets and immediate rebuy would be chase risk, KULR is extended/volatile, MVIS is already held and not eligible for averaging down.
- Open positions: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY.
- Recent fills observed: VNQ and XLK buys from the prior run; earlier target exits today for BBAI, OPEN, IGV, XRT, and XLV. Identifiers redacted.

Candidates reviewed:
- Core: XLP, XLU, SLV, VNQ, XLK, XLF, XLI, XLY, TLT, SCHD, SPY, QQQ, IWM. XLK/XLI/XLY/TLT/SCHD were near 5-day highs but already held with target+stop coverage; XLU was low-priced enough for remaining core capacity but in a mixed/pullback setup; XLP exceeded remaining core capacity; SPY/QQQ/IWM were too large for this small-bankroll structure.
- Penny: BBAI, KULR, OPEN, MVIS, SOUN, LUNR. BBAI was liquid and near highs but had just hit target earlier today, so immediate rebuy was rejected as chase risk. OPEN was above the <$5 penny definition at inspection; KULR remained extended/volatile; MVIS remained held and below short-term momentum, so no averaging down. SOUN/LUNR did not fit the penny sleeve price rule.

Actions:
- Buys: none.
- Sells: none submitted by this run.
- Stop/limit updates: none needed. All open positions showed visible target-limit profit capture and protective stop-loss coverage via OCO-style structures.
- Holds: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY held with verified target+stop coverage.
- Rejections / NO_TRADE reasons: NO_NEW_BUY because candidate quality did not justify adding exposure; remaining core capacity is small, and penny-capacity deployment would require chasing recent target exits or accepting weaker catalyst/volatility quality.

Exit manager:
- Weekly-high / profit-capture checks: XLY, TLT, XLK, XLI, and SCHD were closest to recent highs and already have target-limit exits paired with protective stops. MVIS remains protected but weak; no averaging down.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: none yet; Thursday afternoon. Next run should reassess Friday/weekend exposure and consider raising stops if momentum fades or targets remain just out of reach.

Decision quality tags:
- SMART_HOLD: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY — all had verified target+stop coverage and no duplicate sell quantity was added.
- SMART_HOLD: no new buys; preserved capital instead of chasing BBAI/OPEN after target fills or forcing lower-quality penny/core entries.
- UNCERTAIN: VNQ/XLK follow-through from prior run and whether near-high OCO targets on XLY/TLT/XLI/XLK/SCHD fill before stops.

Lessons / next run watchlist:
- OCO coverage remained intact across all open positions; continue verifying parent/leg visibility before any new buy.
- Watch XLY/TLT/XLI/XLK/SCHD for possible target fills. On the next Friday/late-week run, consider stop raises/replacements only if the market loses momentum or positions remain near targets without filling.
- Penny sleeve cash is intentional right now; require a fresh setup before re-entering BBAI/OPEN and do not average down MVIS automatically.


## 2026-05-28 16:10 CDT — End-of-day paper audit

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market/account context:
- Alpaca endpoint verified as paper-only host `paper-api.alpaca.markets`.
- Read-only EOD audit only: account, positions, open orders, market clock, and today's fill activities inspected; no orders submitted.
- Paper account status ACTIVE; market closed at audit time; raw account identifiers and credentials redacted.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $750.08 / $800
- Penny exposure / target: about $27.77 / $200
- Total strategy exposure: about $777.84 / $1,000
- Unused strategy bankroll / cash drag: about $222.16
- Paper account long market value: about $777.84; paper buying power is much larger than managed strategy bankroll and was ignored for sizing.
- Open positions: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY.
- Open orders: 8 open OCO sell exits; each open position has a visible take-profit limit parent and protective stop-loss leg. No trailing-only coverage found.

Today's paper actions/fills:
- Target sells: XLV 1 @ about $150.02; BBAI 8 total @ about $4.58; IGV 1 @ about $95.20; OPEN 10 total @ about $4.94; XRT 1 @ about $85.50.
- Buys: VNQ 1 @ about $97.03; XLK 1 @ about $187.11.
- Audit job submitted no orders.

Exit manager / v3 target+stop audit:
- Target-limit coverage present: MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XLF $52.01, XLI $175.96, XLK $189.94, XLY $122.74.
- Protective stop coverage present: MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XLF $49.59, XLI $170.20, XLK $180.58, XLY $118.73.
- Missing targets: none. Missing stops: none. Trailing-only positions: none.
- Duplicate/excess sell-order risk: no obvious excess sell quantity; each OCO quantity matches the corresponding open position quantity.
- Weekend risk: Thursday EOD, not yet Friday; next paper run should reassess whether near-target positions need raised/replaced stops if momentum fades before the weekend.

Strategy utilization:
- Core is close to target without breaching the $800 bucket.
- Penny sleeve is very underused after BBAI/OPEN target exits, but this is acceptable because MVIS remains the only penny holding and prior runs rejected forced/chase re-entry.
- Cash drag around 22% is mostly from intentionally unused penny sleeve plus limited remaining core capacity; not a bad hold unless fresh high-quality penny or small-core setups appear.

Decision quality tags:
- SMART_SELL: XLV, BBAI, IGV, OPEN, and XRT target fills validated the v3 profit-capture structure.
- UNCERTAIN: VNQ and XLK buys need follow-through; both have verified OCO exits.
- SMART_HOLD: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLK, XLY held with complete target+stop coverage and no duplicate/excess sell quantity.
- SMART_HOLD: preserving penny cash after target fills instead of chasing immediate BBAI/OPEN re-entry.

Lessons / next run watchlist:
- V3 target+stop coverage is now materially better than earlier trailing-only state; keep verifying OCO parent/stop-leg visibility every run.
- Watch near-target XLY, TLT, XLI, XLK, and SCHD for fills or Friday stop-tightening decisions.
- Do not average down MVIS; either let the planned target/stop work or require a fresh, independent setup.
- Next action: NO_ACTION from this read-only audit; next trade-capable paper run may adjust only after fresh risk/market checks.

## 2026-05-29 08:49 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, and recent fills were checked read-only before decisions, then account/positions/orders were re-read immediately before placement and replacement. Credentials and raw account identifiers were not recorded.
- Market clock was open. Yahoo chart data showed broad risk-on/near-high conditions: SPY about 0.05% below its 5-day high, QQQ about 0.04% below, and IWM about 0.75% below.
- Recent fill observed before action: XLK target sold near $190.14, validating the v3 profit-capture plan and freeing core cash.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target after action: about $697.14 / $800
- Penny exposure / target after action: about $27.10 / $200
- Total strategy exposure: about $724.24 / $1,000
- Cash/unutilized strategy bankroll: about $275.76
- Cash-drag reason: XLK target fill reduced core exposure; only one new core ETF add was accepted. Remaining cash was preserved because penny candidates lacked a clean fresh catalyst/setup or would be chase re-entries after target exits, and several core candidates were weak/pullback or too close to recent target-fill/chase zones.
- Open positions after action: MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY.
- Open orders after verification: 8 OCO sell exits; every open position has visible target-limit profit capture and protective stop-loss coverage.

Candidates reviewed:
- Core: XBI selected as a liquid biotech ETF momentum/breakout add that fit remaining core capacity. IGV/XLK were strong but rejected as immediate target-fill chase risk. XLP/XLU/SLV/XLRE were weaker or below short averages. XHB/XME/ARKK were watchlist but not chosen to avoid over-deploying into Friday near-high risk. SPY/QQQ/IWM/SMH were too large for the small-bankroll whole-share structure.
- Penny: BBAI, OPEN, KULR, MVIS, GPRO reviewed. No new penny buy: BBAI/OPEN remained near recent highs after target exits and would be chase re-entries without a fresh catalyst; KULR remained volatile/extended; MVIS is already held and is not eligible for automatic averaging down; GPRO had liquidity but no strong catalyst confirmed.

Actions:
- Buys: XBI 1 share filled near $136.42 as a core swing add.
- Sells/fills: XLK 1 share target fill observed near $190.14 before action. No discretionary market sells submitted.
- Stop/limit updates: the initial XBI bracket entry left only visible target coverage after fill verification, so the target-only sell order was canceled and repaired with a full-position OCO exit: XBI target $138.85 + stop $134.15 for 1 share. Post-repair verification confirmed both target and stop were visible and sell quantity did not exceed the owned share.
- Holds: MVIS, SCHD, TLT, VNQ, XLF, XLI, and XLY held with verified target+stop OCO coverage.
- Rejections / NO_TRADE reasons: no additional core or penny add due to Friday near-high conditions, chase risk after target fills, and stricter penny-sleeve quality filters.

Exit manager:
- Weekly-high / profit-capture checks: all open positions show visible target-limit and stop-loss OCO coverage.
- Target-limit coverage present: MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XBI $138.85, XLF $52.01, XLI $175.96, XLY $122.74.
- Protective stop coverage present: MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XBI $134.15, XLF $49.59, XLI $170.20, XLY $118.73.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: added only one core position and preserved cash; next Friday/late-day run should consider stop raises only if momentum fades or positions remain near targets without filling.

Decision quality tags:
- SMART_SELL: XLK target fill — planned profit capture worked.
- UNCERTAIN: XBI buy — setup and sizing were policy-compliant with repaired target+stop coverage, but follow-through is not known yet.
- SMART_SELL: XBI exit repair — target-only bracket visibility was not accepted as sufficient; repaired to full OCO target+stop.
- SMART_HOLD: MVIS, SCHD, TLT, VNQ, XLF, XLI, XLY held with complete target+stop coverage and no duplicate/excess sell quantity.
- SMART_HOLD: no forced penny buy; preserved cash rather than chasing BBAI/OPEN or averaging down MVIS.

Lessons / next run watchlist:
- Bracket buys can again leave only visible target coverage after fill; treat this as incomplete until OCO target+stop is verified or repaired.
- Watch XBI for either target follow-through near $138.85 or stop risk at $134.15.
- Watch XLY/TLT/XLI/SCHD for target fills; watch VNQ/XLF for weakness; do not average down MVIS.
- Penny sleeve remains underused intentionally; require a fresh catalyst and clean exit plan before redeploying into BBAI/OPEN/KULR/GPRO.


## 2026-05-29 10:45 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, recent fills, and market data were checked read-only before decisions. Account, positions, and open orders were re-read immediately before placement/repair. Credentials and raw account identifiers were not recorded.
- Market clock was open. Broad ETF backdrop remained constructive/near highs from Yahoo chart data: SPY about 0.22% below its 5-day high, QQQ about 0.57% below, and IWM about 0.94% below. ARKK was near a 5-day high with strong short-term momentum and fit the remaining core capacity.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target after action: about $778.90 / $800
- Penny exposure / target after action: about $27.00 / $200
- Total strategy exposure: about $805.90 / $1,000
- Cash/unutilized strategy bankroll: about $194.10
- Cash-drag reason: core bucket is now near target without breaching the $800 cap; remaining unused cash is mostly the intentionally underused penny sleeve plus a small core reserve. Penny candidates did not pass strict catalyst/setup/exit-quality filters without chasing or averaging down.
- Open positions after action: ARKK, MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY.
- Open orders after verification: 9 OCO-style sell exits; every open position has visible target-limit profit capture and protective stop-loss coverage.

Candidates reviewed:
- Core: ARKK selected as a liquid high-beta ETF momentum add that fit the remaining core capacity and had a clear target+stop plan. XBI from the prior run remains held with OCO coverage. XLK/IGV/XRT/XLV were rejected as recent target-fill/chase risks or not currently held. XHB/XME exceeded remaining core capacity; XLP/XLU/SLV looked weaker or less urgent; SPY/QQQ/IWM were too large for the whole-share small-bankroll structure.
- Penny: MVIS, BBAI, OPEN, KULR, GPRO, SOUN, LUNR reviewed. No new penny buy: MVIS is already held and no averaging down is allowed; BBAI and OPEN were above/near the penny sleeve definition after recent target exits; KULR/GPRO lacked a clean enough catalyst/setup versus volatility; SOUN/LUNR did not fit the penny-stock price rule.

Actions:
- Buys: ARKK 1 share filled near $81.79 as a core swing add.
- Sells/fills: no discretionary sells by this run. Recent XLK target fill from the prior run remained noted as validation of v3 target capture.
- Stop/limit updates: ARKK bracket-style entry was submitted with target $83.29 and stop $78.94. Post-fill verification did not accept partial/uncertain leg visibility as sufficient, so ARKK sell coverage was repaired/replaced with a verified full-position OCO exit: target $83.29 + stop $78.94 for 1 share.
- Holds: MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, and XLY held with verified target+stop coverage.
- Rejections / NO_TRADE reasons: no penny add and no additional core add after ARKK due to bucket caps, Friday near-high conditions, chase risk, and strict exit-quality filters.

Exit manager:
- Weekly-high / profit-capture checks: all open positions show visible target-limit and stop-loss OCO coverage.
- Target-limit coverage present: ARKK $83.29, MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XBI $138.85, XLF $52.01, XLI $175.96, XLY $122.74.
- Protective stop coverage present: ARKK $78.94, MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XBI $134.15, XLF $49.59, XLI $170.20, XLY $118.73.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: added one liquid core position with immediate target+stop coverage; preserved cash rather than forcing penny exposure. Later Friday runs should consider stop raises only if momentum fades or targets remain just out of reach.

Decision quality tags:
- UNCERTAIN: ARKK buy — policy-compliant core add with verified target+stop coverage, but follow-through is not known yet.
- SMART_SELL: ARKK exit repair — full target+stop verification was enforced after fill rather than assuming bracket visibility was enough.
- SMART_HOLD: MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY held with complete target+stop coverage and no duplicate/excess sell quantity.
- SMART_HOLD: no forced penny buy; preserved cash rather than averaging down MVIS or chasing BBAI/OPEN/KULR/GPRO.

Lessons / next run watchlist:
- Watch ARKK for target follow-through near $83.29 or stop risk at $78.94.
- Watch XLY/TLT/XLI/SCHD/XBI for target fills; watch VNQ/XLF for weakness; do not average down MVIS.
- Penny sleeve remains underused intentionally; require a fresh catalyst and clean exit plan before redeploying into BBAI/OPEN/KULR/GPRO.

## 2026-05-29 12:52 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, recent fills, and Yahoo chart data were checked read-only. No order placement/replacement was needed, so no order-submission API call was made.
- Market clock was open; next close was 2026-05-29 16:00 ET. Broad ETF backdrop remained risk-on and near short-term highs: SPY about 0.26% below its 5-day high, QQQ about 0.59% below, and IWM about 0.86% below.
- Friday midday conditions favored protecting existing exposure rather than forcing new risk: core bucket was nearly full, while penny candidates were either above the penny price rule, extended, or lacked a clean fresh catalyst.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $779.58 / $800
- Penny exposure / target: about $26.96 / $200
- Total strategy exposure: about $806.54 / $1,000
- Cash/unutilized strategy bankroll: about $193.46
- Cash-drag reason: core bucket has only about $20 remaining capacity, below the normal $75-$150 core position guide; penny sleeve remains intentionally underused because available candidates did not pass strict fresh-setup/catalyst/volatility filters.
- Open positions: ARKK, MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY.
- Open orders: 9 OCO-style sell exits; every open position had visible target-limit profit capture and protective stop-loss coverage. No duplicate/excess sell quantity was detected.

Candidates reviewed:
- Core: ARKK and XBI remained strong and near 5-day highs but were already held with OCO exits. XLY/TLT/XLF were constructive and held. XLI/SCHD/VNQ showed mixed short-term readings, but still had target+stop coverage. XHB/XME had momentum but would breach the remaining core-cap logic; XLP/XLU/SLV were weak. SPY/QQQ/IWM were too large for this whole-share small-bankroll structure.
- Penny: MVIS held with existing target+stop and no averaging down. BBAI and OPEN were above the <$5 penny rule and were chase risks after recent target exits. KULR and GPRO had high volatility/large moves without a clean enough catalyst/exit-quality edge for Friday. SOUN/LUNR did not fit the penny-stock price rule.

Actions:
- Buys: none.
- Sells/fills: no new discretionary sells by this run; recent ARKK and XBI buys from prior runs remained open and protected.
- Stop/limit updates: none. Existing OCO coverage was verified and left unchanged to avoid unnecessary cancel/replacement risk.
- Holds: ARKK, MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY held with complete target+stop coverage.
- Rejections / NO_TRADE reasons: NO_NEW_BUY because the core bucket is effectively full, penny candidates did not meet strict filters, and Friday near-high conditions create chase/overnight-weekend risk.

Exit manager:
- Target-limit coverage present: ARKK $83.29, MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XBI $138.85, XLF $52.01, XLI $175.96, XLY $122.74.
- Protective stop coverage present: ARKK $78.94, MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XBI $134.15, XLF $49.59, XLI $170.20, XLY $118.73.
- Weekly-high / profit-capture checks: TLT and XBI were closest to targets and already had take-profit limits; XLY/SCHD/XLF remained constructive; VNQ and XLI were weaker/mixed but protected by existing stops.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: no new risk added; no stop raises were submitted because current OCO stops were intact and raising stops in a midday near-high tape was not clearly superior to preserving the existing target+stop plan.

Decision quality tags:
- SMART_HOLD: all existing positions held with complete OCO target+stop coverage and no duplicate/excess sell quantity.
- SMART_HOLD: no forced penny buy; preserved cash rather than chasing BBAI/OPEN/KULR/GPRO or averaging down MVIS.
- SMART_HOLD: no new core buy because remaining core capacity was too small for the normal position guide.
- UNCERTAIN: ARKK/XBI follow-through into their targets; Friday/weekend gap risk remains to be evaluated by the next run/EOD audit.

Lessons / next run watchlist:
- Watch TLT and XBI first because they are closest to planned targets.
- Watch ARKK and XLY for continuation versus reversal; both are risk-on/high-beta or consumer-sensitive exposures.
- Watch VNQ/XLI for weakness into stops; do not average down MVIS.
- Penny sleeve cash remains acceptable until a fresh, liquid, under-$5 setup with realistic target+stop math appears.

## 2026-05-29 14:45 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, recent fills, and Yahoo chart data were checked read-only before decisions. No placement/replacement was needed, so no order-submission API call was made.
- Market clock was open with about 15 minutes to the Friday close. Broad ETFs remained risk-on and near short-term highs: SPY about 0.14% below its 5-day high, QQQ about 0.36% below, and IWM about 0.88% below.
- Friday/near-close conditions favored preserving verified OCO exits rather than adding fresh weekend risk or cancel/replacing already valid coverage.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $778.01 / $800
- Penny exposure / target: about $27.05 / $200
- Total strategy exposure: about $805.06 / $1,000
- Cash/unutilized strategy bankroll: about $194.94
- Cash-drag reason: core bucket has only about $21.99 remaining capacity, below the normal $75-$150 core position guide; penny sleeve remains intentionally underused because expanded penny research did not produce a clean under-$5 setup with catalyst, liquidity/spread quality, and target+stop math.
- Open positions: ARKK, MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY.
- Open orders: 9 OCO-style sell exits; every open position had visible target-limit profit capture and protective stop-loss coverage. No duplicate/excess sell quantity was detected.

Candidates reviewed:
- Core: ARKK, XBI, SCHD, TLT, VNQ, XLF, XLI, XLY were already held with OCO coverage. XHB/XME showed momentum but would breach or crowd the small remaining core capacity; IGV/XLK/XRT/XLV were recent target-fill/chase risks; XLP/XLU/SLV were weaker; SPY/QQQ/IWM/SMH remained too large for this whole-share small-bankroll structure.
- Penny: base list MVIS, BBAI, OPEN, KULR, GPRO plus expanded symbols ESPR, SOBR, JBLU, LABT from high-volume/under-$5 penny-stock web/screener research. No buy: MVIS already held/no averaging down; BBAI and OPEN were above the <$5 penny rule at inspection or chase-risk after recent target exits; KULR was under $5 and liquid but extended/volatile near a wide 5-day range; GPRO was liquid but lacked a confirmed catalyst; ESPR was near its 5-day high but no fresh catalyst was confirmed; SOBR/LABT liquidity was too thin for this sleeve; JBLU was above the penny price rule.

Actions:
- Buys: none.
- Sells/fills: no new discretionary sells by this run; recent ARKK buy and prior XLK target fill remained noted.
- Stop/limit updates: none. Existing OCO coverage was verified and left unchanged to avoid unnecessary cancel/replacement risk minutes before the Friday close.
- Holds: ARKK, MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY held with complete target+stop coverage.
- Rejections / NO_TRADE reasons: no core add because core capacity is below normal position size; no penny add because quality/catalyst/spread-volatility filters failed even after expanded research.
- No-purchase tracking:
  - Core decision: `NO_CORE_BUY`; reason: cap effectively full / remaining capacity below normal position guide.
  - Penny decision: `NO_PENNY_BUY`; reason: no quality setup after expanded research; already held/no averaging down for MVIS; spread/volatility/catalyst concerns for alternatives.
  - Rolling pattern checked: core last 3 scheduled trading runs before this one were `CORE_BUY`, `CORE_BUY`, `NO_CORE_BUY`; after this run core consecutive no-buy count is about 2, last-5 count about 2. Penny last 3 were `NO_PENNY_BUY`, `NO_PENNY_BUY`, `NO_PENNY_BUY`; after this run penny consecutive no-buy count is about 4, last-5 pattern is all no-buy.
  - Research expanded this run? `yes`; `RESEARCH_EXPANDED` for penny sleeve because the under-target sleeve had a multi-run no-buy streak. Sources/screens used: Yahoo chart/volume scan of base list plus expanded web/screener candidates from current penny-stock watch articles and high-volume under-$5 names (ESPR, SOBR, JBLU, LABT), with liquidity/price/catalyst/exit-plan filters preserved.

Exit manager:
- Target-limit coverage present: ARKK $83.29, MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XBI $138.85, XLF $52.01, XLI $175.96, XLY $122.74.
- Protective stop coverage present: ARKK $78.94, MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XBI $134.15, XLF $49.59, XLI $170.20, XLY $118.73.
- Weekly-high / profit-capture checks: TLT was closest to target and just below its 5-day high; XBI/ARKK remained near highs; XLY/SCHD had gains but targets were still realistic. Existing OCO exits already paired profit capture with downside protection.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: no new risk added and no stop raises submitted; cancel/replacing valid OCO exits minutes before close was not clearly superior to preserving existing paired exits.

Decision quality tags:
- SMART_HOLD: all existing positions held with complete OCO target+stop coverage and no duplicate/excess sell quantity.
- SMART_HOLD: no new core buy because remaining capacity is too small for the policy guide.
- NO_PENNY_BUY: penny research was expanded, but no candidate met the strict fresh-catalyst/liquidity/spread/exit-plan gate.
- UNCERTAIN: ARKK/XBI follow-through and Friday/weekend gap risk.

Lessons / next run watchlist:
- Watch TLT first because it is closest to target; XBI and ARKK remain near-high continuation candidates but already have exits.
- Continue penny expansion next run if no fresh under-$5 catalyst appears; do not loosen the sleeve filters or average down MVIS.
- If Monday opens with target fills or stops, re-check exposure before redeploying; do not chase immediate re-entry after profitable target exits.

## 2026-05-29 16:11 CDT — End-of-day paper audit

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market/account context:
- Alpaca endpoint verified as paper-only host `paper-api.alpaca.markets`.
- Read-only EOD audit only: account, positions, open orders, market clock, and today's fill activities inspected; no orders submitted.
- Paper account status ACTIVE; market closed at audit time; raw account identifiers and credentials redacted.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target: about $778.13 / $800
- Penny exposure / target: about $27.00 / $200
- Total strategy exposure: about $805.13 / $1,000
- Unused strategy bankroll / cash drag: about $194.87
- Paper account long market value: about $805.13; paper buying power is much larger than managed strategy bankroll and was ignored for sizing.
- Open positions: ARKK, MVIS, SCHD, TLT, VNQ, XBI, XLF, XLI, XLY.
- Open orders: 9 open OCO sell exits; each open position has visible take-profit limit coverage and protective stop-loss leg. No trailing-only coverage found.

Today's paper actions/fills:
- Target sell: XLK 1 @ about $190.14.
- Buys: XBI 1 @ about $136.42; ARKK 1 @ about $81.79.
- Audit job submitted no orders.

Strategy utilization:
- Core is near target and appropriately not overfilled; remaining core capacity is about $21.87, below normal whole-share position size.
- Penny sleeve is underused at about $27 / $200, but this is acceptable because repeated penny no-buys were documented and research was expanded rather than forcing weak setups.
- Total utilization is about 80.5%; cash drag is mostly intentional penny-sleeve reserve plus small unusable core capacity.

No-purchase tracking:
- Core decision: `NO_CORE_BUY` for the latest trade run; reason: core bucket effectively full / remaining capacity below normal position guide. Consecutive core no-buy streak estimated at 2 scheduled runs after today's earlier XBI and ARKK core buys.
- Penny decision: `NO_PENNY_BUY`; reason: no clean under-$5 setup with fresh catalyst, liquidity/spread quality, and target+stop math; MVIS already held/no averaging down.
- Penny no-buy streak is at least 4 consecutive today and about 5 across recent scheduled runs; the 14:45 run explicitly reported `RESEARCH_EXPANDED` and listed expanded penny candidates/sources, satisfying the escalation rule.

Exit manager / v3 target+stop audit:
- Target-limit coverage present: ARKK $83.29, MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XBI $138.85, XLF $52.01, XLI $175.96, XLY $122.74.
- Protective stop coverage present: ARKK $78.94, MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XBI $134.15, XLF $49.59, XLI $170.20, XLY $118.73.
- Missing targets: none. Missing stops: none. Trailing-only positions: none.
- Duplicate/excess sell-order risk: no obvious excess sell quantity; each OCO quantity matches the corresponding open position quantity.
- Weekend risk: Friday close passed with no new late-day risk added after 10:45; preserving valid OCO exits was safer than cancel/replacing minutes before close.

Decision quality tags:
- SMART_SELL: XLK target fill; v3 profit capture worked.
- UNCERTAIN: XBI and ARKK buys; both are policy-compliant and have verified target+stop coverage, but follow-through is not known yet.
- SMART_HOLD: all current positions held with complete OCO target+stop coverage and no duplicate/excess sell quantity.
- NO_PENNY_BUY: valid no-buy because research expanded and still did not find a clean penny setup; do not force the sleeve.

Lessons / next run watchlist:
- Monday should re-check for any target/stop fills before redeploying cash; do not chase immediate re-entry after profitable exits.
- Continue expanded penny research if the sleeve remains under-target, but keep the catalyst/liquidity/spread/exit-plan gates strict.
- Next action from this read-only audit: NO_ACTION.


## 2026-06-01 08:51 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, recent fills, and Yahoo chart data were checked read-only before decisions. Account/positions/orders were re-read immediately before the IGV order. Credentials and raw account identifiers were not recorded.
- Market clock was open. Broad ETFs were mixed: SPY and QQQ remained near 5-day highs, but IWM lagged and several existing core holdings had pulled back enough to trigger planned stop exits.
- Recent fills observed before/around action: XBI sold by protective stop near $134.09 and XLY sold by protective stop near $118.74, reducing core exposure; IGV then filled as a new core replacement buy near $104.68.

Portfolio snapshot:
- Strategy bankroll: $1,000
- Core exposure / target after action: about $620.16 / $800
- Penny exposure / target after action: about $27.59 / $200
- Total strategy exposure: about $647.75 / $1,000
- Cash/unutilized strategy bankroll: about $352.25
- Cash-drag reason: stop exits reduced core exposure; only one clean core replacement was accepted because the tape was mixed after stop-outs. Penny sleeve remains intentionally underused because expanded penny candidates still failed fresh-catalyst/liquidity/spread/exit-quality filters.
- Open positions after action: ARKK, IGV, MVIS, SCHD, TLT, VNQ, XLF, XLI.
- Open orders after verification: 8 OCO-style sell exits; every open position has visible target-limit profit capture and protective stop-loss coverage. No duplicate/excess sell quantity detected.

Candidates reviewed:
- Core: IGV selected as one-share software ETF replacement exposure because it was liquid, near its 5-day high, above short intraday averages, and fit the normal $75-$150 core guide with a clear target+stop plan. XLK was strong but larger than the normal guide and a recent target-fill/chase risk; XBI and XLY had just stopped out; IWM/XRT/VNQ/XLI/XLF/SCHD were weaker or already held; SPY/QQQ were too large for this small-bankroll whole-share structure.
- Penny: base/expanded review included MVIS, BBAI, OPEN, KULR, GPRO, ESPR, SOBR, LABT, GRAB, and VXRT, plus current web/screener context from Yahoo most-active penny stocks and under-$5 watch/catalyst sources. No new penny buy: MVIS already held/no averaging down; BBAI and OPEN were above the <$5 sleeve definition at inspection; KULR was under $5 and liquid but extended/volatile; GPRO was weak; ESPR was near highs but lacked enough confirmed fresh catalyst edge; SOBR/LABT/VXRT had liquidity/quality concerns; GRAB was liquid under $5 but did not have a clean enough short-term catalyst/target+stop edge.

Actions:
- Buys: IGV 1 share filled near $104.68 as a core swing add.
- Sells/fills: XBI 1 share sold by protective stop near $134.09; XLY 1 share sold by protective stop near $118.74. No discretionary market sells submitted by this run.
- Stop/limit updates: IGV bracket entry initially left only a visible target-limit sell, so the run canceled that incomplete target-only coverage, re-read open orders, and repaired it with full-position OCO target+stop coverage: IGV target $106.30 + stop $101.55 for 1 share. Verification confirmed both target and stop coverage.
- Holds: ARKK, MVIS, SCHD, TLT, VNQ, XLF, and XLI held with existing OCO target+stop coverage.
- Rejections / NO_TRADE reasons: no additional core add because the run avoided overreacting immediately after stop-outs; no penny add because the expanded penny scan still did not produce a clean setup.
- No-purchase tracking:
  - Core decision: `CORE_BUY`; reason: XBI/XLY stop fills lowered core exposure and IGV passed the liquidity/setup/size/target+stop gate.
  - Penny decision: `NO_PENNY_BUY`; reason: no quality setup after expanded research; already held/no averaging down for MVIS; BBAI/OPEN above penny rule; KULR/ESPR/GPRO/SOBR/LABT/GRAB/VXRT failed catalyst, spread/liquidity, volatility, or exit-quality filters.
  - Rolling pattern checked: core last 3 scheduled trading runs including this one are estimated `NO_CORE_BUY`, `NO_CORE_BUY`, `CORE_BUY`; core last 5 are estimated `CORE_BUY`, `CORE_BUY`, `NO_CORE_BUY`, `NO_CORE_BUY`, `CORE_BUY`. Penny last 3 and last 5 scheduled trading runs are all `NO_PENNY_BUY`.
  - Research expanded this run? `yes`; `RESEARCH_EXPANDED` for penny sleeve because the sleeve remains far below target with a 5+ no-buy streak. Sources/screens used: Yahoo chart/volume scan of base penny list, Yahoo most-active penny-stock screener result, current under-$5 watch/catalyst web results, and expanded symbols KULR, GPRO, ESPR, SOBR, LABT, GRAB, VXRT. Expansion did not loosen risk gates.

Exit manager:
- Target-limit coverage present: ARKK $83.29, IGV $106.30, MVIS $0.66, SCHD $32.84, TLT $85.98, VNQ $98.47, XLF $52.01, XLI $175.96.
- Protective stop coverage present: ARKK $78.94, IGV $101.55, MVIS $0.5786, SCHD $31.60, TLT $82.31, VNQ $93.61, XLF $49.59, XLI $170.20.
- Weekly-high / profit-capture checks: IGV was closest to a fresh near-high continuation target and received immediate OCO coverage. ARKK/VNQ/XLI remained below entry or mixed but protected. TLT/SCHD/XLF were held with existing target+stop plans. MVIS remains a no-average-down penny hold.
- Target-limit coverage missing after this run: none.
- Protective stops missing after this run: none.
- Weekend risk actions: none; Monday morning run.

Decision quality tags:
- UNCERTAIN: IGV buy — policy-compliant replacement core exposure with verified target+stop coverage, but follow-through is unknown.
- SMART_SELL: IGV exit repair — target-only bracket visibility was rejected and repaired to full OCO target+stop.
- SMART_HOLD: ARKK, MVIS, SCHD, TLT, VNQ, XLF, XLI held with complete OCO target+stop coverage and no duplicate/excess sell quantity.
- NO_PENNY_BUY: penny research remained expanded, but no candidate met the strict fresh-catalyst/liquidity/spread/exit-plan gate.
- UNCERTAIN: XBI and XLY stop exits reduced risk but also confirm some Friday risk-on exposure weakened at Monday open.

Lessons / next run watchlist:
- Watch IGV for target follow-through near $106.30 or stop risk at $101.55; verify its OCO legs remain paired next run.
- Re-check whether XBI/XLY stop-outs were isolated weakness or a broader momentum fade before replacing more core exposure.
- Continue expanded penny research, but do not force the sleeve or average down MVIS.

## 2026-06-01 10:56 CDT — Scheduled paper run v3 target+stop

Context notes read:
- Trading Automation - Discord Thread Project Note.md
- Trading Strategy Rules.md
- Trading Run Log.md
- Buy Sell Lessons.md

Market context:
- Endpoint verified as Alpaca paper host `paper-api.alpaca.markets`; account, positions, open orders, market clock, recent fills, and Yahoo chart data were checked read-only before decisions. Account/positions/orders were re-read immediately before new entries and before exit placement. Credentials and raw account identifiers were not recorded.
- Market clock was open. Broad ETF backdrop was mixed-to-constructive: SPY about 0.17% below its 5-day high, QQQ about 0.17% below its 5-day high, while IWM lagged about 1.59% below its 5-day high.
- Recent fill observed before action: IGV sold at its planned target near $106.30 after the prior run's buy/repair, validating the v3 target-capture structure.



## 2026-08-13 08:48 CDT — Scheduled paper run — Balanced v4.1

### Notes and safety checks
- Read at run start: `Trading Automation - Discord Thread Project Note.md`, `Trading Strategy Rules.md`, `Trading Run Log.md`, and `Buy Sell Lessons.md`.
- PAPER-ONLY gate passed: normalized the configured base URL and verified host `paper-api.alpaca.markets` before account, positions, nested open OCO orders, market clock, recent fills, asset status, fresh IEX quotes, and daily-bar reads. Account was ACTIVE and regular trading open. No credentials or account identifiers were recorded.

### Portfolio and exit manager
- Fixed managed bankroll: `$1,000`; larger paper buying power ignored. Final core exposure: `$326.0 / $800` (XLE `$121.42`, XLF `$116.37`, XLU `$88.18`). Penny exposure: `$44.52 / $200` (ESPR). Total managed exposure: `$370.49`; cash drag: `$629.51`.
- Fills since last run: XLE 2 bought Aug. 12 at `$60.70`; this run bought XLU 2 at `$44.13`. No current target or protective-stop fill occurred.
- XLE 2 has verified GTC OCO target/stop `$62.30 / $59.70`; XLF 2 has verified GTC OCO `$58.75 / $56.50`; XLU 2 has verified GTC OCO `$44.79 / $43.69`. Parent and held-leg quantities match reserved shares. No trailing-only, duplicate, or excess sell quantity was found.
- Coverage warning: ESPR 14 remains available with no visible target or stop. Alpaca reports `inactive` / non-tradable and its quote remains stale. No unsupported repair or sale was attempted.

### Researcher → trader → confirmer
- Broad tape was firm near five-session highs (SPY/QQQ at or near their five-day highs; IWM close). The July PPI release had already occurred; the scan avoided extended technology/materials names and did not treat incomplete early-session volume as a full-day rejection.
- XLU showed tight displayed spread, positive five-session momentum, and was just below its five-day high; 2 shares fit the `$75–$150` core guide. Entry `$44.13`, target `$44.79`, stop `$43.69`: planned reward/risk about `1.5:1`.
- Independent risk gate approved one B+ core add only. New penny risk was rejected while inactive/uncovered ESPR remains unresolved; no biotech/FDA-binary candidate was considered.

### Actions and verification
- BUY: XLU 2 shares filled at `$44.13` (paper; order reference redacted).
- Immediately re-read position/order state and submitted full-position GTC paper OCO: target-limit `$44.79`, held protective stop `$43.69`, quantity 2. Verification confirmed the OCO parent `new` and stop leg `held`; no duplicate XLU sell coverage exists.
- No sell, cancellation, or exit replacement was submitted. Existing XLE/XLF OCO coverage was preserved.

### Decision tags
- `SMART_BUY` / `UNCERTAIN`: XLU is a policy-compliant B+ core rebuild with a verified GTC OCO exit; follow-through is unknown.
- `SMART_HOLD`: XLE and XLF retain valid paired protection without churn.
- `NO_PENNY_BUY`; `UNCERTAIN / COVERAGE_WARNING`: ESPR remains inactive/non-tradable and uncovered.

### Next-run priorities
- Re-read fills, positions, and all nested OCO legs; verify XLU/XLE/XLF coverage remains paired.
- Seek only a broker-supported/human-reviewed resolution for inactive ESPR. Keep new penny exposure paused while it remains unresolved.
- With exposure below `$500`, continue broad core discovery, but add only a fresh B+ or better liquid setup with event review, time-appropriate volume/relative strength, `1.5:1+` reward/risk, and immediate verified GTC OCO coverage.

Notes updated: appended this run record. `Buy Sell Lessons.md` was read and not changed; no new durable lesson was identified. No secrets or account identifiers were written.

## 2026-08-13 17:11 EDT — End-of-day paper audit — Balanced v4.1

### Notes and safety checks
- Read: `Trading Automation - Discord Thread Project Note.md`, `Trading Strategy Rules.md`, `Trading Run Log.md`, and `Buy Sell Lessons.md`.
- READ-ONLY audit: configured endpoint normalized and verified as `paper-api.alpaca.markets` before account, positions, nested open OCO orders, market clock, and today’s fill activity were read. No order was submitted, canceled, replaced, or modified. Account status was ACTIVE; market closed.

### Managed strategy snapshot
- Fixed strategy bankroll: `$1,000`; paper buying power was ignored for strategy sizing.
- Core exposure: `$326.38 / $800` — XLE `$122.08`, XLF `$116.40`, XLU `$87.90`.
- Penny exposure: `$44.52 / $200` — ESPR `$44.52`.
- Total managed exposure: `$370.90 / $1,000`; cash drag: `$629.10` (62.9%), materially below the Balanced v4.1 `$500` rebuild threshold.
- Open-position unrealized P/L: approximately `+$6.02` (XLE `+$0.68`, XLF `+$5.14`, XLU `-$0.36`, ESPR `+$0.56`). Today’s activity had one XLU buy order filled in two partial-fill events at `$44.13`; no closing fill/realized P/L was observed today.

### Exit coverage and order integrity
- Verified full-position GTC OCO target + protective-stop coverage: XLE 2 (`$62.30 / $59.70`), XLF 2 (`$58.75 / $56.50`), XLU 2 (`$44.79 / $43.69`). OCO parent and held stop-leg quantities match each position; no trailing-only coverage, duplicate orders, or excess sell quantity was found.
- Coverage warning: ESPR 14 shares have no visible target or protective stop. Prior state remains `inactive` / non-tradable with a stale quote, so normal OCO repair is not safely available. No unsupported order or duplicate sell coverage was attempted.
- Exit pricing: XLE/XLF/XLU targets and stops remain live GTC and not stale relative to current prices. Friday/weekend review is due at the next main run; this Thursday EOD audit made no changes.

### Balanced v4.1 compliance and next-run recommendation
- Compliant: paper-only endpoint, no averaging down, no same-day target re-entry, and no immediate stop-out replacement observed. Today’s only fill was a core buy; no new biotech/FDA-binary penny risk was added.
- Cash drag is excessive under Balanced v4.1 because managed exposure is `$370.90`, below `$500`. Next main run should broaden core research and consider at most one fresh B+ or better liquid core setup (plus an eligible non-biotech penny only if the sleeve filters and exit plan pass), with `1.5:1+` reward/risk and immediate verified GTC OCO coverage. Prioritize broker-supported/human-reviewed resolution of inactive, uncovered ESPR before any new penny exposure.

Notes updated: appended this EOD audit to `Trading Run Log.md`. `Buy Sell Lessons.md` was read but not changed; no additional reusable lesson beyond the existing inactive-asset/coverage guidance was identified. No secrets or account identifiers were recorded.

## 2026-08-14 07:31 CDT — Relative-Value Research (read-only lane v1)

### Scope and data quality
- READ-ONLY research only. No Alpaca account endpoint was needed or called; no brokerage order was submitted, canceled, replaced, or modified.
- Pre-market research window. Public web context was available, but direct daily-price pulls from public Yahoo and Stooq endpoints were rate-limited/unavailable. Therefore this is a trigger-defined watchlist, **not** a claim of a verified current spread dislocation. Revalidate both legs with synchronized regular-session daily/5-minute data before any future human-approved paper test.

### Market context
- The latest available broad sector context is uneven rather than a single uniform risk-on signal: Yahoo sector data showed strong YTD leadership in technology, industrials, and energy, while financials and consumer cyclicals were materially weaker; the displayed daily heatmap had energy and health care strong while technology and real estate were weak. Schwab’s July 31 sector outlook favored financials/health care/industrials, rated technology neutral, and least favored real estate. These sources are contextual, not execution prices.
- Current strategy context from the Aug. 13 EOD audit: managed exposure was low (about $371 of $1,000), but this lane has no authority to use that capacity. Existing XLE/XLF/XLU positions and ESPR’s inactive/uncovered status make sector research especially useful, not a basis to add or alter positions.

### Relative-value relationships to watch
1. **XLF vs KBE/KRE — diversified financials versus banks/regional banks**
   - Thesis: If XLF holds broad financial strength while KBE/KRE lag, the divergence can distinguish capital-markets/insurer leadership from a bank-credit/rate-sensitive move.
   - Confirmation trigger: 5- and 20-session relative-return ratio (XLF divided by an equal-weight KBE/KRE proxy) reaches a 20-session extreme, then reverses for two closes with the lagging leg reclaiming its 5-day average on above-average volume.
   - Invalidation: New bank-specific credit/regulatory shock, a widening ratio on rising volume, or divergence driven solely by one mega-cap financial.
   - Suggested future paper-test: Long-only rotation comparison—hold the stronger liquid ETF or use a cash-versus-one-ETF benchmark; do not short the weak leg. Fixed 5–10 trading-day review, small defined notional, and prewritten exit threshold.
   - Risks / not live-ready: constituent overlap is imperfect, KRE has regional-bank concentration, and the required synchronized ratio/z-score has not been calculated from a verified feed.

2. **XLV vs IHF — broad health care versus providers/services**
   - Thesis: A persistent IHF underperformance versus XLV may be policy/reimbursement risk rather than a broad defensive-health-care signal; a reversal can identify normalization without selecting single names.
   - Confirmation trigger: IHF/XLV 20-session z-score below -1.5 followed by two sessions of relative outperformance and IHF volume above its 20-day median.
   - Invalidation: CMS/reimbursement, managed-care, or regulatory headline creates a new fundamental repricing.
   - Suggested future paper-test: One-leg long IHF only after confirmation, benchmarked against XLV and capped to a single small ETF unit; 1.5:1 reward/risk with fixed stop/target.
   - Risks / not live-ready: policy headlines gap this group, correlations change abruptly, and no fresh calculated z-score or event-calendar check is attached.

3. **QQQ vs XLK/IGV — mega-cap Nasdaq versus technology/software breadth**
   - Thesis: QQQ strength with IGV weakness can mean index concentration is masking software breadth deterioration; IGV recovery relative to QQQ may be a slower breadth-repair signal.
   - Confirmation trigger: IGV/QQQ and XLK/QQQ both stop declining, then IGV closes above its 5-day average with a positive 3-day relative return while QQQ remains above its 20-day average.
   - Invalidation: major AI/semiconductor earnings or index-heavy constituent shock drives QQQ independently of software.
   - Suggested future paper-test: Long-only IGV continuation/reversion test after the dual confirmation; no paired short QQQ. Time stop after 5 sessions if relative recovery fails.
   - Risks / not live-ready: sector overlap and valuation sensitivity are high; timing around major tech earnings is critical; today’s ratios were not independently refreshed.

4. **XHB vs VNQ/XLRE — homebuilders versus real-estate owners**
   - Thesis: Homebuilders and REITs respond differently to rates, supply, and housing demand. A large XHB premium versus VNQ/XLRE can either persist with supply scarcity or mean-revert if rate expectations ease broadly.
   - Confirmation trigger: XHB/VNQ 20-session ratio exceeds a 20-session high, then reverses below its 5-day average while VNQ and XLRE both reclaim their 5-day averages.
   - Invalidation: mortgage-rate spike, adverse housing data, or a REIT-specific financing stress event.
   - Suggested future paper-test: Prefer a long-only VNQ or XLRE mean-reversion test only after both REIT proxies confirm; use XHB solely as the signal comparator.
   - Risks / not live-ready: VNQ and XLRE are not identical, real estate is rate-sensitive and less favored in the cited outlook, and no current spread statistic has been verified.

5. **XLE vs SPY — energy leadership versus broad-market beta**
   - Thesis: Energy’s stronger available YTD/daily context may be a durable inflation/supply-demand regime or an overextended oil-beta move. The XLE/SPY ratio is a slow regime filter, not an arbitrage spread.
   - Confirmation trigger: Ratio remains above its 20-day average, but require an XLE pullback that holds the 20-day average and then a close back above the 5-day high; reject a one-day commodity-news spike.
   - Invalidation: oil-price reversal, geopolitical de-escalation, or ratio breaks its 20-day average on higher relative volume.
   - Suggested future paper-test: Existing-position review or one small long-only XLE continuation test after a pullback/reclaim, with a fixed 5–10 day horizon. No short-SPY hedge.
   - Risks / not live-ready: commodity gaps dominate technicals, current portfolio already has XLE exposure, and a fresh oil/event check plus verified ratio data are required.

6. **KBE vs KRE — large-bank versus regional-bank internal divergence**
   - Thesis: KBE outperforming KRE can flag regional funding/credit stress; KRE stabilization relative to KBE may be a more focused mean-reversion signal than XLF alone.
   - Confirmation trigger: KRE/KBE reaches a 20-session low, then records two relative-up closes with no adverse regional-bank news and normal-to-improving KRE liquidity.
   - Invalidation: deposit/credit deterioration, earnings guidance reset, or renewed stress in regional-bank funding indicators.
   - Suggested future paper-test: Observation-only first; if eventually approved, a tiny long-only KRE test after confirmation with a hard stop and no averaging down.
   - Risks / not live-ready: event risk is asymmetric, KRE concentration is material, and this is not market-neutral without a short KBE leg (which this lane prohibits).

### Conclusion
- **NO_TRADE / RESEARCH_ONLY.** No trade proposal, paper order, or portfolio adjustment was made. These are slower, long-only-compatible relative-strength and mean-reversion hypotheses for a future separately human-approved paper-test lane—not live trading and not latency arbitrage.
- Next research run: obtain a reliable synchronized daily-bar source, calculate 20-session ratios/z-scores and volume confirmation for the six relationships, screen scheduled macro/sector events, and retain only relationships with a currently verified trigger.

Notes updated: appended this read-only relative-value research record. No secrets, account identifiers, or credentials were recorded.

## 2026-08-14 08:47 CDT — Scheduled paper run — Balanced v4.1

### Notes and safety checks
- Read at run start: `Trading Automation - Discord Thread Project Note.md`, `Trading Strategy Rules.md`, `Trading Run Log.md`, and `Buy Sell Lessons.md`.
- PAPER-ONLY gate passed: configured base URL was normalized and its host verified as `paper-api.alpaca.markets` before account, positions, nested open OCO orders, market clock, today’s fills, and fresh IEX quotes/bars were read. Account status was ACTIVE; regular session was open. No credentials or account identifiers were recorded.

### Portfolio and exit manager
- Fixed managed bankroll: `$1,000`; larger paper buying power ignored. Core exposure: `$328.22 / $800` (XLE `$123.42`, XLF `$116.40`, XLU `$88.40`). Penny exposure: `$44.52 / $200` (ESPR). Total managed exposure: `$372.74`; cash drag: `$627.26`.
- Fills since the Aug. 13 EOD audit: none. No fill occurred today at this run time.
- XLE 2 has verified GTC OCO target/stop `$62.30 / $59.70`; XLF 2 has verified GTC OCO `$58.75 / $56.50`; XLU 2 has verified GTC OCO `$44.79 / $43.69`. Each OCO parent/held-stop quantity matches reserved shares. No trailing-only, duplicate, or excess sell quantity was found.
- Coverage warning: ESPR 14 remains available with no visible target or stop. The prior state is inactive/non-tradable with a stale quote; no unsupported repair or sale was attempted.

### Researcher → trader → confirmer
- Market data at about 09:47 ET was constructive: SPY `+0.65%`, QQQ `+1.75%`, IWM `+1.20%`, KRE `+2.62%`, and XLP `+1.32%` over the available five-session window; all except the weaker XLB/XLV/XRT set were close to five-session highs, with tight displayed spreads on liquid ETF candidates. Partial early-session volume was not compared mechanically to full-day volume.
- Core candidates: KRE had the strongest short-term momentum but would add financial-sector overlap to XLF. XLP had a tight spread and constructive five-session trend, but a scheduled 10:00 ET consumer-sentiment release was imminent. XLI/VNQ were constructive but either higher-priced or less compelling; XLB/XLV/XRT were weak versus the five-session window. No core candidate cleared the fresh-event and diversification gate at the decision time.
- Penny decision: no new penny scan/entry while ESPR is inactive and uncovered. No biotech/FDA-binary risk was considered.
- Independent risk gate: reject new orders. Although exposure is below `$500`, entering a fresh position immediately before a scheduled high-impact macro release would not meet the no-obvious-event-risk gate. Existing exits were valid and were left unchanged.

### Actions
- No paper order submitted, canceled, replaced, or modified.
- Holds: XLE, XLF, and XLU with verified paired GTC OCO profit-target and protective-stop coverage. ESPR remains a broker-status coverage warning only.
- No-purchase tracking: Core decision `NO_CORE_BUY` — imminent 10:00 ET macro event plus candidate overlap/quality constraints. Penny decision `NO_PENNY_BUY` — inactive/uncovered ESPR requires resolution first; no new penny risk added. Research remains broadened because both buckets are materially under target.

### Decision tags
- `SMART_HOLD`: XLE, XLF, and XLU retained valid GTC OCO coverage without churn.
- `NO_CORE_BUY`: under-deployment alone did not override imminent event risk and portfolio-fit gates.
- `NO_PENNY_BUY`; `UNCERTAIN / COVERAGE_WARNING`: ESPR remains inactive/non-tradable and uncovered.

### Next-run priorities
- Re-read fills, positions, and all nested OCO legs; verify XLE/XLF/XLU coverage stays paired.
- Resume broadened core research after the macro release; if exposure remains below `$500`, consider at most one fresh B+ liquid, diversified core setup with `1.5:1+` reward/risk and immediate verified GTC OCO coverage.
- Seek only a broker-supported/human-reviewed resolution for inactive ESPR; keep new penny exposure paused while unresolved.

Notes updated: appended this run record. `Buy Sell Lessons.md` was read and not changed; no new durable lesson was identified. No secrets or account identifiers were written.



## 2026-08-14 16:12 CDT — End-of-day paper audit — Balanced v4.1

### Notes and safety checks
- Read: `Trading Automation - Discord Thread Project Note.md`, `Trading Strategy Rules.md`, `Trading Run Log.md`, and `Buy Sell Lessons.md`.
- READ-ONLY audit: normalized the configured endpoint and verified host `paper-api.alpaca.markets` before reading account, positions, nested open OCO orders, market clock, today’s fills, and available IEX quotes. Account status was ACTIVE; the market was closed. No order was submitted, canceled, replaced, or modified.

### Managed strategy snapshot
- Fixed strategy bankroll: `$1,000`; larger paper buying power was ignored. Core exposure: `$328.48 / $800` (XLE `$123.74`, XLF `$116.30`, XLU `$88.44`). Penny exposure: `$44.52 / $200` (ESPR). Total: `$373.00`; cash drag: `$627.00` (62.7%), below the Balanced v4.1 `$500` rebuild threshold.
- Open-position unrealized P/L: approximately `+$8.12` (XLE `+$2.34`, XLF `+$5.04`, XLU `+$0.18`, ESPR `+$0.56`). Account equity change versus prior close was approximately `+$1.76`; it is not a managed-strategy realized-P/L calculation. No fills or realized closing activity were observed today.

### Exit coverage and integrity
- Verified GTC OCO target + protective-stop coverage: XLE 2 (`$62.30 / $59.70`), XLF 2 (`$58.75 / $56.50`), and XLU 2 (`$44.79 / $43.69`). Each target parent and held stop leg reserve the same owned quantity as one OCO structure; this is not duplicate coverage. No trailing-only position, duplicate/excess sell quantity, expired TIF, or obviously stale/unrealistic liquid-ETF exit was found.
- Coverage warning: ESPR 14 has no visible target or protective stop. Its available quote remains stale and its prior broker state is inactive/non-tradable; ordinary OCO repair is not safely available. No unsupported order or duplicate sell coverage was attempted.
- Friday/weekend review: XLE/XLF/XLU carry GTC paired exits into the weekend. ESPR remains the sole uncovered weekend-risk exception.

### Balanced v4.1 compliance and recommendation
- Compliant: paper-only endpoint, no buys/sells today, no averaging down, no same-day target re-entry, no stop-out replacement, and no new biotech/FDA-binary penny risk. The `0` fills today require no fill classification.
- Cash drag is excessive under Balanced v4.1. Next main run should continue broadened research and may consider at most one fresh, diversified B+ or better liquid core setup while exposure is below `$500`; any eligible non-biotech penny candidate remains conditional on strict sleeve, liquidity/spread, catalyst, reward/risk, and immediate GTC OCO gates. Prioritize broker-supported/human-reviewed resolution of inactive/uncovered ESPR before adding penny risk.

Notes updated: appended this EOD audit to `Trading Run Log.md`. `Buy Sell Lessons.md` was read and not changed because the inactive-asset and OCO-coverage lessons already cover this reusable condition. No secrets or account identifiers were recorded.

## 2026-08-17 07:30 CDT — Relative-Value Research (read-only lane v1)

### Scope and data quality
- **READ-ONLY / RESEARCH_ONLY.** No Alpaca endpoint was called and no brokerage order was submitted, canceled, replaced, or modified.
- Public sources supplied only delayed/last-available context, predominantly through Aug. 14. No synchronized intraday/daily-bar feed was available for calculating current ratios, z-scores, or correlations; every item below is a conditional watch hypothesis, not a verified dislocation.

### Market context
- The latest available data show a mixed, rotation-prone backdrop rather than a uniform trend: Yahoo sector context showed strong YTD technology, industrial, and energy leadership, while the latest displayed session had energy and health care stronger and technology/real estate weaker. Yahoo’s Aug. 14 quotes put XLE near its 52-week high, XLK/XLV below their displayed 52-week highs, and VNQ modestly ahead of its real-estate category YTD.
- Technology breadth warrants special caution: IGV showed only 1.51% YTD return versus a 13.51% technology-category figure as of Aug. 14, making software-versus-index divergence a live research question, not proof of a mean-reversion entry.

### Relative-value relationships to watch
1. **XLF vs KBE/KRE — broad financials versus banks/regional banks**
   - Thesis: Compare broad financial leadership with bank-sensitive leadership; KBE’s reported stronger one-year return than XLF also implies higher volatility, so a reversal needs confirmation rather than a simple catch-up assumption.
   - Confirmation trigger: 20-session XLF / average(KBE,KRE) ratio reaches a rolling extreme, then reverses for two daily closes while the lagging leg reclaims its 5-day average on above-median volume.
   - Invalidation: bank-credit, funding, or regulatory headline; ratio expansion on rising volume; single mega-cap driving XLF.
   - Suggested future paper-test: long-only stronger-leg continuation or confirmed laggard-recovery test, one small ETF unit, 5–10-session time stop, predefined 1.5:1+ reward/risk. No short leg.
   - Risks / not live-ready: constituent overlap and KRE concentration; no synchronized ratio, macro-event screen, or current volume test was verified.

2. **XLV vs IHF — diversified health care versus providers/services**
   - Thesis: The latest session’s health-care strength can conceal provider-specific reimbursement/policy sensitivity; IHF relative stabilization would be more informative than broad XLV strength alone.
   - Confirmation trigger: IHF/XLV 20-session z-score below -1.5, followed by two positive relative closes, IHF above its 5-day average, and volume above its 20-day median.
   - Invalidation: reimbursement, managed-care, tariff, or regulatory repricing.
   - Suggested future paper-test: long-only IHF after confirmation, benchmarked to XLV, fixed stop/target and five-session time stop.
   - Risks / not live-ready: headline-gap risk and no current z-score/event-calendar validation.

3. **QQQ vs XLK/IGV — Nasdaq concentration versus broad technology/software breadth**
   - Thesis: IGV’s reported YTD lag versus its technology category makes a QQQ/XLK strength–IGV weakness split useful for tracking whether index leadership is masking software weakness.
   - Confirmation trigger: IGV/QQQ and XLK/QQQ stop declining; IGV posts a positive 3-session relative return and closes above its 5-day average while QQQ remains above its 20-day average.
   - Invalidation: major AI, semiconductor, or index-heavy earnings shock that moves QQQ independently.
   - Suggested future paper-test: small long-only IGV recovery/continuation test after the dual signal; exit if relative recovery fails within five sessions.
   - Risks / not live-ready: high overlap, valuation/earnings sensitivity, and absent verified ratio and earnings-calendar data.

4. **XHB vs VNQ/XLRE — homebuilders versus listed real estate**
   - Thesis: Housing-supply/rate dynamics can keep homebuilders strong while REITs lag; synchronized recovery in VNQ and XLRE after an XHB premium reversal is the relevant slower signal.
   - Confirmation trigger: XHB/VNQ ratio makes a 20-session high, drops below its 5-day average, and both VNQ and XLRE reclaim their own 5-day averages.
   - Invalidation: mortgage-rate spike, housing-data deterioration, or REIT financing stress.
   - Suggested future paper-test: long-only VNQ or XLRE after both proxies confirm; XHB is signal-only. Use a fixed 5–10-session review and hard stop.
   - Risks / not live-ready: VNQ/XLRE are not identical exposures; real estate remains rate-sensitive and no current spread statistic is verified.

5. **XLE vs SPY — energy regime versus broad beta**
   - Thesis: Energy’s strong YTD/daily context and proximity to its displayed 52-week high make XLE/SPY a regime filter; it is not an arbitrage spread and must survive an orderly pullback before a continuation hypothesis is credible.
   - Confirmation trigger: XLE/SPY holds above its 20-day average, XLE pulls back without breaking its 20-day average, then closes above a 5-day high on non-spike volume.
   - Invalidation: oil reversal, geopolitical de-escalation, or ratio break below its 20-day average with higher relative volume.
   - Suggested future paper-test: one small long-only XLE continuation test after pullback/reclaim, 5–10-session horizon, fixed stop/target; no short-SPY hedge.
   - Risks / not live-ready: commodity/event gaps, existing strategy XLE exposure, and no fresh oil/event or ratio validation.

6. **KBE vs KRE — diversified banks versus regional banks**
   - Thesis: Persistent KBE outperformance can isolate regional funding/credit sensitivity; only a confirmed KRE stabilization would justify studying mean reversion.
   - Confirmation trigger: KRE/KBE reaches a 20-session low, then produces two relative-up closes with normal-to-improving KRE liquidity and no adverse regional-bank news.
   - Invalidation: deposit/credit deterioration, earnings-guidance reset, or renewed funding stress.
   - Suggested future paper-test: observe first; if separately approved, a tiny long-only KRE test after confirmation, hard stop, no averaging down.
   - Risks / not live-ready: asymmetric event risk, regional concentration, and not market-neutral without prohibited short exposure.

### Conclusion
- **NO_TRADE / RESEARCH_ONLY.** No candidate is live-trade-ready, no paper-test lane is authorized, and no action was taken. These are slow, long-only-compatible relative-strength/mean-reversion hypotheses—not latency arbitrage.
- Next research run should obtain synchronized regular-session daily bars, calculate 20-session relative ratios/z-scores and volume filters, check scheduled macro/sector events, and retain only relationships that meet an independently verified trigger.

Notes updated: appended this read-only relative-value research record. No secrets, account identifiers, or credentials were recorded.

## 2026-08-17 08:46 CDT — Scheduled paper run — Balanced v4.1

### Notes and safety checks
- Read at run start: `Trading Automation - Discord Thread Project Note.md`, `Trading Strategy Rules.md`, `Trading Run Log.md`, and `Buy Sell Lessons.md`.
- PAPER-ONLY gate passed: normalized configured base URL and verified host `paper-api.alpaca.markets` before reading account, positions, nested open OCO orders, market clock, recent fills/activity, assets, and fresh IEX quotes/bars. Account was ACTIVE and trading was not blocked. Credentials and account identifiers were neither recorded nor displayed.
- Durable schedule check: the active main job is `45 8 * * 1-5` (one weekday main run) and the separate EOD audit is `10 16 * * 1-5`; this matches Balanced v4.1 policy. No schedule change made.

### Portfolio and exit manager
- Fixed managed bankroll: `$1,000`; larger paper buying power ignored. Core exposure: `$204.69 / $800` (XLF `$116.42`, XLU `$88.27`). Penny exposure: `$44.52 / $200` (ESPR). Total managed exposure: `$249.21`; cash drag: `$750.79`.
- Fill since the prior Aug. 14 EOD audit: XLE 2 shares sold through its existing target at `$62.30` shortly before this run. No replacement or same-day XLE re-entry considered.
- XLF 2 has verified GTC OCO target/stop `$58.75 / $56.50`; XLU 2 has verified GTC OCO `$44.79 / $43.69`. Each parent and held stop leg is for the owned/reserved quantity. No duplicate/excess sell coverage or trailing-only liquid core position found.
- Coverage warning: ESPR 14 is still held and fully available but has no visible target or stop. Direct asset lookup confirms `inactive` / non-tradable, so normal OCO repair is unavailable; no unsupported or duplicate sell order was attempted.

### Researcher → trader → confirmer
- Market clock was open at approximately 09:46 ET. Fresh IEX data: SPY and QQQ were near recent highs, while IWM softened from Friday; KRE traded near its five-session high with a tight `$0.02` quoted spread. XLI was also near its five-session high with a `$0.05` displayed spread, but its one-share price exceeds the normal `$75–$150` core guide.
- Core candidates: KRE showed the cleanest sub-$150 momentum/reclaim profile, but it overlaps existing XLF financial exposure and was near a five-session high. XLI had constructive industrial strength but failed the normal whole-share size fit; XLP, VNQ, XLV, XLB, and XRT did not present a stronger fresh setup in the available bars. Partial early-session volume was not mechanically compared with full-day volume.
- Event check: the NAHB Housing Market Index was scheduled for 10:00 ET, shortly after the decision timestamp. A new entry immediately before that release did not satisfy the no-obvious-high-impact-event-risk gate.
- Penny decision: no new non-biotech penny candidate was eligible. ESPR's inactive/uncovered condition remains a repair-first risk warning; no averaging-down, biotech/FDA-binary, or replacement risk was added.
- Independent risk gate: reject new orders. Although managed exposure is below `$500` and broadened research continues, the imminent macro event, KRE/XLF overlap, candidate-fit limitations, and unresolved inactive ESPR coverage warning outweighed the under-deployment preference.

### Actions and tags
- No paper order submitted, canceled, replaced, or modified.
- `SMART_SELL`: XLE's pre-existing OCO target filled as intended; the paired exit structure closed without intervention.
- `SMART_HOLD`: XLF and XLU retained valid GTC target-plus-stop coverage without churn.
- `NO_CORE_BUY`: wait for post-10:00 ET event confirmation and a diversified B+ core setup with 1.5:1+ reward/risk and immediate verified GTC OCO coverage.
- `NO_PENNY_BUY`; `UNCERTAIN / COVERAGE_WARNING`: ESPR remains inactive/non-tradable and uncovered; no normal broker order repair is safely available.

### Next-run priorities
- Re-read all fills, positions, nested OCO legs, and available quantity; verify XLF/XLU remain paired after the XLE target fill.
- Continue broadened core research after the macro release. If exposure remains below `$500`, consider at most one diversified B+ liquid core setup that fits size, event-risk, 1.5:1 reward/risk, and immediate verified GTC OCO gates.
- Seek only broker-supported/human-reviewed resolution for inactive ESPR; keep new penny exposure paused while this special coverage exception persists.

Notes updated: appended this run record. `Buy Sell Lessons.md` was read and not changed; the inactive-asset and OCO-coverage lessons already capture the reusable condition. No secrets or account identifiers were written.

## 2026-08-17 17:11 EDT — End-of-day paper audit — Balanced v4.1

### Notes and safety checks
- Read: `Trading Automation - Discord Thread Project Note.md`, `Trading Strategy Rules.md`, `Trading Run Log.md`, and `Buy Sell Lessons.md`.
- **READ-ONLY:** normalized configured endpoint and verified host `paper-api.alpaca.markets` before reading account, positions, nested open OCO orders, today’s fills, market clock, asset status, and available IEX quotes. Account was ACTIVE, not blocked, and the market was closed. No order was submitted, canceled, replaced, or modified.

### Managed strategy snapshot
- Fixed strategy bankroll: `$1,000`; larger paper buying power ignored. Core exposure: `$203.47 / $800` — XLF `$115.16`, XLU `$88.31`. Penny exposure: `$44.52 / $200` — ESPR `$44.52`. Total managed exposure: `$247.99`; cash drag: `$752.01` (75.2%), materially below the `$500` Balanced v4.1 rebuild threshold.
- Open-position unrealized P/L: approximately `+$4.51` (XLF `+$3.90`, XLU `+$0.05`, ESPR `+$0.56`). Today’s observed XLE target fill sold 2 at `$62.30` against the recorded `$60.70` entry, estimated realized profit `+$3.20` before any fees. Account day-to-day equity change is not used as managed-strategy realized P/L.

### Fills, exits, and coverage
- Classified today’s only fill as **target/profit capture**: XLE 2-share GTC OCO limit target filled at `$62.30`; the paired stop leg was canceled as expected. No buy, stop/protective exit, or other fill was observed.
- Verified full-position GTC OCO target + protective-stop coverage: XLF 2 (`$58.75 / $56.50`) and XLU 2 (`$44.79 / $43.69`). Parent and held-stop quantities match the reserved position quantities; no trailing-only coverage, duplicate/excess sell quantity, or expired TIF was found. These liquid-core exits remain plausible relative to current position marks; available after-hours IEX display for XLU was sparse, so it is not used alone to invalidate its existing OCO prices.
- **Coverage warning:** ESPR 14 is fully available with no visible target or protective stop. Fresh asset lookup remains `inactive` / non-tradable and the available quote is stale, so normal OCO repair is not safely available. No unsupported order or duplicate sell coverage was attempted.
- Weekend risk: not a Friday-specific audit; XLF/XLU use GTC OCO exits through the next session. ESPR is the sole uncovered overnight-risk exception.

### Balanced v4.1 compliance and recommendation
- Compliant: paper-only endpoint, no audit-side order activity, no averaging down, no same-day XLE target re-entry, no immediate stop-out replacement, and no new biotech/FDA-binary penny buy. Existing ESPR is an inherited inactive-asset exception, not a new permitted penny exposure.
- Cash drag is excessive at 75.2%. Next main run should continue broadened research and may consider at most one diversified B+ or better liquid core setup while exposure is below `$500`, with event review, `1.5:1+` reward/risk, and immediate verified GTC OCO coverage. Keep new penny exposure paused and seek a broker-supported/human-reviewed resolution for inactive, uncovered ESPR.

Notes updated: appended this EOD audit to `Trading Run Log.md`. `Buy Sell Lessons.md` was read and not changed because its inactive-asset/coverage guidance already captures the durable lesson. No secrets or account identifiers were written.
