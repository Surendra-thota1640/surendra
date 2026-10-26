# Databricks notebook source
# MAGIC %md
# MAGIC # 03 Silver Stream
# MAGIC 
# MAGIC Enrich and standardize bronze events.

# COMMAND ----------
from retailpulse.event_generator import generate_events
from retailpulse.bronze import ingest_bronze
from retailpulse.silver import enrich_silver

raw_events = generate_events(10)
bronze_events = ingest_bronze(raw_events)
silver_events = enrich_silver(bronze_events)
print(f"Processed {len(silver_events)} silver records.")
