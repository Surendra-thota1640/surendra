from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class RetailPulseConfig:
    project_name: str = "retailpulse-databricks-lakehouse"
    raw_zone: str = "raw"
    bronze_zone: str = "bronze"
    silver_zone: str = "silver"
    gold_zone: str = "gold"
    checkpoint_path: str = "/tmp/retailpulse/checkpoints"


def get_config() -> RetailPulseConfig:
    return RetailPulseConfig(
        project_name=os.getenv("PROJECT_NAME", "retailpulse-databricks-lakehouse"),
        raw_zone=os.getenv("RAW_ZONE", "raw"),
        bronze_zone=os.getenv("BRONZE_ZONE", "bronze"),
        silver_zone=os.getenv("SILVER_ZONE", "silver"),
        gold_zone=os.getenv("GOLD_ZONE", "gold"),
        checkpoint_path=os.getenv("CHECKPOINT_PATH", "/tmp/retailpulse/checkpoints"),
    )


def ensure_paths() -> None:
    Path(get_config().checkpoint_path).mkdir(parents=True, exist_ok=True)
