n = int(input("Введите количество чисел n (>= 0): "))

count = 0
total_sum = 0

for i in range(1, n + 1):
    num = int(input(f"Введите число {i}: "))
    if abs(num) > 5:
        count += 1
        total_sum += num

print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
