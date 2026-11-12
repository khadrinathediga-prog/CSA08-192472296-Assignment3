# Q7 – Contact Merging Using Dictionaries and Sets

**Student Name:** Khadrinath Gowd  
**Register Number:** 192472296  
**Course:** B.Tech CSE – AI  
**Subject:** CSA08 – Python Programming

## Stage 1: Problem Understanding

### Problem Statement
Two mobile phones and one SIM card may contain overlapping contact information. The objective is to combine duplicate contacts into a single contact while preserving unique phone numbers and email addresses.

### Input
- Contact name
- Phone number
- Email address

### Output
- A merged contact list
- Unique phone numbers and email addresses
- Performance comparison between dictionary-based and pairwise approaches

### Identity Rules
1. Phone numbers are used as the primary identity.
2. Different formats of the same Indian phone number are treated as duplicates.
3. Contacts with the same name but different phone numbers remain separate.
4. Contacts without a valid phone number are skipped.

## Stage 2: Algorithm Design

### Data Structures Used

**Dictionary:**
- Stores contacts using normalized phone numbers as keys.
- Provides efficient average-case lookup.

**Sets:**
- Store unique original phone-number formats.
- Store unique email addresses.
- Automatically prevent duplicate values.

### Normalization

**Phone normalization:**
- Remove spaces and special characters.
- Remove the Indian country code `91` when present.
- Remove a leading zero when present.
- Accept valid 10-digit numbers.

**Name normalization:**
- Convert names to lowercase.
- Remove punctuation.
- Remove extra spaces.

### Pseudocode

```text
START

Create an empty dictionary

FOR each contact:
    Read name, phone and email
    Normalize phone number

    IF phone number is invalid:
        Skip contact

    IF normalized phone is not in dictionary:
        Create a new contact entry

    Add original phone number to phone set
    Add email to email set

RETURN merged dictionary

STOP
```

## Stage 3: Implementation and Testing

The program was implemented using Python functions, dictionaries, sets and regular expressions.

### Sample Testing Results

| Test case | Result |
|---|---|
| Total input contacts | 7 |
| Total merged contacts | 4 |
| Duplicate phone formats merged | True |
| Contact without phone skipped | True |
| Same name with different phone kept separate | True |

### Edge Case Testing

| Test | Result |
|---|---|
| Input contacts | 4 |
| Merged contacts | 2 |
| Indian number normalization | 9840012345 |
| Name normalization | dr ravi kumar |
| Duplicate numbers merged | True |

### Performance Testing

The dictionary method was tested using 1,000 and 100,000 generated contacts.

| Number of contacts | Dictionary merging time |
|---:|---:|
| 1,000 | 0.001425 seconds |
| 100,000 | 0.188308 seconds |

### Pairwise Comparison

The pairwise method was tested using 1,000 contacts.

| Test | Time |
|---|---:|
| Pairwise comparison – first run | 0.011657 seconds |
| Pairwise comparison – second run | 0.012274 seconds |

**Note:** Pairwise comparison was measured on 1,000 contacts only. It was not run on all 100,000 contacts because its quadratic time complexity makes that test expensive.

## Stage 4: Analysis and Discussion

### Why is a dictionary better than all-pairs comparison?

The dictionary stores each contact using its normalized phone number as a key. It can find an existing contact in average O(1) lookup time.

The pairwise method checks existing groups one by one. In the worst case, it requires O(n²) comparisons.

Therefore, dictionary-based merging is more efficient for large contact collections.

### Time and Space Complexity

| Operation | Time complexity |
|---|---|
| Phone normalization | O(L), where L is phone-string length |
| Dictionary insertion and lookup | Average O(1) per contact |
| Merging n contacts | Average O(n), assuming bounded input lengths |
| Pairwise comparison | O(n²) worst case |
| Dictionary storage | O(n) |

The dictionary approach requires O(n) additional space to store merged contacts and their unique values.

### Limitation

The system uses phone numbers as the primary identity. If the same person uses completely different phone numbers, the system may treat them as separate contacts. Contacts without valid phone numbers are skipped.

The normalization rules are designed for Indian 10-digit mobile numbers and may need modification for international contacts.

## Conclusion

The contact merging system successfully combines duplicate contacts using dictionaries and sets. Testing confirmed that different formats of the same phone number are merged, missing phone numbers are skipped, and contacts with the same name but different phone numbers remain separate.

The performance results demonstrate that dictionary-based merging is more suitable for large contact collections than pairwise comparison.