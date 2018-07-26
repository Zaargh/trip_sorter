from typing import Dict, List


class InvalidTripException(Exception):
    pass


def sort_trip(unsorted_trip: List[Dict]):
    """ Returns sorted trip. If trip is invalid, raises InvalidTripException
    """
    if not _is_valid(unsorted_trip):
        raise InvalidTripException


def _is_valid(unsorted_trip: List[Dict]):
    starts = [x["from"] for x in unsorted_trip]
    destinations = [x["to"] for x in unsorted_trip]

    # Assuming that there are no loops in the trip.
    if len(starts) != len(set(starts)) or len(destinations) != len(set(destinations)):
        return False

    start = set(starts) - set(destinations)
    destination = set(destinations) - set(starts)

    if len(start) != 1 or len(destination) != 1:
        return False

    return True
