def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError('Ожидался список задач')
    ids = set()
    for task in data:
        if not isinstance(task, dict):
            raise ValueError('Задача должна быть словарём')
        task_id = task.get('id')
        user_id = task.get('userId')
        title = task.get('title')
        completed = task.get('completed')
        if type(task_id) is not int or task_id <= 0:
            raise ValueError('Некорректный id')
        if task_id in ids:
            raise ValueError('Повторяющийся id')
        if type(user_id) is not int or user_id <= 0:
            raise ValueError('Некорректный userId')
        if not isinstance(title, str) or not title.strip():
            raise ValueError('Некорректное название')
        if type(completed) is not bool:
            raise ValueError('Некорректное поле completed')
        ids.add(task_id)


def completion_counts(todos):
    counts = {}
    for task in todos:
        user_id = task['userId']
        if user_id not in counts:
            counts[user_id] = 0
        if task['completed']:
            counts[user_id] += 1
    return counts


def top_users(counts):
    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    leaders = []
    for user_id in counts:
        if counts[user_id] == maximum:
            leaders.append(user_id)
    return sorted(leaders)


def leader_tasks(todos, leaders):
    result = []
    for task in todos:
        if task['completed'] and task['userId'] in leaders:
            result.append(task)
    return result


def select_tasks(todos, user_id, parameter=None):
    if not isinstance(parameter, str) or not parameter.strip():
        raise ValueError('Подстрока должна быть непустой')
    result = []
    for task in todos:
        if task['userId'] == user_id:
            if parameter.strip().lower() in task['title'].lower():
                result.append(task)
    return result
