from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    # Словник імен користувачів за днями тижня
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.weekday()

            # Якщо день народження на вихідних, то це як понеділок
            if weekday == 6 or weekday == 5:
                weekday_name = "Monday"
            else:
                weekday_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][weekday]

            birthdays[weekday_name].append(name)

    # print day of the week and name
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# тест
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 11, 2)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 7, 22)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 11, 3)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 28)}
]

get_birthdays_per_week(users)
 