# Databricks notebook source
# MAGIC %md
# MAGIC # 02 Bronze Stream
# MAGIC 
# MAGIC Ingest raw events into the bronze layer.

# COMMAND ----------
from retailpulse.event_generator import generate_events
from retailpulse.bronze import ingest_bronze

raw_events = generate_events(10)
bronze_events = ingest_bronze(raw_events)
print(f"Loaded {len(bronze_events)} bronze events.")
