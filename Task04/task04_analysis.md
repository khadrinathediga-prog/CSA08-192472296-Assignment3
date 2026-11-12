# Q4 – Sets: Elective Registration Clash Detection

## 1. Problem Analysis

The Elective Registration Clash Detection system identifies students registered for two electives.

Python sets are used to store registration numbers, remove duplicates and perform set operations to identify clashes and unique registrations.

## 2. Data Structures Used

### Sets
- Store unique elements.
- Automatically remove duplicate values.
- Support union, intersection, difference and symmetric difference.
- Provide average O(1) membership testing.

### Lists
- Store ordered collections of student registration numbers.
- Support iteration and display.

## 3. Set Operations

The program performs the following operations:

| Operation | Symbol | Purpose |
|---|---|---|
| Union | `A \| B` | Students in either elective |
| Intersection | `A & B` | Students in both electives |
| Difference | `A - B` | Students only in elective A |
| Symmetric difference | `A ^ B` | Students in exactly one elective |

## 4. Registration Clash Analysis

The program identifies three important groups.

### Students in both electives

```python
clashes = elective_a & elective_b
```

Expected result:

```text
['192311004', '192311009']
```

### Students in exactly one elective

```python
exactly_one = elective_a ^ elective_b
```

Expected result:

```text
['192311001', '192311002', '192311007', '192311010']
```

### Students in neither elective

```python
neither = all_students - (elective_a | elective_b)
```

Expected result:

```text
['192311003', '192311005', '192311006', '192311008']
```

The results are sorted before display for consistent reporting.

## 5. Venn Diagram Explanation

The two elective sets can be represented using a Venn diagram:

- Left circle: Students registered only for elective A.
- Right circle: Students registered only for elective B.
- Overlapping