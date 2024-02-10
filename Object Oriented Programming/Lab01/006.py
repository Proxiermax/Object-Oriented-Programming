# Python Lab 01 - 06
number = int(input("number :"))
for i in range(0, number + 1):
    x = number - i
    print(" " * x, end=" ")
    print("#" * i)