subject1_name = input("Введите название первого предмета: ")
subject1_count = int(input(f"Количество занятий в неделю по предмету '{subject1_name}': "))
subject1_duration = int(input(f"Продолжительность одного занятия (в минутах): "))
subject2_name = input("Введите название второго предмета: ")
subject2_count = int(input(f"Количество занятий в неделю по предмету '{subject2_name}': "))
subject2_duration = int(input(f"Продолжительность одного занятия (в минутах): "))
available_hours = float(input("Введите доступное время на неделю (в часах): "))
sub1_minutes = subject1_count * subject1_duration
sub2_minutes = subject2_count * subject2_duration
total_minutes = sub1_minutes + sub2_minutes
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4
print("\n           Расчёт учебной нагрузки           ")
print(f"Время на '{subject1_name}': {sub1_minutes} мин.")
print(f"Время на '{subject2_name}': {sub2_minutes} мин.")
print(f"Общая нагрузка за неделю: {total_minutes} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч.")
