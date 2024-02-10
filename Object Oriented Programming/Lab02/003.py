def delete_minus(x):
    result = [[item for item in sub if item >= 0] for sub in x]
    return result

x = []
while True:
    numbers = input("Enter sublist :").split()
    if '0' in numbers:
        break
    numbers = list(map(int, numbers))
    x.append(numbers)
display = delete_minus(x)
print(display)