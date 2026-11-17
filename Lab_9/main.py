from table import row_sums, column_sums, diagonal_pattern, transform


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    rows = int(input('Введите количество строк: '))
    while rows <= 0:
        rows = int(input('Количество строк должно быть положительным. Повторите: '))

    columns = int(input('Введите количество столбцов: '))
    while columns <= 0:
        columns = int(input('Количество столбцов должно быть положительным. Повторите: '))

    matrix = []
    for number in range(rows):
        parts = input(f"Введите строку {number + 1}: ").split()

        while len(parts) != columns:
            print(f"Количество чисел в строке должно быть равно {columns}.")
            parts = input("Повторите ввод строки: ").split()

        values = []
        for part in parts:
            values.append(int(part))

        matrix.append(values)

    print('Исходная таблица:')
    print_matrix(matrix)
    print(f'Суммы строк: {row_sums(matrix)}')
    print(f'Суммы столбцов: {column_sums(matrix)}')

    size = int(input('Введите размер квадратной таблицы: '))
    while size < 1:
        size = int(input('Размер должен быть положительным. Повторите: '))
    print('Диагональный узор:')
    print_matrix(diagonal_pattern(size))

    print('Индивидуальный вариант №8 (отрицательные числа уменьшить на 2):')
    result = transform(matrix)
    print('Новая таблица:')
    print_matrix(result)
    print('Исходная таблица после преобразования:')
    print_matrix(matrix)


if __name__ == '__main__':
    main()
