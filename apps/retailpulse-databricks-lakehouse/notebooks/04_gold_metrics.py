# Databricks notebook source
# MAGIC %md
# MAGIC # 04 Gold Metrics
# MAGIC 
# MAGIC Create aggregate metrics for dashboarding.

# COMMAND ----------
from retailpulse.event_generator import generate_events
from retailpulse.bronze import ingest_bronze
from retailpulse.silver import enrich_silver
from retailpulse.gold import aggregate_gold

raw_events = generate_events(10)
bronze_events = ingest_bronze(raw_events)
silver_events = enrich_silver(bronze_events)
metrics = aggregate_gold(silver_events)
print(metrics)
