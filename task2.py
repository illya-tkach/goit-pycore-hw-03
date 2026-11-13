import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Generate a sorted list of unique random numbers for a lottery ticket.

    Args:
        min: Smallest possible number (at least 1).
        max: Largest possible number (at most 1000).
        quantity: How many numbers to pick (from 1 to the size of the range).

    Returns:
        Sorted list of `quantity` unique numbers in [min, max],
        or an empty list if the parameters are invalid.
    """
    params = (min, max, quantity)
    if not all(isinstance(p, int) and not isinstance(p, bool) for p in params):
        return []
    if min < 1 or max > 1000 or min > max:
        return []
    if not 1 <= quantity <= max - min + 1:
        return []

    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
    print(get_numbers_ticket(0, 49, 6))
    print(get_numbers_ticket(1, 5, 10))
