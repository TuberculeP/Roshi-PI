word_map = {
    "un": 1,
    "deux": 2,
    "trois": 3,
    "quatre": 4,
    "cinq": 5,
    "six": 6,
    "sept": 7,
    "huit": 8,
    "neuf": 9,
    "dix": 10,
    "onze": 11,
    "douze": 12,
    "treize": 13,
    "quatorze": 14,
    "quinze": 15,
    "seize": 16,
}


def mot2chiffre(mot: str) -> int | None:
    """Convert a word to a number for simple numbers.
    :param mot: str
    :return: int or None"""
    if mot in word_map:
        return word_map[mot]
    return None
