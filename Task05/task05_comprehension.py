
import time
import sys

print("SENSOR READING CLEANING SYSTEM")

# Original sensor readings
readings = [-60, -50, -10, 0, 2, 5, 8, 12, 25, 50, 60]

print("\nORIGINAL READINGS:", readings)

# 1. Using for loop and append()
valid_loop = []
for value in readings:
    if -50 <= value <= 50:
        valid_loop.append(value)

print("\nVALID READINGS USING LOOP:", valid_loop)

# 2. Using list comprehension
valid_comp = [
    value for value in readings
    if -50 <= value <= 50
]

print("VALID READINGS USING COMPREHENSION:", valid_comp)

# 3. Using filter() and lambda
valid_filter = list(
    filter(lambda value: -50 <= value <= 50, readings)
)

print("VALID READINGS USING FILTER:", valid_filter)

# 4. Using map() and lambda for Fahrenheit conversion
fahrenheit_loop = []
for value in valid_loop:
    fahrenheit_loop.append(value * 9 / 5 + 32)

fahrenheit_comp = [
    value * 9 / 5 + 32 for value in valid_comp
]

fahrenheit_map = list(
    map(lambda value: value * 9 / 5 + 32, valid_filter)
)

print("\nFAHRENHEIT USING LOOP:", fahrenheit_loop)
print("FAHRENHEIT USING COMPREHENSION:", fahrenheit_comp)
print("FAHRENHEIT USING MAP:", fahrenheit_map)

# 5. Alarm minutes using enumerate()
alarm_minutes = [
    minute
    for minute, value in enumerate(readings)
    if value > 10
]

print("\nALARM MINUTES:", alarm_minutes)

# 6. Dictionary comprehension
reading_status = {
    minute: "ALERT" if value > 10 else "NORMAL"
    for minute, value in enumerate(readings)
}

print("\nDICTIONARY COMPREHENSION:", reading_status)

# 7. Set comprehension
unique_readings = {value for value in readings}

print("\nSET COMPREHENSION:", unique_readings)

# 8. Method comparison
print("\nMETHOD COMPARISON")
print("Loop and comprehension match:", valid_loop == valid_comp)
print("Loop and filter match:", valid_loop == valid_filter)
print("All Fahrenheit results match:",
      fahrenheit_loop == fahrenheit_comp == fahrenheit_map)

# 9. Edge case testing
all_valid = [2, 5, 10]
all_invalid = [-80, 70, 100]
empty_readings = []
boundary_readings = [-50, 50]

def clean_data(data):
    return [value for value in data if -50 <= value <= 50]

print("\nEDGE CASE TESTING")
print("All valid:", clean_data(all_valid))
print("All invalid:", clean_data(all_invalid))
print("Empty input:", clean_data(empty_readings))
print("Boundary values:", clean_data(boundary_readings))

# 10. Memory comparison: list vs generator
sample_data = range(100000)

list_data = [x * 2 for x in sample_data]
generator_data = (x * 2 for x in sample_data)

print("\nMEMORY COMPARISON")
print("List memory:", sys.getsizeof(list_data), "bytes")
print("Generator memory:", sys.getsizeof(generator_data), "bytes")

# 11. Performance testing
print("\nPERFORMANCE TESTING")

for size in [10000, 100000, 1000000]:
    data = [i % 120 - 60 for i in range(size)]

    # Loop method
    start = time.perf_counter()
    result_loop = []
    for value in data:
        if -50 <= value <= 50:
            result_loop.append(value)
    loop_time = time.perf_counter() - start

    # List comprehension method
    start = time.perf_counter()
    result_comp = [
        value for value in data
        if -50 <= value <= 50
    ]
    comp_time = time.perf_counter() - start

    # Filter and lambda method
    start = time.perf_counter()
    result_filter = list(
        filter(lambda value: -50 <= value <= 50, data)
    )
    filter_time = time.perf_counter() - start

    print(f"\nInput size: {size}")
    print(f"Loop time: {loop_time:.6f} seconds")
    print(f"Comprehension time: {comp_time:.6f} seconds")
    print(f"Filter time: {filter_time:.6f} seconds")
    print("All methods produce identical results:",
          result_loop == result_comp == result_filter)

print("\nQ5 EXECUTION COMPLETED SUCCESSFULLY")
