import math

total = int(input("Введите общее количество заданий: "))
capacity = int(input("Введите количество заданий в комплекте: "))
full_units = total // capacity
remainder = total % capacity
total_units = (total + capacity - 1) // capacity if total > 0 else 0
print(f"Полных {full_units} , остаток {remainder} , всего {total_units}")
