
import copy
import sys
import time


# 1. City bus-stop map using tuples
def create_bus_stop_map():
    bus_stops = {
        ("North", "Zone A"): ("Central", "Park Street"),
        ("North", "Zone B"): ("City Hospital", "Library"),
        ("South", "Zone A"): ("Railway Station", "Market"),
        ("South", "Zone B"): ("College", "Bus Terminal"),
    }

    return bus_stops


# 2. Create a grid using independent rows
def create_grid(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


# 3. Demonstrate aliasing, shallow copy and deep copy
def demonstrate_copying():
    original = [[1, 2], [3, 4]]

    # Aliasing
    alias = original

    # Shallow copies
    shallow_copy = copy.copy(original)
    slicing_copy = original[:]

    # Deep copy
    deep_copy = copy.deepcopy(original)

    original[0][0] = 99

    print("\nCOPYING DEMONSTRATION")
    print("Original:", original)
    print("Alias:", alias)
    print("Shallow copy:", shallow_copy)
    print("Slicing copy:", slicing_copy)
    print("Deep copy:", deep_copy)

    print("Alias is original:", alias is original)
    print("Shallow copy is original:", shallow_copy is original)
    print("Deep copy is original:", deep_copy is original)


# 4. Demonstrate incorrect and correct 2D grid creation
def demonstrate_grid():
    print("\n2D GRID DEMONSTRATION")

    # Incorrect method: all rows refer to the same list
    wrong_grid = [[0] * 3] * 3

    wrong_grid[0][0] = 99

    print("Incorrect grid:", wrong_grid)
    print("All rows share same object:",
          wrong_grid[0] is wrong_grid[1])

    # Correct method: independent rows
    correct_grid = [[0 for _ in range(3)] for _ in range(3)]

    correct_grid[0][0] = 99

    print("Correct grid:", correct_grid)
    print("Rows share same object:",
          correct_grid[0] is correct_grid[1])


# 5. Demonstrate tuple unpacking
def demonstrate_tuple_unpacking():
    stop = ("Central Station", "Zone A", 12)

    name, zone, bus_number = stop

    print("\nTUPLE UNPACKING")
    print("Stop name:", name)
    print("Zone:", zone)
    print("Bus number:", bus_number)


# 6. Demonstrate tuple dictionary keys
def demonstrate_dictionary_keys(bus_stops):
    print("\nTUPLE DICTIONARY KEYS")

    location = ("North", "Zone A")

    print("Bus stops at", location, ":", bus_stops[location])

    try:
        invalid_key = [1, 2]
        sample = {invalid_key: "Bus stop"}
    except TypeError as error:
        print("List as dictionary key:", error)


# 7. Demonstrate mutable objects inside tuples
def demonstrate_mutable_tuple():
    data = ("Bus Route 10", ["Central", "Market"])

    print("\nMUTABLE LIST INSIDE TUPLE")
    print("Before modification:", data)

    data[1].append("College")

    print("After modification:", data)


# 8. Memory comparison
def memory_comparison():
    print("\nMEMORY COMPARISON")

    list_data = list(range(1_000_000))
    tuple_data = tuple(range(1_000_000))

    print("List container memory:",
          sys.getsizeof(list_data), "bytes")

    print("Tuple container memory:",
          sys.getsizeof(tuple_data), "bytes")

    print("Note: These values measure container size,")
    print("not the complete memory of referenced integer objects.")


# 9. Creation and indexing time comparison
def time_comparison():
    print("\nTIME COMPARISON")

    size = 100_000
    repetitions = 5

    # List creation
    start = time.perf_counter()
    for _ in range(repetitions):
        list_data = list(range(size))
    list_time = time.perf_counter() - start

    # Tuple creation
    start = time.perf_counter()
    for _ in range(repetitions):
        tuple_data = tuple(range(size))
    tuple_time = time.perf_counter() - start

    print("List creation time:", round(list_time, 6), "seconds")
    print("Tuple creation time:", round(tuple_time, 6), "seconds")

    # Indexing comparison
    list_data = list(range(size))
    tuple_data = tuple(range(size))

    start = time.perf_counter()
    for _ in range(100_000):
        value = list_data[50_000]
    list_index_time = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(100_000):
        value = tuple_data[50_000]
    tuple_index_time = time.perf_counter() - start

    print("List indexing time:", round(list_index_time, 6), "seconds")
    print("Tuple indexing time:", round(tuple_index_time, 6), "seconds")


# 10. Main program
def main():
    print("CITY BUS-STOP MAP")
    print("-" * 40)

    bus_stops = create_bus_stop_map()

    for location, stops in bus_stops.items():
        print(location, ":", stops)

    demonstrate_dictionary_keys(bus_stops)

    demonstrate_tuple_unpacking()

    demonstrate_copying()

    demonstrate_grid()

    demonstrate_mutable_tuple()

    # Test independent rows
    print("\nINDEPENDENT ROW TEST")
    grid = create_grid(3, 3)
    grid[0][0] = 100
    print("Grid after modification:", grid)
    print("Independent rows:",
          grid[0] is not grid[1] and grid[1] is not grid[2])

    print("\nIDENTITY TEST")
    a = [1, 2, 3]
    b = a
    c = a[:]

    print("a is b:", a is b)
    print("a is c:", a is c)
    print("ID of a:", id(a))
    print("ID of b:", id(b))
    print("ID of c:", id(c))

    memory_comparison()
    time_comparison()

    # Sparse dictionary alternative
    print("\nSPARSE GRID ALTERNATIVE")
    sparse_grid = {
        (0, 0): "Central",
        (1, 2): "Market",
        (2, 1): "College"
    }

    print("Sparse grid:", sparse_grid)
    print("Stop at (1, 2):", sparse_grid.get((1, 2), "Empty"))


if __name__ == "__main__":
    main()
