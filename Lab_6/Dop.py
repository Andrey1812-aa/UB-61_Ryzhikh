numbers = [int(number) for number in input("Введите числа через пробел: ").split()]
unique_numbs=[]
result = numbers.copy()
for i in range(len(numbers)):
    if numbers[i] in unique_numbs:
        result[i] = '*'
    else:
        unique_numbs.append(numbers[i])
print([result[i] for i in range(len(result)) if result[i] != '*'])