from __future__ import annotations

import random
from datetime import datetime, timedelta
from typing import Any, Dict, List


def generate_event() -> Dict[str, Any]:
    store_ids = [101, 102, 103, 104]
    products = ["sku_1001", "sku_1002", "sku_1003", "sku_1004"]
    channels = ["web", "mobile", "store", "partner"]
    event_types = ["purchase", "return", "refund", "view"]
    payment_types = ["card", "wallet", "cash", "upi"]

    now = datetime.utcnow()
    return {
        "event_id": f"evt_{random.randint(100000, 999999)}",
        "store_id": random.choice(store_ids),
        "product_id": random.choice(products),
        "channel": random.choice(channels),
        "event_type": random.choice(event_types),
        "quantity": random.randint(1, 5),
        "amount": round(random.uniform(10.0, 250.0), 2),
        "payment_type": random.choice(payment_types),
        "ts": (now - timedelta(minutes=random.randint(0, 1440))).isoformat(),
    }


def generate_events(count: int = 25) -> List[Dict[str, Any]]:
    return [generate_event() for _ in range(count)]
