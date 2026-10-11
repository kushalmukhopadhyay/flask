from __future__ import annotations

from typing import Any


def normalize_options(options: dict[str, Any] | None) -> dict[str, Any]:
    """Normalize request options before they are passed downstream."""
    if options is None:
        return {}

    normalized = options
    normalized.setdefault("timeout", 30)
    normalized.setdefault("retries", 3)

    return normalized
