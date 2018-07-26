from typing import Dict, List

from trip_sorter.utils import all_unique


class TripSorterException(Exception):
    pass


class TripSorter:
    def __init__(self, unsorted_trip: List[Dict]):
        self.unsorted_trip = unsorted_trip
        self.trip_legs_by_start = {t["from"]: t for t in self.unsorted_trip}

    def run(self):
        """ Returns sorted trip. If trip is invalid, raises TripSorterException
        """
        self._check_duplicates()

        # evaluate properties to run validation
        start = self._start
        destination = self._destination

        sorted_trip = []
        current_location = start
        while self.trip_legs_by_start:
            current_leg = self.trip_legs_by_start.pop(current_location)
            sorted_trip.append(current_leg)
            current_location = current_leg["to"]

        return sorted_trip

    @property
    def _starts(self):
        return [x["from"] for x in self.unsorted_trip]

    @property
    def _destinations(self):
        return [x["to"] for x in self.unsorted_trip]

    @property
    def _start(self):
        s = set(self._starts) - set(self._destinations)
        if len(s) != 1:
            raise TripSorterException("Cannot determine trip start.")
        return s.pop()

    @property
    def _destination(self):
        d = set(self._destinations) - set(self._starts)
        if len(d) != 1:
            raise TripSorterException("Cannot determine trip start.")
        return d.pop()

    def _check_duplicates(self):
        """ Check weather there are duplicates in starts or destinations.
        This would mean there's a loop in the trip, and that's not allowed
        for now.
        """
        if not all_unique(self._starts) or not all_unique(self._destinations):
            raise TripSorterException("There are duplicates in starts or destinations")
