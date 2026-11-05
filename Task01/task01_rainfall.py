
import random
import time


# Calculate weekly rainfall totals using slicing
def weekly_totals(readings):
    return [
        sum(readings[i:i + 7])
        for i in range(0, len(readings), 7)
    ]


# Naive 7-day moving average
def naive_moving_average(readings, window=7):
    if len(readings) < window:
        return []

    averages = []

    for i in range(len(readings) - window + 1):
        total = sum(readings[i:i + window])
        averages.append(total / window)

    return averages


# Running-sum 7-day moving average
def running_sum_moving_average(readings, window=7):
    if len(readings) < window:
        return []

    averages = []
    current_sum = sum(readings[:window])
    averages.append(current_sum / window)

    for i in range(window, len(readings)):
        current_sum += readings[i] - readings[i - window]
        averages.append(current_sum / window)

    return averages


# Find dry days
def find_dry_days(readings):
    return [
        day for day, value in enumerate(readings, start=1)
        if value == 0
    ]


# Performance comparison
def measure_performance():
    print("\nPERFORMANCE COMPARISON")

    for size in [365, 36500, 365000]:
        readings = [
            random.randint(0, 100) for _ in range(size)
        ]

        start = time.perf_counter()
        naive_moving_average(readings)
        naive_time = time.perf_counter() - start

        start = time.perf_counter()
        running_sum_moving_average(readings)
        running_time = time.perf_counter() - start

        print(f"\nReadings: {size}")
        print(f"Naive method: {naive_time:.6f} seconds")
        print(f"Running sum: {running_time:.6f} seconds")


# Main program
def main():
    random.seed(42)

    readings = [
        random.randint(0, 100) for _ in range(365)
    ]

    print("VILLAGE RAIN-GAUGE STATION")
    print("-" * 40)

    print("Total readings:", len(readings))

    # Weekly totals
    weeks = weekly_totals(readings)

    print("\nWeekly totals (first 5 weeks):", weeks[:5])
    print("Number of weekly totals:", len(weeks))

    # Wettest and driest weeks
    wettest_week = max(enumerate(weeks), key=lambda x: x[1])
    driest_week = min(enumerate(weeks), key=lambda x: x[1])

    print("\nWettest week:", wettest_week[0] + 1,
          "Total:", wettest_week[1], "mm")

    print("Driest week:", driest_week[0] + 1,
          "Total:", driest_week[1], "mm")

    # Moving averages
    naive = naive_moving_average(readings)
    running = running_sum_moving_average(readings)

    print("\n7-day moving averages (first 5):",
          [round(x, 2) for x in running[:5]])

    print("Both methods give same result:", naive == running)

    # Dry days
    dry_days = find_dry_days(readings)

    print("\nNumber of dry days:", len(dry_days))
    print("Dry days (first 10):", dry_days[:10])

    # Slicing demonstrations
    print("\nSLICING DEMONSTRATION")
    print("readings[7:14]:", readings[7:14])
    print("readings[-7:]:", readings[-7:])
    print("readings[::7]:", readings[::7][:10])

    # Edge cases
    print("\nEDGE CASE TESTING")
    print("Empty list:", naive_moving_average([]))
    print("Short list:",
          naive_moving_average([1, 2, 3, 4, 5]))

    # Performance tests
    measure_performance()


if __name__ == "__main__":
    main()
