text = input("Введите целые числа через пробел: ")
numbers = [int(number) for number in text.split()]
if not(numbers): print("Нет данных")
else:
    middle = sum(numbers) / len(numbers)
    print(f'Количество: {len(numbers)} | Сумма: {sum(numbers)}\nМинимум: {min(numbers)} | Максимум: {max(numbers)}\nСреднее: {middle:.2f}')
