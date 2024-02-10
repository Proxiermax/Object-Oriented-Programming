def count_minus(x):
    return sum(1 for item in x if item < 0)
    
x = list(map(int, input("numbers :").split()))
result = count_minus(x)
print(result)