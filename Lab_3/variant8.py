percent = int(input("Введите процент заполнения группы (0-100): "))

if percent < 0 or percent > 100:
    print("Ошибка диапазона")
elif 0 <= percent <= 39:
    print("Есть места")
elif 40 <= percent <= 79:
    print("Группа набирается")
else:  
    print("Почти заполнена")
