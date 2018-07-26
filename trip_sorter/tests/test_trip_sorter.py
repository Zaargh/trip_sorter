import pytest

from trip_sorter import sort_trip
from trip_sorter.sorter import _is_valid, InvalidTripException


def test_sort_trip():
    sorted_trip = [
        {"from": "Warsaw", "to": "Berlin", "info": "train, seat 249"},
        {"from": "Berlin", "to": "Helsinki", "info": "flight 34B, no seat"},
        {"from": "Helsinki", "to": "Miami", "info": "submarine cruise, bunk 5"},
        {"from": "Miami", "to": "Ottawa", "info": "horse carriage, seat 39"},
        {"from": "Ottawa", "to": "Osaka", "info": "flight, budget airlines, seat 092"},
        {"from": "Osaka", "to": "Buenos Aires", "info": "flight AS892, seat 19"},
        {"from": "Buenos Aires", "to": "Białystok", "info": "flight OP017"},
    ]
    unsorted_trip = [
        {"from": "Osaka", "to": "Buenos Aires", "info": "flight AS892, seat 19"},
        {"from": "Helsinki", "to": "Miami", "info": "submarine cruise, bunk 5"},
        {"from": "Buenos Aires", "to": "Białystok", "info": "flight OP017"},
        {"from": "Warsaw", "to": "Berlin", "info": "train, seat 249"},
        {"from": "Miami", "to": "Ottawa", "info": "horse carriage, seat 39"},
        {"from": "Ottawa", "to": "Osaka", "info": "flight, budget airlines, seat 092"},
        {"from": "Berlin", "to": "Helsinki", "info": "flight 34B, no seat"},
    ]

    assert sorted_trip == sort_trip(unsorted_trip)


def test_invalid_trip(invalid_trip):
    assert not _is_valid(invalid_trip)


def test_valid_trip():
    valid_trip = [
        {"from": "A", "to": "B", "info": "x"},
        {"from": "B", "to": "C", "info": "c"},
    ]
    assert _is_valid(valid_trip)


def test_trip_sorter_raises_exception_for_invalid_trip(invalid_trip):
    with pytest.raises(InvalidTripException):
        sort_trip(invalid_trip)
