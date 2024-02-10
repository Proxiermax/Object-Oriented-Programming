# Python Lab 01 - 01  
result = []
for number in range(2000, 3200):
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))
output = ', '.join(result)
print(output)

for number in range(2000, 3200):
    if number % 7 == 0 and number % 5 != 0:
        print(number, end=", ")