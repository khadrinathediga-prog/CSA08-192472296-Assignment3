
import random
import time
import sys


# 1. Generate sensor readings
def generate_readings(size):
    return [
        random.uniform(-60, 60)
        for _ in range(size)
    ]


# 2. Clean readings using loop and append
def clean_with_loop(readings):
    valid = []

    for value in readings:
        if -50 <= value <= 50:
            valid.append(value)

    return valid


# 3. Clean readings using list comprehension
def clean_with_comprehension(readings):
    return [
        value for value in readings
        if -50 <= value <= 50
    ]


# 4. Clean readings using filter and lambda
def clean_with_filter(readings):
    return list(
        filter(lambda value: -50 <= value <= 50, readings)
    )


# 5. Convert Celsius to Fahrenheit
def convert_to_fahrenheit(readings):
    return [
        (value * 9 / 5) + 32
        for value in readings
    ]


# 6. Identify alarm minutes using original positions
def find_alarm_minutes(readings):
    return [
        minute
        for minute, temperature in enumerate(readings, start=1)
        if -50 <= temperature <= 50
        and (temperature < 2 or temperature > 8)
    ]


# 7. Dictionary comprehension
def create_temperature_dictionary(readings):
    return {
        index: temperature
        for index, temperature in enumerate(readings, start=1)
    }


# 8. Set comprehension
def unique_temperatures(readings):
    return {
        round(value, 2)
        for value in readings
    }


# 9. Performance comparison
def performance_comparison():
    print("\nPERFORMANCE COMPARISON")

    for size in [10000, 100000, 1000000]:
        readings = generate_readings(size)

        start = time.perf_counter()
        loop_result = clean_with_loop(readings)
        loop_time = time.perf_counter() - start

        start = time.perf_counter()
        comprehension_result = clean_with_comprehension(readings)
        comprehension_time = time.perf_counter() - start

        start = time.perf_counter()
        filter_result = clean_with_filter(readings)
        filter_time = time.perf_counter() - start

        print(f"\nReadings: {size}")
        print(f"Loop and append: {loop_time:.6f} seconds")
        print(f"List comprehension: {comprehension_time:.6f} seconds")
        print(f"Filter and lambda: {filter_time:.6f} seconds")

        print(
            "All methods give same result:",
            loop_result == comprehension_result == filter_result
        )

        print("Valid readings:", len(comprehension_result))


# 10. Memory comparison
def memory_comparison():
    print("\nMEMORY COMPARISON")

    readings = generate_readings(100000)

    list_result = clean_with_comprehension(readings)

    generator_result = (
        value for value in readings
        if -50 <= value <= 50
    )

    print("List memory:", sys.getsizeof(list_result), "bytes")
    print("Generator memory:", sys.getsizeof(generator_result), "bytes")


# 11. Edge case testing
def edge_case_testing():
    print("\nEDGE CASE TESTING")

    print("All valid readings:",
          clean_with_comprehension([2, 5, 10]))

    print("All invalid readings:",
          clean_with_comprehension([-100, 100, 75]))

    print("Empty readings:",
          clean_with_comprehension([]))

    print("Boundary readings:",
          clean_with_comprehension([-50, 50, -51, 51]))


# 12. Main program
def main():
    random.seed(42)

    print("SENSOR READING CLEANING SYSTEM")
    print("-" * 45)

    readings = [
        -60, -50, -10, 0, 2, 5, 8, 12, 25, 50, 60
    ]

    print("\nORIGINAL READINGS")
    print(readings)

    valid = clean_with_comprehension(readings)

    print("\nVALID READINGS (-50 to 50)")
    print(valid)

    fahrenheit = convert_to_fahrenheit(valid)

    print("\nFAHRENHEIT CONVERSION")
    print([round(value, 2) for value in fahrenheit])

    # Use original readings to preserve minute positions
    alarms = find_alarm_minutes(readings)

    print("\nALARM MINUTES (outside 2–8°C)")
    print(alarms)

    temperature_dict = create_temperature_dictionary(valid)

    print("\nDICTIONARY COMPREHENSION")
    print(temperature_dict)

    unique_values = unique_temperatures(valid)

    print("\nSET COMPREHENSION")
    print(sorted(unique_values))

    # Enumerate demonstration
    print("\nENUMERATE DEMONSTRATION")

    for minute, temperature in enumerate(valid, start=1):
        print(f"Minute {minute}: {temperature}°C")

    # Compare cleaning methods
    print("\nMETHOD COMPARISON")

    print("Loop result:", clean_with_loop(readings))
    print("Comprehension result:",
          clean_with_comprehension(readings))
    print("Filter result:", clean_with_filter(readings))

    edge_case_testing()

    memory_comparison()

    performance_comparison()


if __name__ == "__main__":
    main()
