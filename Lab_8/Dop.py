from collections_lab import totals_by_category


def sort_key(pair):
    category = pair[0]
    total = pair[1]
    return (-total, category)


def sorted_totals(records):
    totals = totals_by_category(records)
    pairs = list(totals.items())
    return sorted(pairs, key=sort_key)


records = [
    {"title": "A", "category": "пеший", "amount": 8},
    {"title": "B", "category": "водный", "amount": 10},
    {"title": "C", "category": "пеший", "amount": 2},
    {"title": "D", "category": "велосипедный", "amount": 15},
]

assert sorted_totals(records) == [
    ("велосипедный", 15),
    ("водный", 10),
    ("пеший", 10)
]
assert sorted_totals([]) == []

print("Дополнительные проверки пройдены!")
