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
    check_real = check_date(date01, date02)
    if not check_real:
        return -1
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
    
def check_date(date01, date02):
    if (date01[1] < 1 or date01[1] > 12):
        return False
    if (date02[1] < 1 or date02[1] > 12):
        return False
    
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    
    if date01[1] in month_31:
        if date01[0] < 1 or date01[0] > 31:
            return False
    elif date01[1] in month_30:
        if date01[0] < 1 or date01[0] > 30:
            return False
    else:
        leap_year = is_leap(date01[2])
        if leap_year:
            if date01[0] < 1 or date01[0] > 29:
                return False
        else:
            if date01[0] < 1 or date01[0] > 28:
                return False
            
    if date02[1] in month_31:
        if date02[0] < 1 or date02[0] > 31:
            return False
    elif date02[1] in month_30:
        if date02[0] < 1 or date02[0] > 30:
            return False
    else:
        leap_year = is_leap(date02[2])
        if leap_year:
            if date02[0] < 1 or date02[0] > 29:
                return False
        else:
            if date02[0] < 1 or date02[0] > 28:
                return False
    return True
            
date01 = list(map(int, input("Day-Month-Year 01 :").split()))
date02 = list(map(int, input("Day-Month-Year 02 :").split()))
result = date_diff(date01, date02)
print(result)

# try:
#     date01 = list(map(int, input("Day-Month-Year 01 :").split()))
#     date02 = list(map(int, input("Day-Month-Year 02 :").split()))
    
#     if (date01[1] < 1 or date01[1] > 12):
#         raise ValueError("Invalid month value in date01")
#     if (date02[1] < 1 or date02[1] > 12):
#         raise ValueError("Invalid month value in date02")
    
#     month_31 = [1, 3, 5, 7, 8, 10, 12]
#     month_30 = [4, 6, 9, 11]
    
#     if date01[1] in month_31:
#         if date01[0] < 1 or date01[0] > 31:
#             raise ValueError("Invalid day value for month in date01:", date01[1])
#     elif date01[1] in month_30:
#         if date01[0] < 1 or date01[0] > 30:
#             raise ValueError("Invalid day value for month in date01:", date01[1])
#     else:
#         leap_year = is_leap(date01[2])
#         if leap_year:
#             if date01[0] < 1 or date01[0] > 29:
#                 raise ValueError("Invalid day value for leap February in date01")
#         else:
#             if date01[0] < 1 or date01[0] > 28:
#                 raise ValueError("Invalid day value for non-leap February in date01")
            
#     if date02[1] in month_31:
#         if date02[0] < 1 or date02[0] > 31:
#             raise ValueError("Invalid day value for month in date02:", date02[1])
#     elif date02[1] in month_30:
#         if date02[0] < 1 or date02[0] > 30:
#             raise ValueError("Invalid day value for month in date02:", date02[1])
#     else:
#         leap_year = is_leap(date02[2])
#         if leap_year:
#             if date02[0] < 1 or date02[0] > 29:
#                 raise ValueError("Invalid day value for leap February in date02")
#         else:
#             if date02[0] < 1 or date02[0] > 28:
#                 raise ValueError("Invalid day value for non-leap February in date02")
            
#     result = date_diff(date01, date02)
#     print(result)
    
# except Exception as e:
#     print(e)