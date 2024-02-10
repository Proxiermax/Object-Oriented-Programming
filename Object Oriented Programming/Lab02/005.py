def only_english(string):
    manage = [item for item in string if item.isalpha() and item.isascii()]
    result = ''.join(manage)
    return result

x = list(map(str, input("string :")))
result = only_english(x)
print(result)