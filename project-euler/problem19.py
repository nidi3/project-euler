def len(year, month):
    if month == 2: return 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    if month == 4 or month == 6 or month == 9 or month == 11: return 30
    return 31


year = 1900
month = 1
day = 1
sundays = 0
while year < 2001:
    if year>=1901 and day == 0: sundays += 1
    day = (day + len(year, month)) % 7
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

print sundays