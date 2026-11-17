from collections_lab import (word_counts, common_topics, all_topics,
                             totals_by_category, titles_in_category)

assert word_counts('Python, python! SQL') == {'python': 2, 'sql': 1}
assert word_counts('!!!') == {}
assert word_counts('') == {}
assert word_counts('  Кот; КОТ: собака.  ') == {'кот': 2, 'собака': 1}

first = ['python', 'sql', 'python']
second = ['sql', 'git']
assert common_topics(first, second) == ['sql']
assert all_topics(first, second) == ['git', 'python', 'sql']
assert common_topics([], second) == []
assert all_topics([], second) == ['git', 'sql']
assert common_topics([], []) == []
assert all_topics([], []) == []

records = [
    {'title': 'A', 'category': 'основное', 'amount': 4},
    {'title': 'B', 'category': 'дополнительное', 'amount': 2},
    {'title': 'C', 'category': 'основное', 'amount': 3},
]
copy_before = []
for record in records:
    copy_before.append(record.copy())
assert totals_by_category(records) == {'основное': 7, 'дополнительное': 2}
assert titles_in_category(records, 'основное') == ['A', 'C']
assert titles_in_category(records, 'нет') == []
assert totals_by_category([]) == {}
assert titles_in_category([], 'основное') == []
assert records == copy_before

routes = [
    {'title': 'Тропа к водопаду', 'category': 'пеший', 'amount': 8},
    {'title': 'Прогулка по лесу', 'category': 'пеший', 'amount': 5},
    {'title': 'Маршрут вдоль реки', 'category': 'велосипедный', 'amount': 16},
    {'title': 'Поездка к озеру', 'category': 'автомобильный', 'amount': 42},
    {'title': 'Путь к смотровой площадке', 'category': 'пеший', 'amount': 4},
    {'title': 'Круг по набережной', 'category': 'велосипедный', 'amount': 12},
]
copy_routes = []
for route in routes:
    copy_routes.append(route.copy())
assert totals_by_category(routes) == {
    'пеший': 17, 'велосипедный': 28, 'автомобильный': 42
}
assert titles_in_category(routes, 'пеший') == [
    'Тропа к водопаду', 'Прогулка по лесу', 'Путь к смотровой площадке'
]
assert titles_in_category(routes, 'автомобильный') == ['Поездка к озеру']
assert titles_in_category(routes, 'водный') == []
assert routes == copy_routes

print('Все проверки пройдены успешно!')
