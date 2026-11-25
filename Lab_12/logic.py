def validate_records(records):
    """Проверяет список, при ошибке вызывает ValueError. Список не меняет."""
    if not isinstance(records, list):
        raise ValueError('Ожидался список записей')
    ids = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError('Запись должна быть словарём')
        record_id = record.get('id')
        if type(record_id) is not int or record_id <= 0:
            raise ValueError('Некорректный ID')
        if record_id in ids:
            raise ValueError('Повторяющийся ID')
        for key in ('title', 'category'):
            value = record.get(key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError('Некорректное поле ' + key)
        amount = record.get('amount')
        if type(amount) is not int or amount < 0:
            raise ValueError('Некорректное расстояние')
        if type(record.get('completed')) is not bool:
            raise ValueError('Некорректный статус')
        ids.add(record_id)


def add_record(records, title, category, amount):
    """Добавляет запись и возвращает её. При неверных данных список не меняет."""
    new_id = 1
    if records:
        ids = []
        for record in records:
            ids.append(record['id'])
        new_id = max(ids) + 1
    record = {'id': new_id, 'title': title.strip(), 'category': category.strip(),
              'amount': amount, 'completed': False}
    validate_records([record])
    records.append(record)
    return record


def find_records(records, query):
    """Возвращает совпадения, исходный список не меняет."""
    query = query.strip().lower()
    if not query:
        raise ValueError('Пустой запрос')
    found = []
    for record in records:
        if query in record['title'].lower():
            found.append(record)
    return found


def set_completed(records, record_id, completed):
    """Меняет статус найденной записи; возвращает True или False."""
    if type(completed) is not bool:
        raise ValueError('Неверный статус')
    for record in records:
        if record['id'] == record_id:
            record['completed'] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет найденную запись; возвращает True или False."""
    for record in records:
        if record['id'] == record_id:
            records.remove(record)
            return True
    return False


def statistics(records):
    """Возвращает словарь статистики, исходные записи не меняет."""
    completed = 0
    total_amount = 0
    categories = {}
    for record in records:
        if record['completed']:
            completed += 1
        amount = record['amount']
        total_amount += amount
        category = record['category'].strip()
        if category not in categories:
            categories[category] = 0
        categories[category] += amount
    return {'total': len(records), 'completed': completed,
            'not_completed': len(records) - completed,
            'amount': total_amount, 'categories': categories}
