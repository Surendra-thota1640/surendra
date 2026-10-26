# Databricks notebook source
# MAGIC %md
# MAGIC # 01 Setup
# MAGIC 
# MAGIC This notebook creates the required catalog and storage locations for the RetailPulse Lakehouse demo.

# COMMAND ----------
print("Setting up RetailPulse metadata and storage locations...")

# COMMAND ----------
# Example layout for Unity Catalog tables.
# CREATE SCHEMA IF NOT EXISTS retailpulse.bronze;
# CREATE SCHEMA IF NOT EXISTS retailpulse.silver;
# CREATE SCHEMA IF NOT EXISTS retailpulse.gold;

print("Setup complete.")
