# Task 05 – List Comprehension: Cleaning Sensor Readings

## 1. Aim
To clean invalid sensor readings using list comprehensions and compare their performance with traditional loops and filter functions.

## 2. Design
The program processes temperature readings collected from sensors. Valid readings are between -50°C and 50°C. It uses list, dictionary, and set comprehensions to process and organize the data.

## 3. Implementation
The program implements the following operations:

- Generates sensor readings using random values.
- Filters valid readings between -50°C and 50°C.
- Converts Celsius temperatures into Fahrenheit.
- Identifies alarm minutes for valid temperatures outside the safe range of 2°C to 8°C.
- Uses `enumerate()` to track reading positions.
- Creates dictionaries using dictionary comprehension.
- Finds unique temperatures using set comprehension.
- Compares loop-and-append, list comprehension, and filter with lambda.
- Compares list and generator memory usage.

General list comprehension syntax:

`[expression for item in iterable if condition]`

## 4. Analysis

### Time Complexity
- Cleaning using a loop: O(n)
- List comprehension: O(n)
- Filter operation: O(n)
- Fahrenheit conversion: O(n)
- Dictionary comprehension: O(n)
- Set comprehension: O(n) average case

Here, n represents the number of sensor readings.

### Memory Comparison
The list stores all filtered values in memory, while a generator produces values when needed.

- List memory: 711,960 bytes
- Generator memory: 208 bytes

The generator uses significantly less memory because it does not store all results at once.

## 5. Performance Evaluation

The following timings were recorded during execution:

| Readings | Loop and Append | List Comprehension | Filter and Lambda |
|---:|---:|---:|---:|
| 10,000 | 0.000421 s | 0.000378 s | 0.000563 s |
| 100,000 | 0.004373 s | 0.003822 s | 0.005506 s |
| 1,000,000 | 0.043539 s | 0.038809 s | 0.054482 s |

All three methods produced identical results in every test.

List comprehension was the fastest method in these recorded tests.

## 6. Testing

The program includes the following test cases:

- All valid readings.
- All invalid readings.
- Empty input.
- Boundary values such as -50°C and 50°C.
- Alarm detection outside the safe temperature range.
- Performance comparison with different input sizes.

The performance tests confirmed that all three cleaning methods returned identical results.

## 7. Result
The sensor reading cleaning system was implemented successfully using list comprehension, dictionary comprehension, set comprehension, generators, enumerate, and filter functions. The performance tests demonstrated that list comprehension was the fastest among the three tested cleaning methods on this execution.
