
import random
import time
from collections import Counter


# Stop words
STOP_WORDS = {"the", "is", "a", "and", "to", "of", "in", "was", "for"}


# 1. Count word frequencies using get()
def frequencies(text):
    counts = {}

    for word in text.lower().split():
        word = word.strip(".,!?;:")
        if word and word not in STOP_WORDS:
            counts[word] = counts.get(word, 0) + 1

    return counts


# 2. Group complaints by district using setdefault()
def group_by_district(complaints):
    districts = {}

    for district, complaint in complaints:
        districts.setdefault(district, []).append(complaint)

    return districts


# 3. Find top k frequent words
def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]


# 4. Main program
def main():
    print("FARMER HELPLINE COMPLAINT ANALYSIS")
    print("-" * 45)

    text = """
    seeds price received seeds quality price received
    seeds fertilizer crop water
    """

    word_counts = frequencies(text)

    print("\nWORD FREQUENCIES")
    print(word_counts)

    print("\nTOP 3 WORDS")
    print(top(word_counts, 3))

    complaints = [
        ("Chennai", "Seed quality issue"),
        ("Madurai", "Fertilizer shortage"),
        ("Chennai", "Water supply problem"),
        ("Salem", "Crop price issue"),
        ("Madurai", "Seed availability"),
    ]

    print("\nCOMPLAINTS BY DISTRICT")
    grouped = group_by_district(complaints)

    for district, items in grouped.items():
        print(district, ":", items)

    # setdefault demonstration
    print("\nSTOP WORDS")
    print(STOP_WORDS)

    # Dictionary lookup
    print("\nDICTIONARY LOOKUP")
    print("Seeds count:", word_counts.get("seeds", 0))
    print("Missing word:", word_counts.get("unknown", 0))

    # Compare dictionary, list.count and Counter
    print("\nPERFORMANCE COMPARISON")

    for size in [1000, 10000, 100000]:
        words = [
            random.choice(["seeds", "price", "water", "crop", "fertilizer"])
            for _ in range(size)
        ]

        start = time.perf_counter()
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        dict_time = time.perf_counter() - start

        start = time.perf_counter()
        list_counts = {word: words.count(word) for word in set(words)}
        list_time = time.perf_counter() - start

        start = time.perf_counter()
        counter_counts = Counter(words)
        counter_time = time.perf_counter() - start

        print(f"\nComplaints: {size}")
        print(f"Dictionary: {dict_time:.6f} seconds")
        print(f"list.count(): {list_time:.6f} seconds")
        print(f"Counter: {counter_time:.6f} seconds")

        print("Results match:",
              counts == list_counts == counter_counts)

    # Edge case testing
    print("\nEDGE CASE TESTING")
    print("Empty text:", frequencies(""))
    print("Only stop words:", frequencies("the is a and"))

    # Dictionary views
    print("\nDICTIONARY VIEWS")
    print("Keys:", word_counts.keys())
    print("Values:", word_counts.values())
    print("Items:", word_counts.items())

    print("\nInsertion order is maintained in Python 3.7 and later.")


if __name__ == "__main__":
    main()
