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
1. Frequency