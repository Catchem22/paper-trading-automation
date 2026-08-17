# Buy Sell Lessons

Related: [[Trading Automation - Discord Thread Project Note]] · [[Trading Strategy Rules]] · [[Trading Run Log]]

Purpose: durable lessons for the paper-trading automation. Keep this concise and reusable. Do not store secrets, account IDs, account numbers, or raw credential material.

## Current lessons

### Profit capture matters

A position can be up going into a weekend and still exit later via trailing stop after giving back gains. The automation should not rely only on trailing stops. It should evaluate weekly-high/5-day-high targets, partial profit-taking, and stop tightening when a position is profitable.

### Target limit must be part of the initial exit structure

If a new paper position is opened, the automation should place a profit-capture exit in the same run after fill verification. Preferred structure is bracket/OCO-style: take-profit limit near a realistic weekly-high/target zone plus protective stop-loss. If Alpaca does not support a true trailing stop as the stop leg, use a fixed stop-loss and raise/replace it in later runs as a synthetic trailing stop. Do not use “single share” as a reason to skip the target; choose a full-position target+stop structure instead.

### No-buy logs are signal, not failure

A `NO_CORE_BUY` or `NO_PENNY_BUY` decision is acceptable when the setup quality or risk gate fails. The automation should not force buys to fill the $1,000 bankroll.

However, repeated no-buys are information. Track no-buy streaks separately for core and penny buckets. After 3 consecutive no-buys in an under-target bucket, broaden research beyond the base watchlist; after 5 consecutive no-buys, explicitly report `RESEARCH_EXPANDED` and list the expanded scans/sources used. Expanded research must not loosen risk gates or target+stop requirements.

### Use exposure limits instead of fixed position count

The prior fixed limit of four open positions caused under-utilization. The new policy allows more positions as long as total strategy exposure stays within the $1,000 bankroll and bucket limits.

### Penny stocks require their own risk sleeve

Penny stocks are allowed only inside the $200 high-risk bucket. They need stricter filters for liquidity, spread, volatility, and exit planning. Do not let penny-stock exposure spill into the core bucket.

## Lesson entry format

```text
### YYYY-MM-DD — Symbol / theme

Decision: SMART_BUY | BAD_BUY | SMART_SELL | BAD_SELL | SMART_HOLD | BAD_HOLD | UNCERTAIN
Context:
What happened:
Lesson:
Rule update needed:
```


### 2026-05-26 — Whole-share deployment with immediate stops

Decision: UNCERTAIN
Context: Strategy v2 needed higher utilization without relying on fractional positions that can create stop-order complications.
What happened: The run used small whole-share ETF positions and tiny whole-share penny positions, then placed separate trailing stops immediately after fills.
Lesson: For this paper workflow, whole-share marketable limit entries can make post-fill protective trailing stops simpler and reduce the risk of unsupported fractional/bracket behavior. Keep remaining cash when the best candidates are stretched rather than forcing full deployment.
Rule update needed: No formal rule change; continue preferring position structures that allow clean protective stop coverage.

### 2026-05-26 — Near-high single-share positions need explicit profit capture

Decision: UNCERTAIN
Context: EOD audit found several protected ETF positions within about 1% of their 5-day highs, but no separate target/limit exits were open.
What happened: Trailing stops protected downside, but the account was still exposed to giving back gains if price fades before a target exit is attempted. Single-share ETF positions cannot partial out cleanly.
Lesson: When a one-share position is close to a weekly/5-day high, the exit manager should choose between a realistic target limit sell and a tighter/raised trailing stop instead of relying only on a passive wider trailing stop.
Rule update needed: No formal rule change; reinforce the existing weekly-high/profit-capture rule during the next trade run.

### 2026-05-27 — Tight trailing stops can be profit capture for tiny positions

Decision: UNCERTAIN
Context: Single-share positions and tiny penny positions cannot be partially sold cleanly without removing all exposure, and existing trailing stops can be wide enough to give back most unrealized profit.
What happened: The run tightened BBAI from a 10% trailing stop to 6% and XLY from 4% to 2.5%, then verified replacement trailing-stop orders existed. New XRT and OPEN buys also received immediate protective trailing stops.
Lesson: For whole-share/tiny paper positions, a tighter trailing stop is often safer than adding a separate target order that could conflict with existing sell coverage. Always verify the replacement stop exists after cancel/recreate before considering the position protected.
Rule update needed: Continue treating missing-stop detection as an immediate repair item. The 2026-05-27 run found XLI without an open trailing stop and repaired it with a verified 4% trailing stop.

### 2026-05-27 — Near-full utilization does not mean forcing the last dollars

Decision: SMART_HOLD
Context: EOD audit showed about $904 of the $1,000 strategy bankroll deployed, with core exposure nearly at its $800 target and penny exposure still safely below the $200 sleeve.
What happened: The remaining cash drag was under 10% of the strategy bankroll. Filling it mechanically would risk crowding the core cap or forcing lower-quality penny entries.
Lesson: Once utilization is high and bucket caps are respected, holding a small cash reserve is smarter than forcing trades. Deploy the last dollars only when candidates have clean liquidity, setup, and exit plans.
Rule update needed: No formal rule change; keep reporting cash drag, but judge it against candidate quality and bucket capacity.

### 2026-05-27 — OCO target+stop upgrade is preferred over trailing-only when safe

Decision: SMART_SELL
Context: Strategy v3 requires explicit profit-capture targets paired with downside protection, and prior runs had several trailing-only positions near weekly/5-day highs.
What happened: The run successfully replaced trailing-only sell orders for XLY, BBAI, and XLI with Alpaca paper OCO exits: accepted take-profit limit parents plus held protective stop legs for the same full quantities.
Lesson: For whole-share/tiny positions, full-position OCO target+stop orders can satisfy both profit capture and downside protection without creating duplicate sell quantity. Cancel/re-read/replace/verify is safer than layering independent sell orders over existing full-quantity trailing stops.
Rule update needed: Continue phased OCO upgrades for profitable or near-high trailing-only positions, but verify OCO legs immediately and repair with a protective stop if any replacement fails.


### 2026-05-27 — Phased OCO upgrades reduce trailing-only gap

Decision: SMART_SELL
Context: Strategy v3 requires visible profit-capture targets paired with downside protection. Some existing one-share ETF positions still had only trailing stops.
What happened: The run canceled/re-read/replaced trailing-only coverage for SCHD, TLT, and XLV with full-position Alpaca paper OCO exits, then verified target+stop coverage was visible. No new buys were placed because utilization was already about 90% and the core bucket was effectively full.
Lesson: Continue phased OCO upgrades rather than layering independent target orders on top of full-quantity trailing stops. Cancel/re-read/replace/verify keeps sell quantity from exceeding owned shares and preserves downside protection.
Rule update needed: No formal rule change; keep treating visible target+stop coverage as the preferred v3 exit structure when safe.


### 2026-05-28 — Correct OCO payload shape matters

Decision: SMART_SELL
Context: The v3 pipeline needed to upgrade the remaining trailing-only positions to visible target+stop structures.
What happened: The first Alpaca paper OCO replacement attempt was rejected because the payload used only a top-level limit price. The automation immediately repaired trailing-stop protection, then resubmitted valid OCO exits using `take_profit.limit_price` plus `stop_loss.stop_price`; IGV, XLF, XRT, MVIS, and OPEN were verified with target+stop coverage.
Lesson: For Alpaca paper OCO exits on existing positions, use the explicit take-profit object and verify both target and stop legs after every replacement. If an OCO attempt fails, immediately repair downside protection before continuing.
Rule update needed: No policy change; preserve the cancel/re-read/replace/verify pattern and the corrected OCO payload shape.

### 2026-05-28 — Bracket buys still need post-fill exit-leg verification

Decision: UNCERTAIN
Context: The run redeployed target-fill cash into new whole-share core ETF positions using Alpaca paper bracket buys.
What happened: VNQ and XLK entry fills appeared quickly, but the first post-fill open-order check showed visible target-limit legs without visible stop quantities. The automation canceled the new sell coverage and replaced it with full-position OCO target+stop exits, then verified both target and stop coverage for each symbol.
Lesson: Even when a bracket buy is accepted, do not assume both exit legs are visibly active after fill. Re-read open orders after fill; if only a target leg is visible, repair with cancel/re-read/replace/verify OCO coverage before ending the run.
Rule update needed: Treat post-fill target+stop verification as mandatory for bracket entries, not just submitted-order acceptance.

### 2026-05-28 — Do not chase immediate re-entry after target fills

Decision: SMART_HOLD
Context: Several positions hit planned OCO target exits earlier in the day, freeing cash while broad ETFs and some penny names remained near short-term highs.
What happened: The midday run verified all remaining positions had target+stop coverage and chose no new buy rather than immediately rebuying recent winners or forcing the penny sleeve.
Lesson: A successful target fill should reset the setup review. Do not automatically rebuy a symbol just because it remains liquid and near highs; require a fresh entry zone, catalyst, and full target+stop plan.
Rule update needed: No formal policy change; reinforces `NO_TRADE` when the only available trades are chase entries or averaging down.


### 2026-05-28 — Target exits validate v3 profit-capture design

Decision: SMART_SELL
Context: EOD audit reviewed the first full day after phased OCO target+stop upgrades replaced trailing-only coverage across the paper portfolio.
What happened: XLV, BBAI, IGV, OPEN, and XRT exited through planned take-profit target fills, while remaining positions retained paired target-limit and protective stop-loss coverage.
Lesson: The v3 target+stop structure is working better than trailing-only coverage for capturing gains near realistic targets. Keep using cancel/re-read/replace/verify OCO upgrades and avoid immediate chase re-entry after a target fill.
Rule update needed: No formal rule change; reinforce post-fill exit verification and fresh-setup requirements before redeploying freed cash.

### 2026-05-29 — Bracket target-only visibility still requires immediate repair

Decision: SMART_SELL
Context: A new XBI paper bracket buy filled, but the post-fill open-order check showed only a visible target-limit sell and no visible protective stop leg.
What happened: The automation canceled the target-only sell coverage, re-read orders, and replaced it with a full-position OCO exit using a take-profit limit and protective stop-loss. The repaired XBI OCO target+stop was verified before the run ended.
Lesson: Bracket order acceptance is not enough; visible target+stop coverage after fill is mandatory. If a bracket buy leaves target-only coverage, immediately cancel/re-read/replace/verify with OCO rather than treating the position as protected.
Rule update needed: No formal change; reinforces the existing v3 post-fill verification rule.

### 2026-05-29 — Valid penny no-buy with expanded research

Decision: SMART_HOLD
Context: Penny sleeve exposure remained far below the $200 target after earlier BBAI/OPEN target exits, creating a multi-run no-buy streak.
What happened: The late-Friday run expanded penny research beyond the base list and explicitly reported `RESEARCH_EXPANDED`, but still rejected candidates that lacked fresh catalyst, clean liquidity/spread quality, or safe target+stop math.
Lesson: Underused penny allocation is acceptable when research is actively broadened and risk gates remain strict. Do not force a penny buy just to fill the sleeve; keep expanding discovery until a clean under-$5 setup appears.
Rule update needed: No formal change; continue requiring explicit `RESEARCH_EXPANDED` reporting during 5+ no-buy streaks.


### 2026-06-01 — Bracket target-only repair repeated on IGV

Decision: SMART_SELL
Context: A new IGV core paper buy filled, but post-fill verification again showed only the target-limit leg visible from the initial bracket-style entry.
What happened: The automation canceled the incomplete IGV target-only sell coverage, re-read open orders, and replaced it with a full-position OCO target+stop exit. Verification showed target $106.30 and stop $101.55 for the full share.
Lesson: Keep treating bracket acceptance as insufficient until both profit target and protective stop are visible. If only a target appears, cancel/re-read/replace/verify with OCO before ending the run.
Rule update needed: No formal rule change; this reinforces the existing v3 repair requirement.

### 2026-06-01 — Expanded penny research can break a no-buy streak, but size stays small

Decision: UNCERTAIN
Context: Penny sleeve had a 5+ no-buy streak and remained far below its $200 target, so research expansion continued while strict risk gates stayed in place.
What happened: GRAB passed the expanded under-$5 scan with strong liquidity, constructive short-term momentum, and realistic target+stop math. The run bought 11 shares and immediately verified full-position OCO coverage with target $3.93 and stop $3.41.
Lesson: Expanded research is useful when it finds a genuinely cleaner penny candidate, but the first add after a long no-buy streak should remain small and fully covered. Do not treat one accepted penny trade as permission to force the rest of the sleeve.
Rule update needed: No formal rule change; keep expanded discovery active while preserving liquidity/spread/catalyst/target+stop gates.

### 2026-06-01 — Rebuild core exposure selectively after mixed stop/target exits

Decision: UNCERTAIN
Context: Recent runs saw both protective stop exits and target fills, leaving core exposure below the $800 target while broad ETFs were mixed.
What happened: The run selected only one core replacement, XME, because it fit the position-size guide, was liquid, above short moving averages, and near a recent high. It did not overfill the core bucket after IGV's target fill and prior XBI/XLY stop-outs.
Lesson: When exposure drops because exits are working, rebuild with one or two clean setups rather than reflexively replacing every sold position. Target fills and stop fills both require a fresh setup review before redeployment.
Rule update needed: No formal rule change; continue using exposure targets as guides, not mandates.


### 2026-06-01 — Selective core refill after target/stop churn

Decision: UNCERTAIN
Context: Core exposure remained below the $800 target after recent IGV target capture and XBI/XLY stop exits, while several large technology candidates were strong but too large or chase-prone for the small-bankroll whole-share structure.
What happened: The run selected one XHB core add because it fit the $75-$150 guide and remaining core capacity, then immediately verified full-position OCO coverage with a realistic target and protective stop. It did not force a second core add after capacity dropped below normal size.
Lesson: After mixed stop/target churn, refill core exposure in clean single increments that fit the remaining bucket capacity. A position is not complete until target+stop coverage is visible after fill verification.
Rule update needed: No formal rule change; continue treating exposure targets as guides and visible OCO coverage as mandatory.

### 2026-06-01 — EOD: cash drag is acceptable when OCO coverage is complete

Decision: SMART_HOLD
Context: EOD audit after XBI/XLY stop exits, IGV target capture, and new XME/GRAB/XHB buys left total strategy utilization around 81% with core slightly under target and penny sleeve still underused.
What happened: Every open position had paired OCO target+stop coverage, no trailing-only positions were found, and the latest no-buys were documented with expanded penny research rather than forced low-quality entries.
Lesson: Do not fill the remaining bankroll mechanically when core capacity is below normal whole-share size and penny candidates lack clean catalyst/liquidity/exit quality. Preserve cash until a fresh setup can be bought with immediate target+stop coverage.
Rule update needed: No formal rule change; reinforces exposure-target-as-guide, no-average-down, and mandatory visible target+stop coverage.


### 2026-06-02 — Alpaca tick-size rounding on order prices

Decision: UNCERTAIN
Context: Core and penny replacement orders were prepared after XME target fill and MVIS stop fill created capacity.
What happened: Initial paper order attempts were safely rejected because limit prices used too many decimal places for stocks priced above $1. The automation corrected the tick-size formatting, resubmitted paper-only orders, and verified SLV/ESPR fills plus target+stop OCO coverage.
Lesson: Before submitting Alpaca equity orders, round prices at/above $1 to cents and use four-decimal precision only for sub-$1 securities. Treat API rejections as safe stops, repair the payload, and verify final coverage.
Rule update needed: Add tick-size formatting to any reusable order-placement helper.


### 2026-06-02 — Selective SOFI core refill with immediate OCO

Decision: UNCERTAIN
Context: Core exposure was below the $800 target after recent target/stop churn, while the penny sleeve remained under target but lacked a second clean under-$5 setup.
What happened: The run selected SOFI as a liquid core-stock refill sized inside the $75-$150 guide, bought 5 shares, then immediately verified full-position OCO coverage with target $18.75 and stop $17.10. Penny exposure was not forced because GRAB/ESPR were already held and other under-$5 candidates failed strict filters.
Lesson: When core capacity is available, a liquid high-volume stock can be used as a core refill if it fits size and target+stop math. Keep penny no-buys valid when expanded research does not produce a clean new setup.
Rule update needed: No formal rule change; continue visible OCO verification after every new fill.


### 2026-06-04 — Refill core after multiple exits, but keep penny no-buy strict

Decision: UNCERTAIN
Context: Recent target/stop fills reduced total strategy utilization to roughly half the $1,000 bankroll before the run, while the penny sleeve remained far below target.
What happened: The run rebuilt core exposure with three liquid ETF positions (XLV, XRT, XLP), each filled with immediate verified OCO target+stop coverage. It did not force a penny add because ESPR was already held, GRAB had just stopped out, and expanded under-$5 candidates lacked enough catalyst/trend/exit quality.
Lesson: When several exits free risk budget, it is reasonable to rebuild core with multiple uncorrelated liquid ETFs if each has visible target+stop coverage. Underused penny allocation should still remain cash when the only choices are averaging down, re-entering a stopped name too quickly, or accepting weak catalyst/spread/range quality.
Rule update needed: No formal rule change; reinforces exposure-based refills, no automatic averaging down, and mandatory target+stop verification.


### 2026-06-04 — Expanded penny screen can add one clean name without filling the sleeve

Decision: UNCERTAIN
Context: Penny exposure remained far below the $200 sleeve after GRAB stopped out and ESPR remained the only held penny position, while recent logs showed repeated penny no-buys.
What happened: The run used expanded most-active/high-volume under-$5 screens and selected only RXRX, a liquid narrow-spread candidate, for a small 10-share add with immediate verified OCO target+stop coverage. It rejected additional penny names instead of forcing the sleeve toward $200.
Lesson: Expanded research should improve discovery, not lower standards. When a clean penny candidate appears, add small size with full target+stop coverage and leave the rest of the sleeve cash until another independent setup passes strict filters.
Rule update needed: No formal rule change; continue one-at-a-time penny additions, no averaging down, and visible OCO verification.


### 2026-06-04 — Small add after target fill should still get full OCO coverage

Decision: UNCERTAIN
Context: XLF target profit capture freed core capacity, while the penny sleeve remained under target after repeated under-$5 research expansion.
What happened: The run added one small XLE core position and one small IOVA penny/biotech position, then verified full-position OCO target+stop exits for both immediately after fill.
Lesson: When remaining core capacity is too small for most normal ETF adds, a smaller liquid sector ETF can be acceptable if it keeps the bucket under cap and receives immediate target+stop coverage. For penny/biotech additions, one clean high-volume narrow-spread name is enough; do not force multiple correlated high-risk names just to fill the sleeve.
Rule update needed: No formal rule change; reinforces exposure caps, one-at-a-time penny additions, and visible OCO verification.

### 2026-06-04 — Late-day full-coverage hold is valid

Decision: SMART_HOLD
Context: The final scheduled trade run found roughly 89% of the $1,000 bankroll deployed, with core capacity below normal whole-share add size and three active penny-sleeve positions already covered by OCO exits.
What happened: No new buys or order replacements were submitted. Every open position already had visible target-limit profit capture plus protective stop coverage, and fresh core/penny candidates did not justify breaking exposure caps or adding late-day risk.
Lesson: When utilization is high and OCO coverage is complete, doing nothing can be the highest-quality action. Avoid late-day churn and avoid adding more penny/biotech risk unless a clean, independent setup beats existing exposure.
Rule update needed: No formal rule change; reinforces `SMART_HOLD`, no forced buys, and complete target+stop coverage.


### 2026-06-05 — Refill core after Friday exits, but do not chase penny stop-outs

Decision: UNCERTAIN
Context: XLV hit its planned target while SLV and RXRX exited by protective stops, reducing total strategy exposure and leaving the penny sleeve under target.
What happened: The run rebuilt core exposure with XLI and KRE, each filled with immediate verified OCO target+stop coverage. It did not re-enter RXRX or add another penny name because existing penny positions were already held and fresh under-$5 candidates were too extended, volatile, sub-dollar risky, or lacked clean target+stop quality.
Lesson: After mixed target/stop exits, refill the higher-quality core bucket first when clean liquid setups exist, and treat penny stop-outs as a reset rather than an invitation to chase re-entry. Underused penny capacity remains acceptable when no independent clean setup passes strict gates.
Rule update needed: No formal rule change; reinforces no automatic re-entry after stops, no averaging down, and mandatory visible OCO coverage for every new buy.


### 2026-06-05 — Refill core with adjacent theme only if target+stop remains clean

Decision: UNCERTAIN
Context: KRE hit its planned target during the same day, freeing core capacity while financial/bank ETF quotes remained constructive.
What happened: The run did not immediately rebuy KRE. It selected KBE as a related but separate liquid bank ETF refill that fit the remaining core cap, then verified full-position OCO target+stop coverage immediately after fill.
Lesson: After a target fill, adjacent-theme reallocation can be acceptable when it avoids exact same-symbol chase behavior, stays under the bucket cap, and receives visible target+stop coverage. Keep the follow-through uncertain until the new position proves itself.
Rule update needed: No formal rule change; reinforces fresh setup review after target fills and mandatory OCO verification.


### 2026-06-05 — Friday OCO exits should not expire at the close

Decision: SMART_SELL
Context: The midday Friday run found XLI had visible target+stop OCO coverage, but the order was `day` time-in-force and would expire at the closing bell before the weekend.
What happened: The automation canceled the day-TIF XLI OCO after re-reading paper account/positions/orders, then replaced it with a full-position GTC OCO using the same target and stop. Verification showed both target and stop legs visible.
Lesson: Exit coverage is not complete if the target+stop order will expire before the intended hold period. Late-Friday and swing positions should be checked for `time_in_force` and expiration risk, not just presence of target and stop legs.
Rule update needed: Add a recurring exit-manager check for `time_in_force` and expiration risk, not just presence of target and stop legs.

### 2026-06-05 — Five-run penny no-buy is valid when expanded research still fails gates

Decision: SMART_HOLD
Context: The Friday final scheduled run found the penny sleeve materially under target, but the last five scheduled runs showed repeated `NO_PENNY_BUY` outcomes.
What happened: The run explicitly reported `RESEARCH_EXPANDED`, checked a broader under-$5/high-volume list with Alpaca IEX quote/spread and daily-bar context, and still rejected new penny adds because candidates were already held, recently stopped, sub-dollar/wide-spread, too volatile/extended, or lacked clean target+stop quality.
Lesson: A five-run no-buy streak should broaden discovery, not weaken the filter. Underused penny cash remains acceptable over a weekend when no independent clean setup can be bought with immediate visible target+stop coverage.
Rule update needed: No formal rule change; continue explicit `RESEARCH_EXPANDED` reporting during 5+ under-target penny no-buy patterns.

### 2026-06-05 — Defensive v4 after small drawdown

Decision: SMART_HOLD
Context: The v3 paper strategy showed about a $13-$15 drawdown on the $1,000 managed bankroll. Order safety and OCO coverage worked, but trade selection was too noisy, especially penny/biotech names and immediate replacement/chase behavior.
What happened: Automation was changed to Defensive v4: one main trade run per weekday, one read-only EOD audit, no new penny/biotech buys, max one new core buy per day, A-grade-only entries, cooldown after stop-outs, and no same-day re-entry after target fills. A separate relative-value/arbitrage research lane was created as read-only.
Lesson: A small controlled paper drawdown is useful only if it tightens the system. When stops are working but losses accumulate, reduce frequency and reject more trades rather than adding complexity or chasing arbitrage.
Rule update needed: Defensive v4 overlay is now active in Trading Strategy Rules.md.

### 2026-06-08 — Defensive hold when core is near cap

Decision: SMART_HOLD
Context: Monday-morning Defensive v4 run after Friday target/stop activity, with core exposure around $781 of the $800 target and all positions already covered by GTC OCO target+stop exits.
What happened: The automation verified paper-only endpoint, read account/positions/orders/clock/fills/quotes/bars, found no unsafe coverage gaps, and placed no new orders. It did not replace Friday exits or add penny/biotech exposure.
Lesson: When core exposure is less than $75 below target and exit coverage is complete, the best Defensive v4 action is often HOLD/NO_TRADE. Do not treat available paper buying power or underused penny sleeve cash as a reason to churn.
Rule update needed: No formal rule change; reinforces Defensive v4 core-room and no-new-penny/biotech gates.

### 2026-06-08 — Defensive stop-out is not a replacement signal

Decision: SMART_SELL
Context: EOD Defensive v4 read-only audit found IOVA had exited through its pre-existing protective stop near $4.07 after the morning run had already disabled new penny/biotech buys.
What happened: IOVA sold in two fill events totaling 10 shares and no replacement trade was submitted. Remaining open positions retained complete GTC OCO target+stop coverage with no duplicate/excess sell quantity.
Lesson: A penny/biotech stop-out should be treated as risk control working, not as an invitation to immediately refill the sleeve. Under Defensive v4, keep new penny/biotech buys disabled and require a later human-approved or policy-approved setup before adding similar risk again.
Rule update needed: No formal rule change; reinforces no immediate replacement after stop-outs and `PENNY_EXIT_ONLY` behavior.

### 2026-06-09 — Target fills are not same-day replacement signals

Decision: SMART_SELL / SMART_HOLD
Context: KBE and XHB hit planned target exits before the Defensive v4 morning run, reducing core exposure and creating room under the $800 core cap.
What happened: The run accepted the target fills as successful profit capture, verified all remaining positions still had GTC target+stop coverage, and placed no same-day replacement buy because candidates either involved target-chase context or lacked complete A-grade volume confirmation.
Lesson: Profit-capture exits should reduce churn, not trigger automatic redeployment. In Defensive v4, wait for a fresh A-grade setup with confirmed volume, clean reward/risk, and no same-day target/stop chase before adding core exposure back.
Rule update needed: No formal rule change; reinforces no same-day re-entry after targets and A-grade-only core refill discipline.

### 2026-06-09 — Defensive target cascade can leave cash intentionally high

Decision: SMART_SELL / SMART_HOLD
Context: EOD read-only audit found KBE, XHB, XLI, and XRT all exited through planned target sells, reducing managed exposure to about 40% of the $1,000 bankroll.
What happened: The target exits realized an estimated combined paper gain of about +$6.50, and the audit verified the remaining ESPR, SCHD, TLT, VNQ, XLE, and XLP positions still had full GTC target+stop coverage. No replacement orders were submitted because the EOD job is read-only and Defensive v4 forbids automatic same-day target re-entry.
Lesson: A profitable target cascade is success, not an emergency to refill exposure. Under Defensive v4, let cash sit overnight and require the next scheduled trading run to document a fresh A-grade setup before adding at most one core position.
Rule update needed: No formal rule change; reinforces no same-day target re-entry, A-grade-only core adds, and cash-as-protection during defensive mode.



### 2026-06-10 — Fresh setup evidence beats mechanical redeployment

Decision: SMART_HOLD
Context: Defensive v4 morning run after a target cascade reduced managed exposure and XLP hit a same-day target before the run.
What happened: A few liquid ETFs passed a basic relative-strength/spread/volume screen, but the run rejected new buys because XLP was a same-day target fill and XHB/XRT/KBE/KRE-style opportunities were too close to recent profit-capture/redeployment context. Existing open positions already had valid GTC OCO target+stop coverage.
Lesson: In Defensive v4, low exposure alone is not a buy signal. After target fills, require fresh A-grade evidence rather than mechanically rebuying the same or adjacent themes. Cash is acceptable while the system is trying to reduce churn.
Rule update needed: No formal rule change; reinforces no same-day target chase and A-grade-only core refill discipline.

### 2026-06-10 — EOD target fill can leave the portfolio cash-heavy on purpose

Decision: SMART_SELL / SMART_HOLD
Context: Defensive v4 EOD read-only audit after XLP exited through its planned target and no new buys were allowed by the audit job.
What happened: XLP realized an estimated +$1.50 paper gain from the observed 2026-06-04 entry to the 2026-06-10 target sell. Remaining ESPR, SCHD, TLT, VNQ, and XLE positions still had full GTC OCO target+stop coverage, and no replacement order was submitted.
Lesson: In Defensive mode, a target fill plus complete coverage is success even when managed exposure falls. Do not treat cash-heavy exposure as a defect; require the next trading run to document a fresh A-grade setup and continue forbidding same-day target re-entry.
Rule update needed: No formal rule change; reinforces cash-as-protection, no same-day target chase, and complete coverage before adding risk.

### 2026-06-11 — Relative strength without volume/R:R is not A-grade

Decision: SMART_HOLD
Context: Defensive v4 morning run found low managed exposure and several ETFs with SPY-relative strength, but the system is intentionally reducing churn after noisy v3 behavior.
What happened: The run verified paper-only account state and complete GTC OCO coverage, screened liquid core candidates, and placed no buy because volume confirmation was weak at the run timestamp and realistic target/stop reward/risk was not strong enough for an A-grade entry.
Lesson: Low exposure plus relative strength is still not a buy signal. In Defensive v4, require simultaneous tight spread, fresh volume confirmation, clean event-risk context, and at least 1.5:1 realistic target/stop math before adding even one core position.
Rule update needed: No formal rule change; reinforces A-grade-only core additions and cash-as-protection during defensive mode.


### 2026-06-11 — Balanced v4.1 after over-defense

Decision: SMART_HOLD
Context: Defensive v4 protected the paper bankroll and harvested winners, but after recovering most of the earlier drawdown it left the strategy too under-deployed. The operating policy allows selective penny-stock participation, excluding risky biotech/FDA-binary names.
What happened: Strategy rules were revised from the most restrictive Defensive v4 posture to Balanced v4.1: keep OCO exits, no averaging down, paper-only scope, and cooldowns, but allow one core and one non-biotech penny setup per main run when quality gates pass.
Lesson: After the bot proves stops/targets and profit capture are working, avoid over-correcting into permanent cash drag. Rebuild exposure when managed exposure falls below about $500, but keep biotech penny risk disabled by default.
Rule update needed: Active rules now use Balanced v4.1 with B+ core entries allowed below $500 managed exposure and selective non-biotech penny buys inside the $200 sleeve.


### 2026-06-11 — Balanced cash drag after target fills needs active redeployment research

Decision: SMART_SELL / SMART_HOLD
Context: Balanced v4.1 EOD read-only audit found TLT had exited through its target for an estimated paper gain, leaving only about $231 of the $1,000 managed bankroll deployed.
What happened: Remaining positions retained full GTC OCO target+stop coverage, but exposure fell far below the ~$500 Balanced v4.1 rebuild threshold. No replacement order was submitted because the EOD audit is read-only.
Lesson: In Balanced v4.1, target fills are still success, but very low exposure should become an active research/redeployment prompt for the next main run. Prefer one valid B+ core setup when exposure is below ~$500 and optionally one clean non-biotech penny setup inside the sleeve; do not relax OCO, no-chase, no-averaging, liquidity/spread, or reward/risk gates.
Rule update needed: No formal rule change; reinforces the Balanced v4.1 under-deployment rule and the separation between read-only EOD recommendations and main-run order placement.


### 2026-06-12 — Early-session volume checks need context

Decision: UNCERTAIN
Context: Balanced v4.1 main run needed to rebuild exposure below the ~$500 threshold. Early in the session, current-day daily volume looked weak versus full-day averages for many liquid ETFs, even while live spreads and relative strength were acceptable.
What happened: The run avoided blindly treating incomplete daily-volume data as a hard rejection signal, selected one liquid B+ core ETF setup (KRE), and immediately verified full-position GTC OCO target+stop coverage after fill.
Lesson: During the first hour, do not compare partial current-day volume directly to full-day average volume as a standalone gate. Require tight live spread/liquidity, relative strength, and clean reward/risk, but interpret volume confirmation in context of time elapsed.
Rule update needed: No formal rule change; improve future scanner logic to normalize intraday volume or avoid full-day volume thresholds early in the session.

### 2026-07-13 — Same-day OCO repairs need EOD re-verification

Decision: UNCERTAIN
Context: Balanced v4.1 morning run repaired missing ESPR target+stop coverage, but the read-only EOD audit later found the repair OCO canceled while the ESPR shares remained open.
What happened: The EOD audit found no same-day fills, ESPR still held, and no visible open ESPR sell coverage. Other visible OCO exits remained valid, while BBAI stayed stuck in a pending-cancel state.
Lesson: Do not assume an intraday repair remains valid through the close. EOD audits should re-read open orders and all-order history for repaired symbols, then flag any canceled repair that leaves shares uncovered. The next trading run should repair available uncovered shares before adding new risk.
Rule update needed: No formal rule change; reinforces EOD coverage verification and repair-first sequencing.


### 2026-07-14 — Inactive held assets can block normal OCO repair

Decision: UNCERTAIN
Context: Balanced v4.1 run found ESPR still held with no visible sell coverage after a prior repair OCO canceled.
What happened: A fresh paper OCO repair attempt for ESPR was rejected because Alpaca reported the asset as not active. The run did not layer duplicate or invalid sell orders, and it prioritized reporting the uncovered/inactive state.
Lesson: When a held symbol becomes inactive, standard target+stop OCO repair may be unavailable even though the position remains in the account. Treat this as a special coverage warning: re-check asset tradability/order eligibility before repair, avoid duplicate sell quantity, and escalate for human review or broker-supported liquidation path rather than assuming normal OCO mechanics will work.
Rule update needed: No formal rule change; reinforces repair-first sequencing and explicit inactive-asset handling.

### 2026-07-15 — Pending-cancel exits can neutralize practical stop protection

Decision: UNCERTAIN
Context: EOD read-only audit found BBAI still held with an OCO parent stuck in `pending_cancel`, a held stop leg shown above the current position price, and zero available quantity.
What happened: The audit did not submit or layer any duplicate sell order, but flagged that a visible held stop leg is not enough when the parent order state is dirty and the position has already traded below the stop area.
Lesson: Treat stuck `pending_cancel` OCO exits as coverage warnings, not clean protection. Re-read nested orders, position `qty_available`, and recent fills before acting; avoid duplicate sell quantity while shares are tied up, and prioritize broker/API state resolution before adding related risk.
Rule update needed: No formal rule change; reinforces repair-first sequencing, duplicate-sell avoidance, and EOD verification of dirty order states.
