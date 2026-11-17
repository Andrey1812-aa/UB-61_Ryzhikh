def word_counts(text):
    counts = {}
    words = text.lower().split()

    for part in words:
        word = part.strip(".,!?;:")
        if word != "":
            counts[word] = counts.get(word, 0) + 1

    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    first_set = set(first)
    second_set = set(second)
    common = first_set & second_set
    return sorted(common)


def all_topics(first, second):
    first_set = set(first)
    second_set = set(second)
    topics = first_set | second_set
    return sorted(topics)


def totals_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        amount = record["amount"]
        totals[category] = totals.get(category, 0) + amount

    return totals


def titles_in_category(records, category):
    titles = []

    for record in records:
        if record["category"] == category:
            titles.append(record["title"])

    return titles
