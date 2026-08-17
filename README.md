# Paper Trading Automation

A **paper-only** Alpaca portfolio audit and risk-gating foundation for the swing-trading project.

## Safety boundary

- It accepts only `https://paper-api.alpaca.markets`.
- It has **no order-placement command**.
- It makes only `GET` requests to account, positions, and open orders.
- Credentials are read from process environment and are never logged.
- `.env` files are ignored; commit only redacted `.env.example` templates.

## Run a read-only audit

```bash
export ALPACA_BASE_URL=https://paper-api.alpaca.markets
export ALPACA_API_KEY_ID='...'
export ALPACA_API_SECRET_KEY='...'
PYTHONPATH=src python3 -m paper_trading.cli audit
```

The audit reports sanitized account totals, positions, active sell-order coverage, and a manual-review flag for positions without a visible open sell order. It intentionally excludes account IDs, raw orders, and credentials.

## Test

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## Project documents

The operating context is versioned alongside the code:

- [Trading Strategy Rules](docs/Trading%20Strategy%20Rules.md)
- [Buy / Sell Lessons](docs/Buy%20Sell%20Lessons.md)
- [Trading Run Log](docs/Trading%20Run%20Log.md)
- [Trading Automation Project Context](docs/Trading%20Automation%20-%20Project%20Context.md)

These documents contain strategy history and decision records only; they must never include brokerage credentials, account identifiers, or raw order IDs.

## Roadmap before adding any execution

1. Collect and evaluate read-only daily audit history.
2. Define one testable strategy with written entry, stop, target, and event-risk rules.
3. Add deterministic risk validation and a dry-run proposal format.
4. Require paper-endpoint re-check plus explicit approval before any future order-placement module.

No live trading, margin, options, or withdrawal functionality belongs in this repository.
