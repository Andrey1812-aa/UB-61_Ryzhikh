text = input("Введите текст: ")
if (not text) or not(text.replace(' ','')):
    print("Нет текста")
else:
    text = "".join(text.lower().split())
    for i in range(len(text)-1):
        if not(text[i] == text[len(text)-1-i]):
            print("Не палиндром")
    else:
        print("Палиндром")
