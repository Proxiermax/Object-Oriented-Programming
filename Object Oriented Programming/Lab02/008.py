days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(date):
    days_in_year = date[0]
    flag_leap = is_leap(date[2])
    for i in range(1, date[1]):
        days_in_year += days_in_month[i]
    if flag_leap and date[1] > 2:
        days_in_year += 1
    return days_in_year

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      return True
    return False

def year_diff(past, current):
    not_leap_year = 0
    leap_year = 0
    if past == current or current - past == 1:
        return 0, 0
    for i in range(past + 1, current):
        if i % 4 == 0:
            leap_year += 1
        else:
            not_leap_year += 1
    return leap_year, not_leap_year

def date_diff(date01, date02):
    # date01 = list(map(int, date01.split('-')))
    # date02 = list(map(int, date02.split('-')))
    days01 = day_of_year(date01)
    days02 = day_of_year(date02)
    # years_between = [i for i in range(date01[2] + 1, date02[2])]
    # years_between = [365 if not is_leap(i) else 366 for i in years_between]
    # days_between_years = sum([i for i in years_between])
    days_between_years = sum(365 if not is_leap(i) else 366 for i in range(date01[2] + 1, date02[2]))
    days_until_end = 365 - days01 if not is_leap(date01[2]) else 366 - days01
    if date01[2] == date02[2]:
        result = days02 - days01
        return result + 1
    if date01[2] != date02[2]:
        result = days02 + days_until_end + days_between_years
        return result + 1

date01 = list(map(int, input("Day-Month-Year 01 :").split()))
date02 = list(map(int, input("Day-Month-Year 02 :").split()))
result = date_diff(date01, date02)
print(result)
