text = input("Введите числа через пробел: ")
numbers = [int(number) for number in text.split()]
if not numbers:
    print("Нет данных")
else:
    numbers_moduls=numbers.copy()
    for i in range(len(numbers_moduls)):
        numbers_moduls[i]=abs(numbers_moduls[i])
print(numbers, numbers_moduls)