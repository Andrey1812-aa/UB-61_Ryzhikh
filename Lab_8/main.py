from collections_lab import (word_counts, print_word_counts, common_topics,
                             all_topics, totals_by_category, titles_in_category)


def main():
    print('Задание 1. Подсчет слов')
    text = input('Введите текст: ')
    counts = word_counts(text)
    print('Частоты слов в алфавитном порядке:')
    print_word_counts(counts)

    print('\nЗадание 2. Учебные интересы')
    first = input('Темы первого студента через пробел: ').split()
    second = input('Темы второго студента через пробел: ').split()
    print(f'Общие темы: {common_topics(first, second)}')
    print(f'Все уникальные темы: {all_topics(first, second)}')

    print('\nЗадание 3. Словарь и кортеж')
    course = {'title': 'Python', 'hours': 4}
    course['hours'] = 6
    course['completed'] = False
    print(f'Запись: {course}')
    pair = (course['title'], course['hours'])
    title, hours = pair
    print(f'Название: {title}, часы: {hours}')

    print('\nИндивидуальный вариант №8. Туристические маршруты')
    routes = [
        {'title': 'Тропа к водопаду', 'category': 'пеший', 'amount': 8},
        {'title': 'Прогулка по лесу', 'category': 'пеший', 'amount': 5},
        {'title': 'Маршрут вдоль реки', 'category': 'велосипедный', 'amount': 16},
        {'title': 'Поездка к озеру', 'category': 'автомобильный', 'amount': 42},
        {'title': 'Путь к смотровой площадке', 'category': 'пеший', 'amount': 4},
        {'title': 'Круг по набережной', 'category': 'велосипедный', 'amount': 12},
    ]
    for route in routes:
        print(f"{route['title']} — {route['category']}, {route['amount']} км")

    totals = totals_by_category(routes)
    print('Общая протяженность по категориям:')
    for category in sorted(totals):
        print(f'{category}: {totals[category]} км')

    category = input('Введите категорию для поиска: ')
    print(f'Найденные маршруты: {titles_in_category(routes, category)}')


if __name__ == '__main__':
    main()
