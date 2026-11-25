import json
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records
from logic import add_record, set_completed

with TemporaryDirectory() as directory:
    path = Path(directory) / 'data.json'
    records = []
    save_records(path, records)
    assert load_records(path) == []
    add_record(records, 'Лесная тропа', 'Пешие', 4)
    set_completed(records, 1, True)
    save_records(path, records)
    assert load_records(path) == records
    path.write_text('{', encoding='utf-8')
    try:
        load_records(path)
    except json.JSONDecodeError:
        assert path.read_text(encoding='utf-8') == '{'
    else:
        assert False, 'Ошибка JSON не обнаружена'
    path.unlink()
    try:
        load_records(path)
    except FileNotFoundError:
        pass
    else:
        assert False, 'Отсутствующий файл не обнаружен'
print('Все проверки хранения пройдены')
