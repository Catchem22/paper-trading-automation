"""Command-line entrypoint. This project intentionally has no order-placement command."""

from __future__ import annotations

import argparse
import json

from .audit import build_audit
from .client import AlpacaPaperClient, PaperEndpointError


def main() -> int:
    parser = argparse.ArgumentParser(description="Paper-only Alpaca audit")
    parser.add_argument("command", choices=["audit"], help="Read-only command to run")
    args = parser.parse_args()
    try:
        if args.command == "audit":
            print(json.dumps(build_audit(AlpacaPaperClient.from_env()), indent=2, sort_keys=True))
    except PaperEndpointError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
