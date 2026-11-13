import re


def normalize_phone(phone_number: str) -> str:
    """Normalize a phone number for SMS delivery.

    Removes everything except digits, then adds the Ukrainian country code:
    - number with a leading '+' keeps its code;
    - number starting with '380' gets only '+';
    - any other number gets '+38'.

    Args:
        phone_number: Phone number in an arbitrary format.

    Returns:
        Normalized number, e.g. '+380501234567'.
    """
    has_plus = phone_number.strip().startswith("+")
    digits = re.sub(r"\D", "", phone_number)

    if has_plus or digits.startswith("380"):
        return "+" + digits
    return "+38" + digits


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
