def iss(lst):
    return lst == sorted(lst)
lst1 = [1,4,2,6,8,9]
lst2 = [1,3,6,7,8,10]

print(iss(lst1))  
print(iss(lst2))  
