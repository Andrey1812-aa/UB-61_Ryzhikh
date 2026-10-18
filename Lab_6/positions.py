numbers = [int(number) for number in input("Введите числа через пробел: ").split()]
if not(numbers):
    print("Нет данных")
else:
    indexes = []
    maximum = max(numbers)
    for i, number in enumerate(numbers, 0):
        if number == maximum:
            indexes.append(i)
    print(indexes)