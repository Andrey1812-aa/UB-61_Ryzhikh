text = input("Целые числа через пробел: ")

numbers = []
for part in text.split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if 10 <= number <= 20:
        selected.append(number)

count = len(selected)
total = sum(selected)
sorted_selected = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Сортированная копия: {sorted_selected}")
