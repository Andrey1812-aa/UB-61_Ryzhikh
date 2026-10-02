first_str = "2"
second_str = "3"
print("Фрагмент А:")
print(f"  До преобразования: types ({type(first_str).__name__}, {type(second_str).__name__}), результат: {first_str + second_str}")
first_num = int(first_str)
second_num = int(second_str)
sum_result = first_num + second_num
print(f"  После преобразования: types ({type(first_num).__name__}, {type(second_num).__name__}), сумма: {sum_result}\n")
print("Объяснение: В исходном коде переменные содержали строки (str). "
      "Оператор '+' для строк выполняет объединение текста '2' и '3' -> '23'. "
      "После преобразования строк в целые числа (int) оператор '+' выполнил математическое сложение (2 + 3 = 5).\n")
raw_age = "17"  # Имитация ввода input("Возраст: ") 
print("Фрагмент Б:")
print(f"  Исходный тип ввода: {type(raw_age).__name__}")
int_age = int(raw_age)
age_next_year = int_age + 1
print(f"  После преобразования: type ({type(int_age).__name__}), возраст через год: {age_next_year}\n")
print("Объяснение: Функция input() всегда возвращает значение типа str. "
      "Попытка прибавить число 1 (int) к строке вызывает ошибку TypeError. "
      "Для выполнения арифметической операции необходимо применить функцию int() к полученной строке.\n")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Фрагмент В:")
print(f"  Среднее арифметическое чисел {first}, {second}, {third}: {average:.1f}")
print("Объяснение: Из-за приоритета арифметических операций деление выполняется "
      "раньше сложения, поэтому выражение 'first + second + third / 3' сначала разделило 10 на 3 (3.333...), "
      "а затем прибавило 4 и 7, получив 14.333... Чтобы сначала найти сумму трёх чисел, их нужно заключить в скобки.")

