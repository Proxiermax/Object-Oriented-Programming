def count_char(string):
    count = {x: string.count(x) for x in string}
    return count

string = input("input string: ")
result = count_char(string)
print("letter counts :", result)