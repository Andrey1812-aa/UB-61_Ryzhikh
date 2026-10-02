rejected_count = 0

while True:
    num = int(input("Введите положительное целое число: "))
    if num > 0:
        square = num ** 2
        print(f"Квадрат: {square}")
        print(f"Отклонено попыток: {rejected_count}")
        break
    else:
        rejected_count += 1
