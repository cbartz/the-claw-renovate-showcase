from datetime import date

from dateutil.parser import isoparse
from pydantic import BaseModel


class DependencyEvent(BaseModel):
    name: str
    opened_on: date


def test_pydantic_v1_model_parses_date():
    event = DependencyEvent(name="requests", opened_on="2026-05-13")

    assert event.name == "requests"
    assert event.opened_on == date(2026, 5, 13)


def test_dateutil_parses_utc_timestamp():
    parsed = isoparse("2026-05-13T10:30:00Z")

    assert parsed.year == 2026
    assert parsed.tzinfo is not None
