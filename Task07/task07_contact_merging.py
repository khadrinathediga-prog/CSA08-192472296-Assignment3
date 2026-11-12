
import re
import time


# 1. Normalize phone numbers
def normalize_phone(phone):
    if not phone:
        return ""

    digits = re.sub(r"\D", "", str(phone))

    # Remove Indian country code
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    # Remove leading zero
    if len(digits) == 11 and digits.startswith("0"):
        digits = digits[1:]

    # Accept only 10-digit phone numbers
    if len(digits) != 10:
        return ""

    return digits


# 2. Normalize names
def normalize_name(name):
    if not name:
        return ""

    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9\s]", "", name)

    return " ".join(name.split())


# 3. Merge contacts using a dictionary
def merge_contacts(contacts):
    merged = {}

    for contact in contacts:
        name = contact.get("name", "") or ""
        phone = contact.get("phone", "") or ""
        email = contact.get("email", "") or ""

        normalized_phone = normalize_phone(phone)
        normalized_name = normalize_name(name)

        # Skip contacts without a valid phone number
        if not normalized_phone:
            continue

        # Create a new contact if phone number is not present
        if normalized_phone not in merged:
            merged[normalized_phone] = {
                "name": name.strip() if name.strip() else "Unknown",
                "normalized_name": normalized_name,
                "phone_numbers": set(),
                "emails": set()
            }

        entry = merged[normalized_phone]

        # Update name if the existing name is Unknown
        if name.strip() and entry["name"] == "Unknown":
            entry["name"] = name.strip()
            entry["normalized_name"] = normalized_name

        # Store original phone formats
        if phone.strip():
            entry["phone_numbers"].add(phone.strip())

        # Store unique email addresses
        if email.strip():
            entry["emails"].add(email.strip().lower())

    return merged


# 4. Display merged contacts
def display_contacts(merged):
    print("\nMERGED CONTACT LIST")
    print("=" * 60)

    for phone, details in sorted(merged.items()):
        print("\nName:", details["name"])
        print("Normalized Phone:", phone)
        print("All Phone Numbers:",
              sorted(details["phone_numbers"]))
        print("Email Addresses:",
              sorted(details["emails"]))


# 5. Small sample testing
def small_sample_testing():
    print("\nSMALL SAMPLE TESTING")

    contacts = [
        {
            "name": "Dr. Ravi",
            "phone": "+91 98400 12345",
            "email": "ravi@gmail.com"
        },
        {
            "name": "ravi kumar",
            "phone": "9840012345",
            "email": "RAVI@GMAIL.COM"
        },
        {
            "name": "Priya",
            "phone": "9876543210",
            "email": "priya@gmail.com"
        },
        {
            "name": "Ravi",
            "phone": "09840012345",
            "email": "ravi.work@gmail.com"
        },
        {
            "name": "Unknown",
            "phone": "",
            "email": "unknown@gmail.com"
        },
        {
            "name": "",
            "phone": "9123456789",
            "email": ""
        },
        {
            "name": "Ravi",
            "phone": "9876501234",
            "email": "another.ravi@gmail.com"
        }
    ]

    merged = merge_contacts(contacts)

    display_contacts(merged)

    print("\nTotal input contacts:", len(contacts))
    print("Total merged contacts:", len(merged))

    ravi = merged.get("9840012345", {})

    print(
        "Ravi duplicate formats merged:",
        len(ravi.get("phone_numbers", set())) == 3
    )

    print(
        "Contact without phone skipped:",
        len(merged) == 4
    )

    print(
        "Same name with different phone kept separate:",
        "9876501234" in merged
    )


# 6. Generate contacts for performance testing
def generate_contacts(number_of_contacts):
    contacts = []

    for i in range(number_of_contacts):
        phone = f"9{i % 1000000000:09d}"

        contacts.append({
            "name": f"Person {i}",
            "phone": phone,
            "email": f"person{i}@example.com"
        })

    return contacts


# 7. Pairwise comparison method
def pairwise_duplicate_check(contacts):
    groups = []

    for contact in contacts:
        phone = normalize_phone(contact.get("phone", ""))

        if not phone:
            continue

        email = (contact.get("email") or "").strip().lower()
        found = False

        for group in groups:
            if phone in group["phones"]:
                if email:
                    group["emails"].add(email)

                found = True
                break

        if not found:
            groups.append({
                "phones": {phone},
                "emails": {email} if email else set()
            })

    return groups


# 8. Performance comparison
def performance_comparison():
    print("\nPERFORMANCE COMPARISON")
    print("=" * 60)

    for size in [1000, 100000]:
        contacts = generate_contacts(size)

        # Dictionary method
        start = time.perf_counter()
        merged = merge_contacts(contacts)
        dictionary_time = time.perf_counter() - start

        print(f"\nNumber of contacts: {size}")
        print(f"Dictionary merging: {dictionary_time:.6f} seconds")
        print("Merged contacts:", len(merged))

        # Pairwise method is measured on the first 1000 contacts
        sample = contacts[:1000]

        start = time.perf_counter()
        pairwise_result = pairwise_duplicate_check(sample)
        pairwise_time = time.perf_counter() - start

        print(
            "Pairwise comparison (1000 contacts): "
            f"{pairwise_time:.6f} seconds"
        )

        print("Pairwise groups:", len(pairwise_result))


# 9. Edge case testing
def edge_case_testing():
    print("\nEDGE CASE TESTING")

    test_contacts = [
        {
            "name": "Ravi",
            "phone": "+91 98400 12345",
            "email": "ravi@gmail.com"
        },
        {
            "name": "RAVI",
            "phone": "9840012345",
            "email": "RAVI@GMAIL.COM"
        },
        {
            "name": "No Phone",
            "phone": "",
            "email": "nophone@gmail.com"
        },
        {
            "name": "",
            "phone": "9876543210",
            "email": ""
        }
    ]

    result = merge_contacts(test_contacts)

    print("Input contacts:", len(test_contacts))
    print("Merged contacts:", len(result))

    print(
        "Normalized Indian number:",
        normalize_phone("+91 98400 12345")
    )

    print(
        "Name normalization:",
        normalize_name(" Dr. RAVI Kumar ")
    )

    print(
        "Duplicate numbers merged:",
        len(result["9840012345"]["phone_numbers"]) == 2
    )


# 10. Main function
def main():
    print("CONTACT MERGING SYSTEM")
    print("=" * 60)

    small_sample_testing()
    edge_case_testing()
    performance_comparison()


if __name__ == "__main__":
    main()
