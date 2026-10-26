from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List


def aggregate_gold(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    totals = defaultdict(float)
    counts = defaultdict(int)

    for event in events:
        totals[event.get("product_id")] += float(event.get("order_value", 0))
        counts[event.get("product_id")] += 1

    return {
        "total_revenue": round(sum(totals.values()), 2),
        "top_products": {
            product: {"revenue": round(value, 2), "orders": counts.get(product, 0)}
            for product, value in totals.items()
        },
    }
