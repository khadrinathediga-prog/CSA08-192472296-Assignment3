# Q1 – Daily Rainfall Records

## 1. Problem Analysis

A village rain-gauge station records daily rainfall measurements for 365 days.

The program uses a Python list to store readings and performs weekly rainfall calculations, moving averages, dry-day identification and performance comparisons.

## 2. Data Structure

A list is suitable because:
- It stores multiple daily readings in sequence.
- It supports indexing and slicing.
- It allows modification of rainfall values.
- It supports iteration and built-in functions.

## 3. Maximum and Minimum Rainfall

The program identifies the maximum and minimum daily rainfall values using Python's built-in `max()` and `min()` functions.

| Measurement | Rainfall | Day |
|---|---:|---:|
| Maximum rainfall | 100 mm | 282 |
| Minimum rainfall | 0 mm | 36 |

The `index()` method identifies the position of the first occurrence of each value. Adding 1 converts the zero-based index into a day number.

## 4. Pseudocode – 7-Day Moving Average

```text
START
Read rainfall list
IF number of readings is less than 7:
    RETURN empty list
Calculate sum of first 7 readings
Store sum / 7 as first average
FOR each remaining reading:
    Add new reading to running sum
    Subtract the reading leaving the window
    Calculate running sum / 7
    Store the average
RETURN averages
STOP
```

## 5. List Slicing Explanation

- `readings[7:14]` – Returns elements from index 7 to index 13.
- `readings[-7:]` – Returns the last seven readings.
- `readings[::7]` – Returns every seventh reading, starting from index 0.

## 6. List Operation Complexity

| Operation | Time Complexity |
|---|---|
| append() | O(1) amortized |
| insert() | O(n) |
| pop() at end | O(1) |
| pop() at beginning | O(n) |
| sort() | O(n log n) |

## 7. Moving Average Complexity

### Naive Method

Each window processes seven readings.

For n readings, the number of windows is n - 6.

Arithmetic additions: 6(n - 6).

Time complexity: O(7n), which is O(n) for a fixed window size of 7.

### Running-Sum Method

The first window requires 6 additions. Each subsequent window uses one addition and one subtraction.

Arithmetic additions: 6 + (n - 7).

Arithmetic subtractions: n - 7.

Time complexity: O(n).

The running-sum method avoids repeatedly summing all seven values.

## 8. Experimental Investigation

The program generated random rainfall readings and compared both methods.

| Readings | Naive Time (seconds) | Running-Sum Time (seconds) |
|---:|---:|---:|
| 365 | 0.000055 | 0.000028 |
| 36,500 | 0.005362 | 0.002757 |
| 365,000 | 0.048610 | 0.026357 |

**Observation:** The running-sum method was faster in all three experiments.

Timings may vary between executions and computers.

## 9. Edge Case Testing

| Test Case | Input | Expected Result | Observed Result |
|---|---|---|---|
| TC01 | Empty list | Empty result | Passed |
| TC02 | Five readings | Empty result | Passed |
| TC03 | 365 readings | 365-day analysis | Passed |
| TC04 | Zero rainfall | Identify dry days | Passed |

## 10. Weekly Rainfall Analysis

The program generates 365 daily readings and groups them into seven-day periods using list slicing.

It produces 53 weekly totals because 365 days contain 52 complete weeks and one remaining day.

- Wettest week: Week 50 – 590 mm.
- Driest week: Week 53 – 61 mm.

The final weekly total represents the remaining one-day period.

## 11. Late Reading Insertion

The `list.insert()` operation takes O(n) time in the worst case because existing elements may need to be shifted.

A list is still suitable for 365 daily readings. For frequent insertions, a different data structure such as a deque may be considered.

## 12. Alternative Concepts

### Using collections.deque

A deque with `maxlen=7` can maintain a seven-day window.

A running sum can be updated when a new reading arrives and an old reading leaves the window.

- Time complexity with repeated window sums: O(7n).
- Time complexity with running sum: O(n).
- Window storage: O(7), which is O(1) for a fixed window.

### Using a Dictionary

A dictionary can store rainfall readings using dates as keys.

Example:

```python
rainfall = {
    "2026-01-01": 25,
    "2026-01-02": 30
}
```

It allows readings to be accessed by date, but chronological ordering and missing dates must be handled carefully.

## 13. Conclusion

The list data structure is suitable for storing daily rainfall readings. Both moving-average methods produce the same results, but the running-sum method is faster in the experiments.

The program successfully identifies maximum and minimum rainfall, weekly totals, dry days and moving averages.

Therefore, the running-sum approach is recommended for efficient rainfall analysis.