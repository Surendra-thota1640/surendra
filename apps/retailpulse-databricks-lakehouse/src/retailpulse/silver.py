from __future__ import annotations

from typing import Any, Dict, List


def enrich_silver(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    enriched = []
    for event in events:
        enriched.append({
            **event,
            "order_value": float(event.get("amount", 0)) * int(event.get("quantity", 0)),
            "is_purchase": event.get("event_type") == "purchase",
        })
    return enriched
