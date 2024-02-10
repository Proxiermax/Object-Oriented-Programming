# Python Lab 01 - 04
result = 0
x = 1111
number = int(input("input(1 - 9) :"))
if number >= 0 and number < 10:
    for i in range(1, 4 + 1):
        result += number * x
        x = x // 10
    print("output :", result)
else:
    print("please, enter input in range(1 - 9)")