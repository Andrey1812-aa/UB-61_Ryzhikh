from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


def check_error(path, text, message=''):
    path.write_text(text, encoding='utf-8')
    try:
        read_matrix(path)
    except ValueError as error:
        assert message in str(error)
    else:
        assert False, 'Ошибка не обнаружена'


with TemporaryDirectory() as directory:
    path = Path(directory) / 'matrix.txt'
    path.write_text('1 2\n7 -1\n', encoding='utf-8')
    assert read_matrix(path) == [[7, -1]]
    path.write_text('1 1\n0\n', encoding='utf-8')
    assert read_matrix(path) == [[0]]
    path.write_text('2 3\n1 -2 3\n4 0 -6\n', encoding='utf-8')
    matrix = read_matrix(path)
    assert row_sums(matrix) == [2, -2]
    assert column_sums(matrix) == [5, -2, -3]
    assert selected_sum(matrix) == 2
    assert selected_sum([[9]]) == 9
    assert selected_sum([]) == 0
    check_error(path, '')
    check_error(path, '0 3\n')
    check_error(path, '1 2\n1\n', 'Строка 2')
    check_error(path, '1 2\n1 x\n', 'Строка 2')
    check_error(path, '1 1\n1\n2\n')
    check_error(path, '1 1\n\n')
    check_error(path, 'x 2\n')
    check_error(path, '2 2\n1 2\n')
    path.unlink()
    try:
        read_matrix(path)
    except FileNotFoundError:
        pass
    else:
        assert False, 'Отсутствующий файл не обнаружен'
print('Все проверки пройдены')
