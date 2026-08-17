"""Read-only portfolio audit with redacted, operationally useful output."""

from __future__ import annotations

from typing import Any

from .client import AlpacaPaperClient


def _number(value: Any) -> float:
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return 0.0


def build_audit(client: AlpacaPaperClient) -> dict[str, Any]:
    """Fetch allowed read-only resources and return no identifiers or secrets."""
    account = client.account()
    positions = client.positions()
    orders = client.open_orders()
    exit_symbols = {order.get("symbol") for order in orders if order.get("side") == "sell"}
    position_rows = [
        {
            "symbol": position.get("symbol"),
            "quantity": position.get("qty"),
            "market_value": _number(position.get("market_value")),
            "unrealized_pl": _number(position.get("unrealized_pl")),
            "covered_by_open_sell_order": position.get("symbol") in exit_symbols,
        }
        for position in positions
    ]
    missing_exit_symbols = [
        row["symbol"] for row in position_rows if not row["covered_by_open_sell_order"]
    ]
    return {
        "mode": "READ_ONLY_PAPER_AUDIT",
        "paper_endpoint_verified": True,
        "account": {
            "equity": _number(account.get("equity")),
            "last_equity": _number(account.get("last_equity")),
            "cash": _number(account.get("cash")),
            "long_market_value": _number(account.get("long_market_value")),
        },
        "positions": position_rows,
        "open_sell_order_symbols": sorted(symbol for symbol in exit_symbols if symbol),
        "risk_flags": {
            "positions_without_open_sell_order": missing_exit_symbols,
            "requires_manual_review": bool(missing_exit_symbols),
        },
    }
