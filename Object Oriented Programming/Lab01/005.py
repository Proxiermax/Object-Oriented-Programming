# Python Lab 01 - 05
found = False
max_palindrome = 0
max_x = 0
max_y = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        calculate = x * y
        convert = int(str(calculate)[::-1])
        if calculate == convert and calculate > max_palindrome:
            max_palindrome = calculate
            max_x = x
            max_y = y
print("palindrome is", max_palindrome, "by", max_x, "*", max_y)