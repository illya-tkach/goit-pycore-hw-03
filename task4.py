from datetime import date, datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"
DAYS_AHEAD = 7


def _birthday_in_year(birthday: date, year: int) -> date:
    """Return the birthday in the given year (Feb 29 -> Mar 1 in non-leap years)."""
    try:
        return birthday.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def get_upcoming_birthdays(users: list[dict], today: date | None = None) -> list[dict]:
    """Find birthdays within the next 7 days (today included).

    Congratulations that fall on a weekend are moved to the next Monday.

    Args:
        users: List of dicts with 'name' and 'birthday' ('YYYY.MM.DD').
        today: Date to count from; defaults to the current date.

    Returns:
        List of dicts with 'name' and 'congratulation_date' ('YYYY.MM.DD').
    """
    today = today or datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], DATE_FORMAT).date()

        birthday_this_year = _birthday_in_year(birthday, today.year)
        if birthday_this_year < today:
            birthday_this_year = _birthday_in_year(birthday, today.year + 1)

        if (birthday_this_year - today).days > DAYS_AHEAD:
            continue

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() >= 5:  # Saturday or Sunday
            congratulation_date += timedelta(days=7 - congratulation_date.weekday())

        upcoming.append(
            {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
            }
        )

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    print("Список привітань на цьому тижні:", get_upcoming_birthdays(users, date(2024, 1, 22)))
    print("Сьогодні:", get_upcoming_birthdays(users))
