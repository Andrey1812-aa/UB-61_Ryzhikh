from pathlib import Path
from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


def read_positive_integer():
    while True:
        try:
            number = int(input('Введите положительное целое число: '))
        except ValueError:
            print('Не целое число')
            continue
        if number <= 0:
            print('Должно быть больше нуля')
        else:
            return number


def main():
    size = read_positive_integer()
    print('Введено:', size)
    folder = Path(__file__).resolve().parent
    try:
        matrix = read_matrix(folder / 'matrix.txt')
        rows = ' '.join(str(x) for x in row_sums(matrix))
        columns = ' '.join(str(x) for x in column_sums(matrix))
        report = f'Суммы строк: {rows}\nСуммы столбцов: {columns}\nРезультат варианта: {selected_sum(matrix)}\n'
        with open(folder / 'report.txt', 'w', encoding='utf-8') as file:
            file.write(report)
        print(report, end='')
    except FileNotFoundError:
        print('Файл не найден')
    except UnicodeError:
        print('Неверная кодировка файла')
    except ValueError as error:
        print('Ошибка формата:', error)
    except OSError as error:
        print('Ошибка доступа:', error)


if __name__ == '__main__':
    main()
