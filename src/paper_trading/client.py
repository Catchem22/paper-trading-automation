"""Minimal read-only client guarded against live Alpaca endpoints."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Callable
from urllib.parse import urlparse
from urllib.request import Request, urlopen

PAPER_HOST = "paper-api.alpaca.markets"


class PaperEndpointError(RuntimeError):
    """Raised when configuration is missing or does not resolve to Alpaca paper."""


@dataclass(frozen=True)
class AlpacaPaperClient:
    base_url: str
    api_key_id: str
    api_secret_key: str
    opener: Callable[..., Any] = urlopen

    @classmethod
    def from_env(cls) -> "AlpacaPaperClient":
        base_url = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
        api_key_id = os.environ.get("ALPACA_API_KEY_ID", "")
        api_secret_key = os.environ.get("ALPACA_API_SECRET_KEY", "")
        if not api_key_id or not api_secret_key:
            raise PaperEndpointError("Missing Alpaca paper credentials in environment.")
        return cls(base_url=base_url, api_key_id=api_key_id, api_secret_key=api_secret_key)

    def _normalized_base_url(self) -> str:
        base = self.base_url.rstrip("/")
        if base.endswith("/v2"):
            base = base[:-3]
        parsed = urlparse(base)
        if parsed.scheme != "https" or parsed.netloc != PAPER_HOST:
            raise PaperEndpointError("Refusing non-paper Alpaca endpoint.")
        return base

    def get_json(self, path: str) -> Any:
        if not path.startswith("/v2/"):
            raise ValueError("Only Alpaca v2 API paths are allowed.")
        request = Request(
            self._normalized_base_url() + path,
            headers={
                "APCA-API-KEY-ID": self.api_key_id,
                "APCA-API-SECRET-KEY": self.api_secret_key,
            },
            method="GET",
        )
        with self.opener(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))

    def account(self) -> dict[str, Any]:
        return self.get_json("/v2/account")

    def positions(self) -> list[dict[str, Any]]:
        return self.get_json("/v2/positions")

    def open_orders(self) -> list[dict[str, Any]]:
        return self.get_json("/v2/orders?status=open&nested=true&limit=100")
