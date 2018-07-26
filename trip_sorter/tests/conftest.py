import pytest

INVALID_TRIPS = [
    [  # no connection
        {"from": "A", "to": "B", "info": "x"},
        {"from": "Z", "to": "Y", "info": "c"},
    ],
    [  # loop in trip
        {"from": "A", "to": "B", "info": "x"},
        {"from": "B", "to": "C", "info": "c"},
        {"from": "C", "to": "B", "info": "x"},
        {"from": "B", "to": "Y", "info": "c"},
    ],
    [  # whole trip is a loop
        {"from": "A", "to": "B", "info": "x"},
        {"from": "B", "to": "C", "info": "c"},
        {"from": "C", "to": "D", "info": "x"},
        {"from": "D", "to": "A", "info": "c"},
    ],
]


@pytest.fixture(params=INVALID_TRIPS)
def invalid_trip(request):
    return request.param
