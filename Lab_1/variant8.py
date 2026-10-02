order_name = "Фотопечать"
customer_name = input("Введите имя заказчика: ")

item1_name = "Малые фотографии"
item1_count = int(input(f"Количество ({item1_name}): "))
item1_price = float(input(f"Цена за единицу ({item1_name}), руб.: "))

item2_name = "Большие фотографии"
item2_count = int(input(f"Количество ({item2_name}): "))
item2_price = float(input(f"Цена за единицу ({item2_name}), руб.: "))

delivery_cost = float(input("Стоимость доставки, руб.: "))
discount_percent = float(input("Введите скидку на товары (в %, от 0 до 100): "))
amount_paid = float(input("Внесённая сумма, руб.: "))

item1_total = item1_count * item1_price
item2_total = item2_count * item2_price
goods_total = item1_total + item2_total
discount_amount = goods_total * (discount_percent / 100)
discounted_goods_total = goods_total - discount_amount
total_cost = discounted_goods_total + delivery_cost
total_quantity = item1_count + item2_count
change = amount_paid - total_cost

print("\n")
print(f"Заказ: {order_name} | Заказчик: {customer_name}")
print(f"{item1_name} | {item1_count} шт. | {item1_price:.2f} руб. | {item1_total:.2f} руб.")
print(f"{item2_name} | {item2_count} шт. | {item2_price:.2f} руб. | {item2_total:.2f} руб.")
print(f"Общее количество товаров: {total_quantity} шт.")
print(f"Стоимость товаров (без скидки): {goods_total:.2f} руб.")
print(f"Скидка ({discount_percent:.1f}%): -{discount_amount:.2f} руб.")
print(f"Стоимость товаров (со скидкой): {discounted_goods_total:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"ИТОГО К ОПЛАТЕ: {total_cost:.2f} руб.")
print(f"Внесено: {amount_paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
