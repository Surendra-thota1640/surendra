from retailpulse.bronze import ingest_bronze
from retailpulse.event_generator import generate_events
from retailpulse.gold import aggregate_gold
from retailpulse.silver import enrich_silver


def test_transformations_pipeline_flow():
    raw_events = generate_events(10)
    bronze = ingest_bronze(raw_events)
    silver = enrich_silver(bronze)
    gold = aggregate_gold(silver)

    assert len(bronze) == 10
    assert len(silver) == 10
    assert "total_revenue" in gold
    assert "top_products" in gold
