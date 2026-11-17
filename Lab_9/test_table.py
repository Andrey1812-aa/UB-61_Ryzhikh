from table import row_sums, column_sums, diagonal_pattern, transform

matrix = [[1, 2, 3], [4, 5, 6]]
copy_before = []
for row in matrix:
    copy_before.append(row.copy())
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]
assert matrix == copy_before

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

original = [[-2, 0, 3], [4, -5, 6]]
original_copy = []
for row in original:
    original_copy.append(row.copy())
result = transform(original)
assert result == [[-4, 0, 3], [4, -7, 6]]
assert original == original_copy
result[0][0] = 100
assert original == original_copy

assert transform([[0]]) == [[0]]
assert transform([[-1]]) == [[-3]]
assert transform([[5, -3, 0], [-7, 2, -1]]) == [[5, -5, 0], [-9, 2, -3]]
assert transform([[1], [-1], [0]]) == [[1], [-3], [0]]

print('Все проверки пройдены успешно!')
