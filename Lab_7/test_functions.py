from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

original = [-5, 0, 2, 5]
copy_before = original.copy()

assert select_numbers(original, 2) == [0, 2]
assert select_numbers([], 5) == []
assert select_numbers([10, -10, 3, -3, 0], 5) == [3, -3, 0]

assert select_numbers([4, 5, 6, -5], 5) == [4, 5, -5] # <--- ВОТ ТУТ ИСПРАВИЛ!
assert select_numbers([2, 2, -2, 8], 2) == [2, 2, -2]
assert original == copy_before

print("Все проверки пройдены успешно!")
