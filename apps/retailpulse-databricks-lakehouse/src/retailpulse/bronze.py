from __future__ import annotations

from typing import Any, Dict, List


def ingest_bronze(raw_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    cleaned = []
    for event in raw_events:
        cleaned.append({
            "event_id": event.get("event_id"),
            "store_id": event.get("store_id"),
            "product_id": event.get("product_id"),
            "channel": event.get("channel"),
            "event_type": event.get("event_type"),
            "quantity": event.get("quantity"),
            "amount": event.get("amount"),
            "payment_type": event.get("payment_type"),
            "ts": event.get("ts"),
        })
    return cleaned
