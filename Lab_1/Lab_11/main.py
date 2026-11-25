import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users, leader_tasks, select_tasks


def read_user_id():
    while True:
        try:
            user_id = int(input('Введите ID пользователя: '))
            if user_id > 0:
                return user_id
            print('ID должен быть больше нуля')
        except ValueError:
            print('Введите целое число')


def read_parameter():
    while True:
        parameter = input('Введите подстроку: ').strip()
        if parameter:
            return parameter
        print('Подстрока не должна быть пустой')


def main():
    folder = Path(__file__).resolve().parent
    try:
        with open(folder / 'todos.json', 'r', encoding='utf-8') as file:
            todos = json.load(file)
        validate_todos(todos)
        counts = completion_counts(todos)
        leaders = top_users(counts)
        result = leader_tasks(todos, leaders)
        selected = select_tasks(todos, read_user_id(), read_parameter())
        with open(folder / 'leaders.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, ensure_ascii=False, indent=2)
        with open(folder / 'selected.json', 'w', encoding='utf-8') as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)
        print('Количество выполненных задач:', counts)
        print('Лидеры:', leaders)
        print('Найденные задачи:', selected)
    except FileNotFoundError:
        print('Файл не найден')
    except UnicodeError:
        print('Неверная кодировка')
    except json.JSONDecodeError as error:
        print('Ошибка JSON:', error)
    except ValueError as error:
        print('Ошибка структуры:', error)
    except OSError as error:
        print('Ошибка доступа:', error)


if __name__ == '__main__':
    main()
