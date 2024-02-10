def add2list(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Error"
    return [lst1[i] + lst2[i] for i in range(len(lst1))]
    
lst1 = list(map(int, input("input list01 :").split()))
lst2 = list(map(int, input("input list02 :").split()))
result = add2list(lst1, lst2)
print(result)