import io
import json
import unittest
from urllib.error import URLError

from paper_trading.audit import build_audit
from paper_trading.client import AlpacaPaperClient, PaperEndpointError


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def read(self):
        return json.dumps(self.payload).encode()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


def fake_opener(request, timeout):
    assert timeout == 20
    assert request.full_url.startswith("https://paper-api.alpaca.markets/v2/")
    if request.full_url.endswith("/account"):
        return FakeResponse({"equity": "1000", "last_equity": "995", "cash": "700", "long_market_value": "300"})
    if request.full_url.endswith("/positions"):
        return FakeResponse([
            {"symbol": "ABC", "qty": "2", "market_value": "100", "unrealized_pl": "1.2"},
            {"symbol": "XYZ", "qty": "1", "market_value": "200", "unrealized_pl": "-2.5"},
        ])
    if "orders?status=open" in request.full_url:
        return FakeResponse([{"symbol": "ABC", "side": "sell", "order_class": "oco"}])
    raise AssertionError(request.full_url)


class PaperClientTests(unittest.TestCase):
    def test_rejects_live_endpoint(self):
        client = AlpacaPaperClient("https://api.alpaca.markets", "id", "secret")
        with self.assertRaises(PaperEndpointError):
            client.account()

    def test_audit_redacts_and_flags_missing_exit(self):
        audit = build_audit(AlpacaPaperClient("https://paper-api.alpaca.markets/v2", "id", "secret", fake_opener))
        self.assertTrue(audit["paper_endpoint_verified"])
        self.assertEqual(audit["account"]["equity"], 1000.0)
        self.assertEqual(audit["risk_flags"]["positions_without_open_sell_order"], ["XYZ"])
        self.assertNotIn("id", json.dumps(audit))
        self.assertNotIn("secret", json.dumps(audit))


if __name__ == "__main__":
    unittest.main()
