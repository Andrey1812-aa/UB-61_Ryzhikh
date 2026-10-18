from shlex import split

text = input("Введите текст: ")
normaliz = text.strip()
while '  ' in normaliz:
    normaliz = normaliz.replace('  ', ' ')
print(f"Старая длина строки: {len(text)} | Новая: {len(normaliz)}")
print(f"Нормализованный текст: {normaliz} | Количество слов: {len(normaliz.split())}")
