def read_matrix(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if not lines:
        raise ValueError('Файл пуст')
    parts = lines[0].split()
    if len(parts) != 2:
        raise ValueError('Строка 1: нужно два целых числа')
    try:
        rows, columns = int(parts[0]), int(parts[1])
    except ValueError:
        raise ValueError('Строка 1: размеры должны быть целыми')
    if rows <= 0 or columns <= 0:
        raise ValueError('Строка 1: размеры должны быть положительными')
    if len(lines) != rows + 1:
        raise ValueError('Неверное количество строк матрицы')
    matrix = []
    for i in range(1, rows + 1):
        parts = lines[i].split()
        if len(parts) != columns:
            raise ValueError(f'Строка {i + 1}: неверное количество чисел')
        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(f'Строка {i + 1}: ожидалось целое число')
        matrix.append(row)
    return matrix


def selected_sum(matrix):
    if not matrix:
        return 0
    return sum(matrix[0])
