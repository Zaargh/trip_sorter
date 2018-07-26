from typing import Iterable


def all_unique(iterable: Iterable):
    seen = set()
    return not any(i in seen or seen.add(i) for i in iterable)
