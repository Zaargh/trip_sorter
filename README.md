# Trip Sorter

The repository contains a simple Python trip sorting API for a perspective employer.
 
 ## Usage
 1. `from trip_sorter import TripSorter`
 1. `sorter = TripSorter(input_data)`
 1. `result = sorter.run()`
 
 `run()` method will either return sorted trip in the same format as input data, or raise `TripSorterException` if trip in `input_data` is invalid. 
 
 #### Data format
 `input_data` MUST be a Python list of dictionaries describing trip legs. Each dict MUST have values for  `"from"` and `"to"` keys. 
 Other keys and their values do not affect program behavior and are returned "as is".
 
 Example:
 ```python
>>> input_data =  [
        {"from": "Warsaw", "to": "Berlin", "info": "train, seat 249"},
        {"from": "Berlin", "to": "Helsinki", "info": "flight 34B, no seat"},
        {"from": "Helsinki", "to": "Miami", "info": "submarine cruise, bunk 5"},
        {"from": "Miami", "to": "Ottawa", "info": "horse carriage, seat 39"},
        {"from": "Ottawa", "to": "Osaka", "info": "flight, budget airlines, seat 092"},
        {"from": "Osaka", "to": "Buenos Aires", "info": "flight AS892, seat 19"},
        {"from": "Buenos Aires", "to": "Białystok", "info": "flight OP017"},
    ]
    
>>> TripSorter(input_data).run()
[
    {"from": "Osaka", "to": "Buenos Aires", "info": "flight AS892, seat 19"},
    {"from": "Helsinki", "to": "Miami", "info": "submarine cruise, bunk 5"},
    {"from": "Buenos Aires", "to": "Białystok", "info": "flight OP017"},
    {"from": "Warsaw", "to": "Berlin", "info": "train, seat 249"},
    {"from": "Miami", "to": "Ottawa", "info": "horse carriage, seat 39"},
    {"from": "Ottawa", "to": "Osaka", "info": "flight, budget airlines, seat 092"},
    {"from": "Berlin", "to": "Helsinki", "info": "flight 34B, no seat"},
]
```

## Running tests
`PYTHONPATH=. pytest` should do the trick.