def what_is_my_sign(day, month):
    if day >= 21 and month == 3 and day <= 31 or day <= 20 and month == 4:
        return "Овен"
    elif day >= 21 and month == 4 and day <= 29 or day <= 20 and month == 5:
        return "Телец"
    elif day >= 21 and month == 5 and day <= 31 or day <= 20 and month == 6:
        return "Близнаци"
    elif day >= 21 and month == 6 and day <= 30 or day <= 21 and month == 7:
        return "Рак"
    elif day >= 22 and month == 7 and day <= 31 or day <= 22 and month == 8:
        return "Лъв"
    elif day >= 23 and month == 8 and day <= 31 or day <= 22 and month == 9:
        return "Дева"
    elif day >= 23 and month == 9 and day <= 30 or day <= 22 and month == 10:
        return "Везни"
    elif day >= 23 and month == 10 and day <= 31 or day <= 21 and month == 11:
        return "Скорпион"
    elif day >= 22 and month == 11 and day <= 30 or day <= 21 and month == 12:
        return "Стрелец"
    elif day >= 22 and month == 12 and day <= 31 or day <= 19 and month == 1:
        return "Козирог"
    elif day >= 20 and month == 1 and day <= 31 or day <= 18 and month == 2:
        return "Водолей"
    else:
        return "Риби"
