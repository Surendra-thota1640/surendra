# Data dictionary

## raw_events

| Column | Description |
| --- | --- |
| event_id | Unique event identifier |
| store_id | Store location identifier |
| product_id | Product SKU |
| channel | Channel where the event occurred |
| event_type | purchase, return, refund, or view |
| quantity | Quantity of the product |
| amount | Price or monetary value |
| payment_type | card, wallet, cash, or upi |
| ts | Timestamp in ISO format |

## silver_events

| Column | Description |
| --- | --- |
| order_value | price * quantity |
| is_purchase | Boolean flag for purchase events |
