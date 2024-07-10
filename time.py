def time():
    try:
        hours = int(input('Введите час: '))
        if hours not in range(24):
            print('Неверное количество часов!')
            exit()
        minutes = int(input('Введите минуты: '))
        if minutes not in range(60):
            print('Неверное количество минут!')
            exit()
        seconds = int(input('Введите секунды: '))
        if seconds not in range(60):
            print('Неверное количество секунд!')
            exit()
    except:
        print('Введено не число!')
        exit()
    minutes += hours * 60
    seconds += minutes * 60
    seconds = int(seconds * (125 / 108))
    minutes = seconds // 100
    seconds %= 100
    hours = minutes // 100
    minutes %= 100
    if minutes < 10:
        minutes = str(f'0{minutes}')
    if seconds < 10:
        seconds = str(f'0{seconds}')
    print(f'{hours}:{minutes}:{seconds}')


def date():
    try:
        is_leap = int(input('Год – високосный? (0/1): '))
        if is_leap not in (0, 1):
            print('Неверные данные!')
            exit()
        month = int(input('Введите номер месяца: '))
        if month not in range(1, 13):
            print('Неверный номер месяца!')
            exit()
        day = int(input('Введите номер дня: '))
        if (month in (1, 3, 5, 7, 8, 10, 12) and day not in range(1, 32)) or (month in (4, 6, 9, 11) and day not in range(1, 31)) or (month == 2 and is_leap == 0 and day not in range(1, 29)) or (month == 2 and is_leap == 1 and day not in range(1, 30)):
            print('Неверный номер дня!')
            exit()
    except:
        print('Введено не число!')
        exit() #В комментах – предыдущий месяц
    if month == 2: day += 31 #Jan
    elif month == 3: day += 59 #feb
    elif month == 4: day += 90 #mar
    elif month == 5: day += 120 #apr
    elif month == 6: day += 151 #may
    elif month == 7: day += 181 #jun
    elif month == 8: day += 212 #jul
    elif month == 9: day += 243 #aug
    elif month == 10: day += 273 #sep
    elif month == 11: day += 304 #oct
    elif month == 12: day += 334 #nov
    if is_leap == 1 and month >= 3:
        day += 1
    month = day // 30 + 1
    if month == 13:
        month = 'остаточные дни'
    day %= 30
    if day == 0:
        day = 30
        month -= 1
    print(f'День: {day}, месяц: {month}')


if (choice := input('''1. Конвертация времени
2. Конвертация даты
Выберите режим: ''')) == '1':
    time()
elif choice == '2':
    date()
else:
    print('Ошибка')
