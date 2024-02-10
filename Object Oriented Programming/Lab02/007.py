# days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def day_of_year(date):
#     days_in_year = date[0]
#     flag_leap = is_leap(date[2])
#     for i in range(1, date[1]):
#         days_in_year += days_in_month[i]
#     if flag_leap and date[1] > 2:
#         days_in_year += 1
#     return days_in_year

# def is_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# date = list(map(int, input("Day-Month-Year: ").split()))
# days = day_of_year(date)
# print(days)

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(day: int, month: int, year: int) -> int:
    days_in_year = day
    flag_leap = is_leap(year)
    for i in range(1, month):
        days_in_year += days_in_month[i]
    if flag_leap and month > 2:
        days_in_year += 1
    return days_in_year

def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

date = list(map(int, input("Day-Month-Year: ").split()))
if len(date) != 3:
    print("Invalid date format. Please provide Day, Month, and Year.")
else:
    day, month, year = date
    days = day_of_year(day, month, year)
    print(days)
