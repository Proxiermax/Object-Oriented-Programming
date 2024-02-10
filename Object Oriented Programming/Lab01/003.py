# Python Lab 01 - 03
start01, start02, final01, final02 = input("input :").split()
start01 = int(start01)
start02 = int(start02)
final01 = int(final01)
final02 = int(final02)
hours = final01 - start01
minutes = final02 - start02
if (hours == 0 and minutes <= 15) or (hours == 1 and final02 - (60 - start02) <= 15):
    price = 0
    print(price)
else:
    if minutes > 0:
        hours += 1
    if hours <= 3:
        price = 10 * hours
        print(price)
    elif hours >= 4 and hours <= 6:
        price = (20 * (hours - 3)) + 30
        print(price)
    else:
        price = 200
        print(price)