from logic import validate_records, add_record, find_records, set_completed, delete_record, statistics


def check_error(records):
    try:
        validate_records(records)
    except ValueError:
        pass
    else:
        assert False, 'Ошибка не обнаружена'


records = []
validate_records(records)
assert statistics(records) == {'total': 0, 'completed': 0, 'not_completed': 0, 'amount': 0, 'categories': {}}
first = add_record(records, ' Лес ', ' Пешие ', 4)
second = add_record(records, 'Лес', 'Велосипедные', 2)
assert first['title'] == 'Лес' and first['category'] == 'Пешие'
assert first['id'] == 1 and second['id'] == 2
assert find_records(records, 'ЛЕС') == records
assert find_records(records, 'река') == []
assert set_completed(records, 2, True)
assert not set_completed(records, 99, True)
assert not delete_record(records, 99)
assert statistics(records) == {'total': 2, 'completed': 1, 'not_completed': 1, 'amount': 6,
                               'categories': {'Пешие': 4, 'Велосипедные': 2}}
check_error({})
check_error([first, first])
for key, value in [('id', True), ('amount', True), ('amount', -1), ('completed', 1), ('title', ' '), ('category', None)]:
    wrong = first.copy()
    wrong[key] = value
    check_error([wrong])
assert delete_record(records, 1)
assert records[0]['id'] == 2
assert add_record(records, 'Река', 'Пешие', 0)['id'] == 3
print('Все проверки логики пройдены')
