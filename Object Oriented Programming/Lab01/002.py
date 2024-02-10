# Python Lab 01 - 02
big = [];
small = [];
string = input("input: ")
for i in string:
    i = ord(i)
    if i >= 65 and i <= 90:
        i = chr(i)
        big.append(i)
    elif i >= 97 and i <= 122:
        i = chr(i)
        small.append(i)
print("Big:", len(big))
print("Small:", len(small))