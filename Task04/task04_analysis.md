
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

| Operation | Symbol | Purpose |
|---|---|---|
| Union | `A | B` | Students in either elective |
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
- Overlapping region: Students registered for both electives.
- Outside both circles: Students registered for neither elective.

The intersection identifies registration clashes, while symmetric difference identifies students registered for exactly one elective.

## 6. Duplicate Removal

Sets automatically remove duplicate registration numbers.

Example:

```python
registrations = [101, 102, 101, 103, 102]
unique_registrations = set(registrations)

print(unique_registrations)
```

The resulting set contains only unique registration numbers.

## 7. Membership Performance Comparison

The program compares membership testing using a list and a set.

| Number of elements | List lookup (seconds) | Set lookup (seconds) |
|---:|---:|---:|
| 10,000 | 0.033552 | 0.000020 |
| 100,000 | 0.333387 | 0.000019 |
| 1,000,000 | 3.364527 | 0.000023 |

**Observation:** Set membership was significantly faster than list membership in the experiments.

## 8. Nested Loop vs Set Intersection

The program compares a nested-loop approach with set intersection.

| Input size | Nested loop (seconds) | Set intersection (seconds) |
|---:|---:|---:|
| 1,000 | 0.011797 | 0.000018 |
| 3,000 | 0.093531 | 0.000042 |
| 5,000 | 0.268403 | 0.000066 |

**Observation:** Set intersection was considerably faster than nested-loop comparison.

## 9. Time Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Set insertion | O(1) average |
| Set membership | O(1) average |
| Set removal | O(1) average |
| Union | O(n + m) |
| Intersection | O(min(n, m)) average |
| Difference | O(n) average |
| Symmetric difference | O(n + m) average |
| List membership | O(n) |

Here, n and m represent the sizes of the two sets.

A nested-loop comparison takes O(n × m) time, whereas set operations are generally much more efficient.

## 10. Edge Case Testing

The program tests:
- Empty sets.
- Sets containing duplicate values.
- Two sets with no common elements.
- Two identical sets.
- Membership of existing and non-existing elements.

These tests verify that set operations produce correct results for different inputs.

## 11. Alternative Approach

A list-based approach can also identify common students by checking each registration number against another list.

However, list membership requires O(n) time in the worst case.

Sets are more suitable for repeated membership testing because they provide average O(1) lookup time.

## 12. Conclusion

The experiment demonstrates how Python sets can efficiently identify elective registration clashes and unique student registrations.

Union, intersection, difference and symmetric difference simplify registration analysis.

The performance experiments show that set membership and intersection are considerably faster than list membership and nested-loop comparison.

Therefore, sets are the recommended data structure for detecting elective registration clashes.
