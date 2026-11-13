from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """Return the number of days from the given date to today.

    Args:
        date: Date string in the 'YYYY-MM-DD' format.

    Returns:
        Whole number of days between `date` and today. The result is negative
        if `date` is in the future. Time of day is ignored.
        Returns None if `date` has an invalid format.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print(f"Невірний формат дати: {date!r}. Очікується 'РРРР-ММ-ДД'.")
        return None

    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2999-01-01"))
    print(get_days_from_today("09.10.2021"))
