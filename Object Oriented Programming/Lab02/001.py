# infomation = []
# zeroes = []
# leader = []
# result, x = 0, 1
# numbers = list(map(int, input("numbers (digits) :").split()))
# for i in range(min(len(numbers), 10)):
#     if numbers[i] != 0:
#         infomation.append(numbers[i])
#     else:
#         zeroes.append(numbers[i])
# infomation.sort()
# infomation.reverse()
# for i in range(len(zeroes)):
#     infomation.insert(len(infomation) - 1, 0)
# for i in range(len(infomation)):
#     result += infomation[i] * x
#     x *= 10
# print(infomation)
# print(zeroes)
# print("result :", result)

numbers = list(input("numbers (digit) :").split())
zero = 0
numbers.sort()
# print(numbers)
for digit in numbers:
    if digit == '0':
        zero += 1
        # print("count 0")
    else:
        print(str(digit) + '0'*zero, end="")
        zero = 0