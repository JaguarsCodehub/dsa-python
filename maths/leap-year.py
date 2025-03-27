def is_leap_year(year):
    return year % 4 == 0 and (year != 100 or year % 400 == 0)


year = 2023
print(is_leap_year(year))