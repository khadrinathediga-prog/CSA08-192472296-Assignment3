
# Q3 – Dictionaries: Farmer Helpline Complaint Analysis

## 1. Problem Analysis

The Farmer Helpline Complaint Analysis system processes farmer complaints, counts frequently used words and groups complaints by district.

Python dictionaries are used to store word frequencies and district-wise complaint details.

## 2. Data Structures Used

### Dictionary
- Stores key-value pairs.
- Provides average O(1) lookup, insertion and update operations.
- Used for counting complaint words and grouping complaints.

### Set
- Stores unique elements.
- Used to maintain stop words.
- Average membership testing takes O(1) time.

### List
- Stores multiple complaints for each district.
- Allows complaints to be grouped and displayed.

## 3. Word Frequency Using get()

The `frequencies()` function uses the dictionary `get()` method to count words.

```python
counts[word] = counts.get(word, 0) + 1
```

If the word exists, its count is increased. Otherwise, it starts at 1.

The program converts text to lowercase and removes punctuation before counting.

## 4. Grouping Complaints Using setdefault()

The `group_by_district()` function groups complaints by district.

```python
districts.setdefault(district, []).append(complaint)
```

The `setdefault()` method creates a new list when a district is encountered for the first time.

## 5. Stop Words

Stop words are common words that are excluded from frequency analysis.

The program uses a set:

```python
STOP_WORDS = {"the", "is", "a", "and", "to", "of", "in", "was", "for"}
```

Set membership testing has average O(1) time complexity.

## 6. Top-K Word Frequency

The `top()` function sorts words by:
1. Frequency in descending order.
2. Word alphabetically when frequencies are equal.

It returns the most frequently occurring words.

## 7. Dictionary Lookup Performance

The program compares dictionary lookup with list-based counting and `collections.Counter`.

| Method | Description |
|---|---|
| Dictionary | Uses key-based word counting |
| List.count() | Counts occurrences by scanning a list |
| Counter | Uses Python's Counter class |

### Experimental Results

| Input Size | Dictionary (s) | List.count() (s) | Counter (s) |
|---:|---:|---:|---:|
| 1,000 | 0.000043 | 0.000045 | 0.000033 |
| 10,000 | 0.000446 | 0.000420 | 0.000319 |
| 100,000 | 0.004690 | 0.004210 | 0.003014 |

**Observation:** Counter was the fastest in these experiments. Actual timings may vary depending on the system and input.

## 8. Time Complexity Analysis

| Operation | Average/Worst-case complexity |
|---|---|
| Dictionary lookup | O(1) average, O(n) worst case |
| Dictionary insertion | O(1) average, O(n) worst case |
| Dictionary update | O(1) average, O(n) worst case |
| List.count() | O(n) |
| Set membership | O(1) average |
| Sorting dictionary items | O(n log n) |

Word-frequency counting using a dictionary takes approximately O(n) average time for n words, assuming average constant-time dictionary operations.

Sorting the word frequencies for Top-K selection takes O(u log u), where u is the number of unique words.

## 9. Edge Case Testing

The program checks:
- Empty complaint input.
- Stop-word filtering.
- Repeated words.
- Case-insensitive word counting.
- Punctuation removal.
- Dictionary view operations.

These tests help verify correct word counting and grouping behaviour.

## 10. Dictionary Views

Dictionary methods such as `keys()`, `values()` and `items()` provide dynamic views.

- `keys()` returns dictionary keys.
- `values()` returns dictionary values.
- `items()` returns key-value pairs.

Dictionary views reflect changes made to the dictionary.

## 11. Alternative Approach

A `collections.Counter` object can be used for word-frequency analysis.

Example:

```python
from collections import Counter

words = ["farmer", "water", "farmer", "crop"]
counts = Counter(words)

print(counts)
```

Counter provides a convenient way to count repeated elements.

## 12. Conclusion

The experiment demonstrates how dictionaries efficiently store word frequencies and district-wise complaint information.

The `get()` method simplifies frequency counting, while `setdefault()` simplifies grouping.

The performance experiment compares dictionary counting, list counting and Counter. Counter performed fastest in the recorded tests.

Therefore, dictionaries and Counter are useful data structures for analysing farmer complaints.
