def row_sums(matrix):
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


def column_sums(matrix):
    if len(matrix) == 0:
        return []
    sums = []
    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total += row[column]
        sums.append(total)
    return sums


def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        values = []
        for column in range(size):
            if row == column:
                values.append(0)
            elif row < column:
                values.append(1)
            else:
                values.append(2)
        matrix.append(values)
    return matrix


def transform(matrix):
    result = []
    for row in matrix:
        new_row = []
        for number in row:
            if number < 0:
                new_row.append(number - 2)
            else:
                new_row.append(number)
        result.append(new_row)
    return result
