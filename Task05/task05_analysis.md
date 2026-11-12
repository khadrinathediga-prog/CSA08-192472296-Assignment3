
# Q5 – List Comprehensions: Sensor Reading Cleaning System

## 1. Problem Analysis

The Sensor Reading Cleaning System processes temperature readings collected from sensors.

The objective is to remove invalid readings, convert valid Celsius readings into Fahrenheit, identify alarm minutes and compare different Python techniques.

The program demonstrates:
- For loop with append()
- List comprehension
- map() and filter() with lambda
- enumerate()
- Dictionary comprehension
- Set comprehension
- Generator expressions

## 2. Input Data

The program uses the following sensor readings:

```python
readings = [-60, -50, -10, 0, 2, 5, 8, 12, 25, 50, 60]
```

Valid readings are between -50 and 50, inclusive.

## 3. Data Cleaning Using Different Methods

### Method 1: For Loop and append()

```python
valid_loop = []

for value in readings:
    if -50 <= value <= 50:
        valid_loop.append(value)
```

This method checks each reading and appends valid values to a new list.

### Method 2: List Comprehension

```python
valid_comp = [
    value for value in readings
    if -50 <= value <= 50
]
```

List comprehension provides a concise way to create a filtered list.

### Method 3: filter() and lambda

```python
valid_filter = list(
    filter(lambda value: -50 <= value <= 50, readings)
)
```

The filter() function selects values satisfying the given condition.

All three methods produce identical results:

```text
[-50, -10, 0, 2, 5, 8, 12, 25, 50]
```

## 4. Fahrenheit Conversion Using map()

The Celsius readings are converted into Fahrenheit using the formula:

Fahrenheit = (Celsius × 9/5) + 32

The program demonstrates conversion using a loop, list comprehension and map().

```python
fahrenheit_map = list(
    map(lambda value: value * 9 / 5 + 32, valid_filter)
)
```

All three conversion methods produce identical results:

```text
[-58.0, 14.0, 32.0, 35.6, 41.0, 46.4, 53.6, 77.0, 122.0]
```

## 5. Alarm Minutes Using enumerate()

The enumerate() function provides both the index and value while iterating through a list.

```python
alarm_minutes = [
    minute
    for minute, value in enumerate(readings)
    if value > 10
]
```

The program identifies readings greater than 10.

Observed alarm positions:

```text
[7, 8, 9, 10]
```

These positions correspond to the readings 12, 25, 50 and 60.

## 6. Dictionary Comprehension

Dictionary comprehension creates a dictionary containing the status of each reading.

```python
reading_status = {
    minute: "ALERT" if value > 10 else "NORMAL"
    for minute, value in enumerate(readings)
}
```

Each reading is assigned either NORMAL or ALERT status.

## 7. Set Comprehension

Set comprehension creates a collection of unique readings.

```python
unique_readings = {value for value in readings}
```

Sets automatically remove duplicate values.

## 8. Performance Comparison

The program compares three filtering methods:
1. For loop with append()
2. List comprehension
3. filter() with lambda

### Experimental Results

| Input Size | Loop (seconds) | List Comprehension (seconds) | Filter (seconds) |
|---:|---:|---:|---:|
| 10,000 | 0.000484 | 0.000327 | 0.000442 |
| 100,000 | 0.005018 | 0.003579 | 0.004962 |
| 1,000,000 | 0.045482 | 0.032495 | 0.040501 |

### Observation

- List comprehension was the fastest method in all three experiments.
- The for loop was slightly slower.
- Filter with lambda performed between the other two methods.
- All three methods produced identical results.

Actual execution times may vary depending on hardware and system conditions.

## 9. Memory Comparison: List vs Generator

The program compares memory usage using sys.getsizeof().

| Structure | Memory Usage |
|---|---:|
| List | 800,984 bytes |
| Generator | 200 bytes |

### Observation

A list stores all generated elements in memory.

A generator produces values when requested rather than storing the complete collection.

Therefore, the generator uses significantly less container memory in this experiment.

Note: These measurements represent the objects measured by sys.getsizeof(), not the complete memory usage of all referenced elements.

## 10. Edge Case Testing

| Test Case | Input | Expected Result | Observed Result |
|---|---|---|---|
| All valid | [2, 5, 10] | All values retained | Passed |
| All invalid | [-80, 70, 100] | Empty list | Passed |
| Empty input | [] | Empty list | Passed |
| Boundary values | [-50, 50] | Both retained | Passed |

These tests verify that the filtering condition works correctly for different input conditions.

## 11. Time Complexity Analysis

Let n represent the number of sensor readings.

| Operation | Time Complexity |
|---|---|
| For loop filtering | O(n) |
| List comprehension | O(n) |
| filter() | O(n) |
| map() | O(n) |
| enumerate() | O(n) |
| Dictionary comprehension | O(n) |
| Set comprehension | O(n) |

The filtering methods examine each input element once.

The additional output storage for list-based filtering is O(n) in the worst case.

A generator can produce values lazily with O(1) additional iterator storage, excluding the input collection and generated values consumed by the caller.

## 12. Evaluation

The experiments demonstrate that list comprehension provides a concise and efficient approach to filtering sensor readings.

The map() function simplifies conversion operations, while filter() selects values based on conditions.

The enumerate() function is useful when both the position and value are required.

Generator expressions are useful when memory efficiency is important.

## 13. Conclusion

The Sensor Reading Cleaning System successfully demonstrates different Python data-processing techniques.

The program removes invalid sensor readings, converts Celsius values into Fahrenheit, identifies alarm positions and creates dictionary and set comprehensions.

The performance experiments show that list comprehension was the fastest filtering method in the recorded tests. The generator also used considerably less container memory than the list.

Therefore, list comprehensions are suitable for efficient list processing, while generators are useful for memory-efficient iteration.
