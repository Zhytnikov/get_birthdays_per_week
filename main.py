from datetime import date, timedelta

def get_birthdays_per_week(users):
    # Якщо список користувачів пустий, повертаємо пустий словник
    if not users:
        return {}

    # Отримуємо поточну дату
    current_date = date.today()

    # Список днів тижня 
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # Ініціалізуємо словник для зберігання імен користувачів за днями тижня
    birthdays_per_week = {day: [] for day in weekdays.values()}

    # Перебираємо кожного користувача
    for user in users:
        name = user['name']
        birthday = user['birthday']

        # Знаходимо наступну дату народження в поточному році
        next_birthday = birthday.replace(year=current_date.year)

        # Якщо день народження вже минув, використовуємо наступний рік
        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)

        # Визначаємо, чи дата народження потрапляє в наступний тиждень
        if current_date <= next_birthday <= current_date + timedelta(days=7):
            # Визначаємо день тижня для наступного дня народження
            day_of_week = next_birthday.weekday()
            day_name = weekdays[day_of_week]  # Отримуємо назву дня тижня

            # Перевіряємо, чи день народження падає на вихідний
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'  # Переносимо на понеділок

            # Додаємо ім'я користувача до відповідного дня тижня
            birthdays_per_week[day_name].append(name)

    # Видаляємо дні, для яких немає привітань
    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}

    # Повертаємо оновлений словник з іменами користувачів за днями тижня
    return birthdays_per_week

if __name__ == "__main":
    # Приклад вхідних даних (список користувачів)
    users = [
        {"name": "Maryna", "birthday": date(2023, 11, 3)},
        {"name": "Olia", "birthday": date(2023, 11, 4)},
        {"name": "Sasha", "birthday": date(2023, 11, 5)},
        {"name": "Sophia", "birthday": date(2023, 11, 6)},
        {"name": "Tania", "birthday": date(2023, 11, 7)},
        {"name": "Vova", "birthday": date(2023, 11, 8)},
        {"name": "Yehor", "birthday": date(2023, 11, 9)},
        {"name": "Valera", "birthday": date(2023, 11, 10)}
    ]

    # Викликаємо функцію і отримуємо результат
    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
