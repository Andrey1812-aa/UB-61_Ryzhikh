import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import validate_todos, completion_counts, top_users, leader_tasks, select_tasks


def check_error(data):
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, 'Ошибка не обнаружена'


folder = Path(__file__).resolve().parent
with open(folder / 'todos.json', encoding='utf-8') as file:
    todos = json.load(file)
validate_todos(todos)
counts = completion_counts(todos)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]
assert [t['id'] for t in leader_tasks(todos, top_users(counts))] == [1, 3, 4, 5]
assert completion_counts([]) == {}
assert top_users({}) == []
assert top_users({5: 0, 10: 0}) == []
assert leader_tasks([todos[1]], []) == []
assert completion_counts([todos[1]]) == {5: 0}
assert top_users({5: 2, 10: 1}) == [5]
assert top_users({10: 2, 5: 2}) == [5, 10]
selected = select_tasks(todos, 5, 'и')
assert [t['id'] for t in selected] == [2, 5]
assert select_tasks(todos, 5, 'И') == selected
assert select_tasks(todos, 100, 'и') == []
assert select_tasks(todos, 5, 'xyz') == []
check_error({})
check_error([todos[0], todos[0]])
for key, value in [('id', True), ('completed', 'false')]:
    task = todos[0].copy()
    task[key] = value
    check_error([task])
task = todos[0].copy()
del task['userId']
check_error([task])
with TemporaryDirectory() as directory:
    path = Path(directory) / 'selected.json'
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(selected, file, ensure_ascii=False)
    with open(path, encoding='utf-8') as file:
        assert json.load(file) == selected
print('Все проверки пройдены')
