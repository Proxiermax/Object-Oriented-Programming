def is_plusone_dictionary(infomation):
    x = sum(i + 1 for i in range(len(infomation) * 2))
    y = sum(k + v for k, v in infomation.items())
    return True if x == y else False

infomation = {}
while True:
    numbers = input("Input [0 to exit]: ").split()
    if numbers[0] == '0':
        break
    if len(numbers) != 2:
        print("Please input key-value.")
        continue
    infomation[int(numbers[0])] = int(numbers[1])
print(infomation) 
check = is_plusone_dictionary(infomation)
print(check)