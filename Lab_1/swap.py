first_room = input("Введите номер первой аудитории: ")
second_room = input("Введите номер второй аудитории: ")
print(f"\nИсходные значения: first_room = {first_room}, second_room = {second_room}")
temp = first_room
first_room = second_room
second_room = temp
print(f"После обмена:    first_room = {first_room}, second_room = {second_room}")
