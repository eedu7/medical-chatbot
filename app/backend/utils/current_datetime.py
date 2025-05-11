from datetime import datetime, UTC


def get_current_datetime() -> datetime:
    return datetime.now(UTC)
