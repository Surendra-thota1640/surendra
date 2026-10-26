from retailpulse.event_generator import generate_events


def test_generate_events_returns_expected_count():
    events = generate_events(12)
    assert len(events) == 12
    assert all("event_id" in event for event in events)


def test_generate_events_include_numeric_amount():
    events = generate_events(5)
    assert all(isinstance(event["amount"], float) for event in events)
