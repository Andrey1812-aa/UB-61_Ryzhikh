text = input("Введите текст: ")
cnt_of_dous_puntos = text.count(":")
result = text.replace(":", "-")
print(f'Количество замен: {cnt_of_dous_puntos}\nНовая строка: {result}')