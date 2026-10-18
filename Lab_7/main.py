from functions import average, normalize_text, sum_digits, select_numbers


def main():
    number = int(input("Введите целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    raw_numbers = input("Введите числа через пробел: ").split()
    numbers = []
    for part in raw_numbers:
        numbers.append(int(part))
    
    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg}")

    text = input("Введите текст: ")
    print(f"Нормализованный текст: {normalize_text(text)}")

    threshold = int(input("Введите порог: "))
    result = select_numbers(numbers, threshold)
    print(f"Подходящие числа: {result}")


if __name__ == "__main__":
    main()
