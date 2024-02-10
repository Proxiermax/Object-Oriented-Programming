def count_char_in_string(x, c):
    result = [temp.count(c) for temp in x]
    return result

x = list(map(str, input("list of x :").split()))
c = input("1 char :")
print(count_char_in_string(x, c))