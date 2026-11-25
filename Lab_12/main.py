import json
from pathlib import Path
from logic import add_record, find_records, set_completed, delete_record, statistics
from storage import load_records, save_records


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print('Строка не должна быть пустой')


def read_number(prompt, minimum):
    while True:
        try:
            number = int(input(prompt))
            if number >= minimum:
                return number
            print('Число должно быть не меньше', minimum)
        except ValueError:
            print('Введите целое число')


def get_id(record):
    return record['id']


def show_records(records):
    if not records:
        print('Нет записей')
        return
    for record in sorted(records, key=get_id):
        status = 'пройден' if record['completed'] else 'не пройден'
        print(f"{record['id']}. {record['title']} | {record['category']} | {record['amount']} км | {status}")


def show_statistics(records):
    data = statistics(records)
    print('Всего маршрутов:', data['total'])
    print('Пройдено:', data['completed'])
    print('Не пройдено:', data['not_completed'])
    print('Общая длина:', data['amount'], 'км')
    for category in sorted(data['categories']):
        print(category + ':', data['categories'][category], 'км')


def save(path, records):
    try:
        save_records(path, records)
    except (OSError, ValueError) as error:
        print('Ошибка сохранения:', error)
        return False
    print('Данные сохранены')
    return True


def main():
    path = Path(__file__).resolve().parent / 'data.json'
    try:
        records = load_records(path)
    except FileNotFoundError:
        records = []
        print('Файла нет. Создан пустой список')
    except UnicodeError:
        print('Неверная кодировка')
        return
    except json.JSONDecodeError as error:
        print('Ошибка JSON:', error)
        return
    except (ValueError, OSError) as error:
        print('Ошибка загрузки:', error)
        return
    while True:
        print('\nПлан туристических маршрутов')
        print('1. Показать записи\n2. Добавить запись\n3. Найти записи')
        print('4. Изменить статус\n5. Удалить запись\n6. Показать статистику')
        print('7. Сохранить данные\n8. Выйти')
        command = input('Команда: ').strip()
        if command == '1':
            show_records(records)
        elif command == '2':
            title = read_text('Название: ')
            category = read_text('Категория: ')
            amount = read_number('Длина в км: ', 0)
            record = add_record(records, title, category, amount)
            print('Добавлен маршрут с ID', record['id'])
        elif command == '3':
            found = find_records(records, read_text('Поиск по названию: '))
            if found:
                show_records(found)
            else:
                print('Ничего не найдено')
        elif command == '4':
            record_id = read_number('ID: ', 1)
            if record_id not in [record['id'] for record in records]:
                print('ID не найден')
                continue
            while True:
                status = input('1 — пройден, 0 — не пройден: ').strip()
                if status in ('0', '1'):
                    break
                print('Введите 0 или 1')
            set_completed(records, record_id, status == '1')
            print('Статус изменён')
        elif command == '5':
            record_id = read_number('ID: ', 1)
            if record_id not in [record['id'] for record in records]:
                print('ID не найден')
            elif input('Удалить? (да/нет): ').strip().lower() == 'да':
                delete_record(records, record_id)
                print('Запись удалена')
            else:
                print('Удаление отменено')
        elif command == '6':
            show_statistics(records)
        elif command == '7':
            save(path, records)
        elif command == '8':
            while True:
                answer = input('Сохранить данные? (да/нет): ').strip().lower()
                if answer in ('да', 'нет'):
                    break
                print('Введите да или нет')
            if answer == 'нет':
                break
            if save(path, records):
                break
        else:
            print('Неизвестная команда')


if __name__ == '__main__':
    main()
