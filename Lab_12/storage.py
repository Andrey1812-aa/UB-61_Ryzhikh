import json
from logic import validate_records


def load_records(path):
    """Читает и проверяет JSON. Ошибки передаёт вызывающей программе."""
    with open(path, 'r', encoding='utf-8') as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    """Проверяет и сохраняет список. Ошибки не скрывает."""
    validate_records(records)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
