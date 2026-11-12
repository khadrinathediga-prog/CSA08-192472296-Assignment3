# Task 06 – Nested Data: A Railway Timetable

## 1. Aim
To implement a railway timetable using nested Python data structures and compare station searches with and without a station index.

## 2. Design

The timetable uses a nested dictionary structure.

```python
timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:15"),
            ("Vijayawada", "11:30", "11:40"),
            ("Warangal", "15:00", "15:05")
        ],
        "running_days": {"Monday", "Wednesday", "Friday"}
    }
}
```

The expression to access the departure time of the third station is:

`timetable["12601"]["stops"][2][2]`

It returns `15:05`.

## 3. Implementation

The program implements the following operations:

- Builds a timetable containing five trains.
- Stores train details in nested dictionaries.
- Stores station details as a list of tuples.
- Stores running days using sets.
- Finds trains stopping at a specified station on a given day.
- Sorts matching trains by departure time using `sorted()` and `lambda`.
- Prints the timetable in a readable format.
- Builds a station index to improve repeated searches.
- Tests large timetables containing 100, 1,000 and 10,000 trains.

## 4. Data Structure Analysis

| Data structure | Purpose |
|---|---|
| Dictionary | Stores train details using train numbers as keys |
| List | Maintains stations in route order |
| Tuple | Stores station, arrival and departure information |
| Set | Stores running days and avoids duplicate days |
| Station index dictionary | Maps station names to train numbers |

### Station query complexity

Without an index, the program scans trains and their stops.

Time complexity: O(T × S), where T is the number of trains and S is the average number of stops.

With a station index, the search checks only trains listed for the requested station.

Approximate query complexity: O(K × S), where K is the number of trains stopping at the station.

Index construction requires O(T × S) time and additional memory proportional to the total number of indexed station-train entries.

## 5. Experimental Investigation

The program was tested with 100, 1,000 and 10,000 trains. Each timing represents 100 station queries.

| Number of trains | Without index | With index | Index memory |
|---:|---:|---:|---:|
| 100 | 0.001990 s | 0.000652 s | 23,667 bytes |
| 1,000 | 0.017803 s | 0.006488 s | 223,459 bytes |
| 10,000 | 0.181993 s | 0.072553 s | 2,229,955 bytes |

All search results matched between the two methods.

The indexed method was approximately three times faster in these tests.

## 6. Edge Case Testing

The program tested:

1. Unknown station: The program displays `No trains found.`
2. Station with no train operating on the selected day: The program displays `No trains found.`
3. Matching station and day: The program displays the matching trains.
4. Sorting: Matching trains are ordered by departure time.

## 7. Alternative Concept

An alternative approach is to store all timetable stops in one flat list of tuples:

`(train, station, arrival, departure, days)`

Every query would scan the complete list.

- Flat-list search: O(total stops) per query.
- Indexed search: O(trains at the station × stops per train) approximately.
- Flat-list storage avoids the extra station index.
- Indexed storage requires additional memory but makes repeated station queries faster.

## 8. Conclusion

The station index improves repeated railway timetable searches by reducing the number of trains that must be examined. The experiments showed faster indexed searches for all three tested timetable sizes. However, the index requires additional memory and time to build. Therefore, it is useful when the timetable receives frequent station queries.
