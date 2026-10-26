# RetailPulse Databricks Lakehouse

This project provides a starter Databricks Lakehouse pipeline for retail analytics. It includes dataset generation, bronze/silver/gold processing, notebook examples, and unit tests.

## Project layout

- `src/retailpulse/` contains Python modules for event generation and transformations.
- `notebooks/` contains Databricks notebook examples.
- `resources/` contains job definitions.
- `tests/` contains unit tests.
- `docs/` contains design and data documentation.

## Prerequisites

- Python 3.10+
- Databricks workspace access
- Databricks CLI configured (`databricks auth login`)

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
```

## Deployment

```bash
databricks bundle validate
# or
# databricks bundle deploy
```

## Notes

This is a starter kit for demo and learning purposes. Extend it with real ingestion, schema validation, and CI/CD integration as needed.
