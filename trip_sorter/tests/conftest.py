import pytest


@pytest.fixture()
def invalid_trip():
    return [
        {"from": "A", "to": "B", "info": "x"},
        {"from": "Z", "to": "Y", "info": "c"},
    ]
