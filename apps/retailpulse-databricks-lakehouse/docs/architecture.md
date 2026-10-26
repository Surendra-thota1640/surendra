# RetailPulse Architecture

This project follows a layered lakehouse design:

1. Raw zone: ingest event streams from source systems.
2. Bronze layer: normalize raw events into a common schema.
3. Silver layer: enrich event data and add business context.
4. Gold layer: aggregate metrics for dashboards and analytics.

## Main components

- Event generator: simulates retail purchases, returns, and behavior.
- Bronze transformation: standardizes the source event schema.
- Silver transformation: enriches data with derived metrics.
- Gold transformation: creates revenue and product-level KPIs.

## Recommended extensions

- Add ML feature tables for churn or demand prediction.
- Use Delta tables and Unity Catalog for governance.
- Add monitoring jobs and notebook validation checks.
