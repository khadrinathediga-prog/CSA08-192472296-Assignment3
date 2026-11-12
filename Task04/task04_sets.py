
import random
import time


# 1. Create elective registration sets
def create_registration_sets():
    elective_a = {
        "192311001",
        "192311004",
        "192311007",
        "192311009"
    }

    elective_b = {
        "192311002",
        "192311004",
        "192311009",
        "192311010"
    }

    all_students = {
        "192311001", "192311002", "192311003",
        "192311004", "192311005", "192311006",
        "192311007", "192311008", "192311009",
        "192311010"
    }

    return elective_a, elective_b, all_students


# 2. Demonstrate set operations
def analyze_registrations(elective_a, elective_b, all_students):
    clashes = elective_a & elective_b
    exactly_one = elective_a ^ elective_b
    neither = all_students - (elective_a | elective_b)

    print("\nELECTIVE REGISTRATION ANALYSIS")

    print("Elective A:", sorted(elective_a))
    print("Elective B:", sorted(elective_b))

    print("\nClashing students:", sorted(clashes))
    print("Exactly one elective:", sorted(exactly_one))
    print("Neither elective:", sorted(neither))

    print("\nUNION:", sorted(elective_a | elective_b))
    print("INTERSECTION:", sorted(elective_a & elective_b))
    print("A DIFFERENCE B:", sorted(elective_a - elective_b))
    print("B DIFFERENCE A:", sorted(elective_b - elective_a))
    print("SYMMETRIC DIFFERENCE:", sorted(elective_a ^ elective_b))


# 3. Demonstrate set methods
def demonstrate_set_methods(a, b):
    print("\nSET METHODS")

    print("Union:", sorted(a.union(b)))
    print("Intersection:", sorted(a.intersection(b)))
    print("Difference:", sorted(a.difference(b)))
    print("Symmetric difference:",
          sorted(a.symmetric_difference(b)))


# 4. Compare list and set membership
def membership_performance():
    print("\nLIST VS SET MEMBERSHIP PERFORMANCE")

    for size in [10000, 100000, 1000000]:
        numbers = list(range(size))
        number_set = set(numbers)
        target = size - 1
        repetitions = 1000

        start = time.perf_counter()
        for _ in range(repetitions):
            target in numbers
        list_time = time.perf_counter() - start

        start = time.perf_counter()
        for _ in range(repetitions):
            target in number_set
        set_time = time.perf_counter() - start

        print(f"\nSize: {size}")
        print(f"List membership: {list_time:.6f} seconds")
        print(f"Set membership: {set_time:.6f} seconds")


# 5. Compare nested loops and set intersection
def intersection_performance():
    print("\nNESTED LOOPS VS SET INTERSECTION")

    for size in [1000, 3000, 5000]:
        a = set(range(size))
        b = set(range(size // 2, size + size // 2))

        list_a = list(a)
        list_b = list(b)

        start = time.perf_counter()
        nested_result = []

        for x in list_a:
            for y in list_b:
                if x == y:
                    nested_result.append(x)

        nested_time = time.perf_counter() - start

        start = time.perf_counter()
        set_result = a & b
        set_time = time.perf_counter() - start

        print(f"\nSize: {size}")
        print(f"Nested loops: {nested_time:.6f} seconds")
        print(f"Set intersection: {set_time:.6f} seconds")
        print("Results match:", set(nested_result) == set_result)


# 6. Edge case testing
def edge_case_testing():
    print("\nEDGE CASE TESTING")

    empty_a = set()
    empty_b = set()

    print("Empty intersection:", sorted(empty_a & empty_b))

    same_a = {1, 2, 3}
    same_b = {1, 2, 3}

    print("Identical set intersection:",
          sorted(same_a & same_b))

    print("Identical set difference:",
          sorted(same_a - same_b))

    # Duplicate removal
    duplicate_list = [1, 2, 2, 3, 3, 3]
    print("Original list:", duplicate_list)
    print("After converting to set:", sorted(set(duplicate_list)))

    # Hashability test
    try:
        invalid_set = {[1, 2], [3, 4]}
    except TypeError as error:
        print("List inside set:", error)


# 7. Main program
def main():
    print("ELECTIVE REGISTRATION CLASH DETECTION")
    print("-" * 45)

    elective_a, elective_b, all_students = create_registration_sets()

    analyze_registrations(elective_a, elective_b, all_students)

    demonstrate_set_methods(elective_a, elective_b)

    edge_case_testing()

    membership_performance()

    intersection_performance()


if __name__ == "__main__":
    main()
