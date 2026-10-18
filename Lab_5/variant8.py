text = input("Введите текст: ")

words = text.split()
found = 0

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if cleaned.count("а") == 1:
        print(cleaned)
        found = found + 1

if found == 0:
    print("Нет совпадений")

print(f"Количество: {found}")
