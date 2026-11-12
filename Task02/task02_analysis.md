# Q2 – Tuples, Mutability and Copying

## 1. Problem Analysis

The City Bus-Stop Map demonstrates Python tuples, dictionaries, mutability, aliasing and copying.

Tuples are used to represent fixed bus-stop information. Dictionaries store bus-stop details using tuple keys.

## 2. Data Structures Used

### Tuples
- Tuples store fixed collections of values.
- They are immutable.
- They can be used as dictionary keys when their elements are hashable.

### Dictionaries
- Dictionaries store key-value pairs.
- Tuple keys allow locations to be represented using coordinates or zones.
- Average lookup time complexity is O(1).

### Lists
- Lists store mutable collections.
- Nested lists are used to represent a 2D grid.

## 3. Tuple Dictionary Keys

The program uses tuple keys such as:

```python
("North", "Zone A")
```

A tuple can be used as a dictionary key because it is immutable and hashable when all its elements are hashable.

A list cannot be used as a dictionary key because lists are mutable and unhashable. Using a list as a key produces a TypeError.

## 4. List Comprehension for Grid Creation

The correct method to create an independent 3 × 3 grid is:

```python
grid = [[0 for _ in range(3)] for _ in range(3)]
```

Each row is created independently.

The incorrect method is:

```python
grid = [[0] * 3] * 3
```

This creates three references to the same inner list. Changing one row affects all rows.

### Memory Diagram

Incorrect grid:

```text
grid
 |
 +----> Row 1 ----+
 |                |
 +----> Row 2 ----+----> [0, 0, 0]
 |                |
 +----> Row 3 ----+
```

Correct grid:

```text
grid
 |
 +----> Row 1 ----> [0, 0, 0]
 |
 +----> Row 2 ----> [0, 0, 0]
 |
 +----> Row 3 ----> [0, 0, 0]
```

## 5. Aliasing and Copying

### Aliasing

Aliasing occurs when two variables refer to the same object.

```python
alias = original
```

Changes made through either variable affect the same object.

### Shallow Copy

A shallow copy creates a new outer object but shares nested objects.

Methods used:
- copy.copy()
- List slicing [:]

### Deep Copy

A deep copy creates a separate copy of the object and its nested objects.

Method used:

```python
copy.deepcopy(original)
```

Changes to the original nested lists do not affect the deep copy.

## 6. Tuple Unpacking

Tuple unpacking assigns tuple elements to individual variables.

Example:

```python
stop = ("Central Station", "Zone A", 12)
name, zone, bus_number = stop
```

The three values are assigned to their corresponding variables.

## 7. Identity Testing

The program uses the `is` operator and `id()` function.

- `is` checks whether two variables refer to the same object.
- `id()` returns the identity of an object.

The experiment demonstrates that an alias refers to the original object, while a slicing copy creates a different outer object.

## 8. Memory Comparison

The program measures container memory using `sys.getsizeof()` for one million elements.

| Data Structure | Measured Memory |
|---|---:|
| List | 8,000,056 bytes |
| Tuple | 8,000,040 bytes |

These measurements represent container size and exclude the complete memory occupied by referenced integer objects.

## 9. Creation and Indexing Time

The program compares list and tuple creation and indexing using `time.perf_counter()`.

| Operation | List Time (seconds) | Tuple Time (seconds) |
|---|---:|---:|
| Creation | 0.004804 | 0.005137 |
| Indexing | 0.001599 | 0.001562 |

Observation: The measured times are very close. Tuple creation was slightly slower in this experiment, while tuple indexing was slightly faster.

Timings may vary between executions and computers.

## 10. Mutable Objects Inside Tuples

A tuple cannot be modified by replacing its elements. However, if a tuple contains a mutable object such as a list, the contents of that list can be modified.

The program demonstrates this by adding a new bus stop to a list stored inside a tuple.

## 11. Alternative Data Structure – Sparse Dictionary

A sparse dictionary stores only the positions that contain actual data.

Example:

```python
sparse_grid = {
    (0, 0): "Central",
    (1, 2): "Market",
    (2, 1): "College"
}
```

This approach avoids storing empty grid positions.

Average dictionary lookup complexity is O(1).

## 12. Conclusion

The experiment demonstrates the use of tuples as immutable data structures and dictionary keys.

It also explains aliasing, shallow copying, deep copying and the difference between shared and independent nested lists.

The results show why independent list rows should be created using list comprehension and why deep copying is useful when nested objects must be copied independently.