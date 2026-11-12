
import random
import time
import sys


# --------------------------------------------------
# 1. Create sample timetable with 5 trains
# --------------------------------------------------

def create_sample_timetable():
    timetable = {
        "12601": {
            "name": "Chennai Express",
            "stops": [
                ("Chennai", "06:00", "06:15"),
                ("Vijayawada", "11:30", "11:40"),
                ("Warangal", "15:00", "15:05"),
                ("Hyderabad", "18:30", "18:45")
            ],
            "running_days": {"Monday", "Wednesday", "Friday"}
        },

        "12602": {
            "name": "Deccan Express",
            "stops": [
                ("Chennai", "07:00", "07:10"),
                ("Gudur", "09:00", "09:05"),
                ("Vijayawada", "12:00", "12:15"),
                ("Hyderabad", "19:00", "19:10")
            ],
            "running_days": {"Tuesday", "Thursday", "Saturday"}
        },

        "12701": {
            "name": "Charminar Express",
            "stops": [
                ("Chennai", "08:00", "08:10"),
                ("Nellore", "10:00", "10:05"),
                ("Vijayawada", "13:00", "13:10"),
                ("Hyderabad", "20:00", "20:15")
            ],
            "running_days": {
                "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"
            }
        },

        "12702": {
            "name": "Godavari Express",
            "stops": [
                ("Hyderabad", "05:30", "05:45"),
                ("Warangal", "08:00", "08:05"),
                ("Vijayawada", "11:00", "11:10"),
                ("Chennai", "17:00", "17:15")
            ],
            "running_days": {"Monday", "Thursday", "Sunday"}
        },

        "12801": {
            "name": "Coastal Express",
            "stops": [
                ("Chennai", "09:00", "09:15"),
                ("Gudur", "11:00", "11:05"),
                ("Nellore", "12:00", "12:05"),
                ("Vijayawada", "15:00", "15:15")
            ],
            "running_days": {"Tuesday", "Friday", "Sunday"}
        }
    }

    return timetable


# --------------------------------------------------
# 2. Search without station index
# --------------------------------------------------

def search_without_index(timetable, station, day):
    results = []

    for train_number, details in timetable.items():

        if day not in details["running_days"]:
            continue

        for stop in details["stops"]:
            if stop[0].lower() == station.lower():
                results.append({
                    "train_number": train_number,
                    "name": details["name"],
                    "arrival": stop[1],
                    "departure": stop[2]
                })
                break

    return results


# --------------------------------------------------
# 3. Build station index
# --------------------------------------------------

def build_station_index(timetable):
    station_index = {}

    for train_number, details in timetable.items():
        for station, arrival, departure in details["stops"]:
            station_index.setdefault(
                station.lower(), []
            ).append(train_number)

    return station_index


# --------------------------------------------------
# 4. Search using station index
# --------------------------------------------------

def search_with_index(timetable, station_index, station, day):
    results = []

    train_numbers = station_index.get(station.lower(), [])

    for train_number in train_numbers:
        details = timetable[train_number]

        if day not in details["running_days"]:
            continue

        for stop in details["stops"]:
            if stop[0].lower() == station.lower():
                results.append({
                    "train_number": train_number,
                    "name": details["name"],
                    "arrival": stop[1],
                    "departure": stop[2]
                })
                break

    return results


# --------------------------------------------------
# 5. Sort trains by departure time
# --------------------------------------------------

def sort_by_departure(results):
    return sorted(
        results,
        key=lambda train: train["departure"]
    )


# --------------------------------------------------
# 6. Print complete timetable
# --------------------------------------------------

def print_timetable(timetable):
    print("\nCOMPLETE RAILWAY TIMETABLE")
    print("=" * 65)

    for train_number, details in timetable.items():
        print(f"\nTrain Number: {train_number}")
        print(f"Train Name  : {details['name']}")
        print("Running Days:", ", ".join(
            sorted(details["running_days"])
        ))

        print("Station          Arrival    Departure")

        for station, arrival, departure in details["stops"]:
            print(f"{station:<17} {arrival:<10} {departure}")


# --------------------------------------------------
# 7. Display search results
# --------------------------------------------------

def display_results(results):
    if not results:
        print("No trains found.")
        return

    print("\nTrain Number   Train Name          Arrival   Departure")

    for train in results:
        print(
            f"{train['train_number']:<14}"
            f"{train['name']:<20}"
            f"{train['arrival']:<10}"
            f"{train['departure']}"
        )


# --------------------------------------------------
# 8. Generate large timetable for testing
# --------------------------------------------------

def generate_large_timetable(number_of_trains):
    stations = [
        "Central", "Chennai", "Hyderabad", "Vijayawada",
        "Warangal", "Nellore", "Gudur", "Bangalore",
        "Mumbai", "Delhi"
    ]

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    timetable = {}

    for i in range(number_of_trains):
        train_number = f"T{i + 1:05d}"

        selected_stations = random.sample(stations[1:], 3)

        route = ["Central"] + selected_stations
        stops = []

        for position, station in enumerate(route):
            hour = 5 + position * 2 + (i % 3)
            arrival = f"{hour:02d}:00"
            departure = f"{hour:02d}:10"

            stops.append((station, arrival, departure))

        running_days = set(random.sample(days, 4))

        timetable[train_number] = {
            "name": f"Express {i + 1}",
            "stops": stops,
            "running_days": running_days
        }

    return timetable


# --------------------------------------------------
# 9. Performance comparison
# --------------------------------------------------

def performance_comparison():
    print("\nPERFORMANCE COMPARISON")
    print("=" * 65)

    random.seed(42)

    for size in [100, 1000, 10000]:
        timetable = generate_large_timetable(size)

        start = time.perf_counter()
        station_index = build_station_index(timetable)
        index_build_time = time.perf_counter() - start

        station = "Hyderabad"
        day = "Monday"

        normal_result = search_without_index(
            timetable, station, day
        )

        indexed_result = search_with_index(
            timetable, station_index, station, day
        )

        assert normal_result == indexed_result

        repetitions = 100

        start = time.perf_counter()
        for _ in range(repetitions):
            search_without_index(timetable, station, day)
        normal_time = time.perf_counter() - start

        start = time.perf_counter()
        for _ in range(repetitions):
            search_with_index(
                timetable, station_index, station, day
            )
        indexed_time = time.perf_counter() - start

        index_memory = sys.getsizeof(station_index)

        for key, value in station_index.items():
            index_memory += sys.getsizeof(key)
            index_memory += sys.getsizeof(value)

            for train_number in value:
                index_memory += sys.getsizeof(train_number)

        print(f"\nNumber of trains: {size}")
        print(f"Station index build time: {index_build_time:.6f} seconds")
        print(
            f"Without index ({repetitions} queries): "
            f"{normal_time:.6f} seconds"
        )
        print(
            f"With index ({repetitions} queries): "
            f"{indexed_time:.6f} seconds"
        )
        print("Results match:", normal_result == indexed_result)
        print(f"Trains stopping at {station}: {len(indexed_result)}")
        print("Station index memory:", index_memory, "bytes")


# --------------------------------------------------
# 10. Edge case testing
# --------------------------------------------------

def edge_case_testing(timetable, station_index):
    print("\nEDGE CASE TESTING")

    print("\nUnknown station:")
    result = search_with_index(
        timetable, station_index,
        "Unknown Station", "Monday"
    )
    display_results(result)

    print("\nTrain does not run on the selected day:")
    result = search_with_index(
        timetable, station_index, "Gudur", "Monday"
    )
    display_results(result)


# --------------------------------------------------
# 11. Main program
# --------------------------------------------------

def main():
    timetable = create_sample_timetable()

    print("RAILWAY ENQUIRY COUNTER")
    print("=" * 65)

    print_timetable(timetable)

    station_index = build_station_index(timetable)

    station = "Vijayawada"
    day = "Monday"

    print(
        f"\nTRAINS STOPPING AT {station.upper()} ON {day.upper()}"
    )

    results = search_with_index(
        timetable, station_index, station, day
    )

    sorted_results = sort_by_departure(results)
    display_results(sorted_results)

    print("\nNESTED DATA ACCESS")
    print("Train 12601:", timetable["12601"]["name"])
    print(
        "Departure from the third station:",
        timetable["12601"]["stops"][2][2]
    )

    edge_case_testing(timetable, station_index)

    performance_comparison()


if __name__ == "__main__":
    main()
