last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст (в полных годах): "))
favorite_subject = input("Введите любимый предмет: ")
hours_per_week = float(input("Введите количество часов подготовки в неделю: "))
age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
hours_per_day = hours_per_week / 7
print("\n           КАРТОЧКА СТУДЕНТА            ")
print(f"Полное имя: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Текущий возраст: {age}")
print(f"Возраст через 4 года: {age_in_4_years}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Часов подготовки за 4 недели: {hours_in_4_weeks:.2f}")
print(f"Среднее время подготовки в день: {hours_per_day:.2f}")
