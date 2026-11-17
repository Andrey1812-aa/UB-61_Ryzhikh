def factorial_recursive(number):
    if number == 0:
        return 1
    return number * factorial_recursive(number - 1)


def factorial_iterative(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


for number in range(21):
    assert factorial_recursive(number) == factorial_iterative(number)

assert factorial_recursive(0) == 1
assert factorial_recursive(5) == 120
print('Дополнительные проверки пройдены!')
