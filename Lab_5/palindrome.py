text = input("Введите текст: ")
if (not text) or not(text.replace(' ','')):
    print("Нет текста")
else:
    if "".join(text.lower().split()) == ("".join(text.lower().split()))[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")