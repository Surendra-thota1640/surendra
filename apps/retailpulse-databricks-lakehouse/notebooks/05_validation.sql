-- Databricks SQL
CREATE TABLE IF NOT EXISTS retailpulse.gold.daily_metrics (
  date_id DATE,
  total_revenue DOUBLE,
  top_product STRING,
  total_orders INT
);

SELECT * FROM retailpulse.gold.daily_metrics LIMIT 10;
