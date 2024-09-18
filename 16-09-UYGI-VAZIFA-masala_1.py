def split_list(lst, n):
    # Listni bo'lish
    result = [lst[i:i+n] for i in range(0, len(lst), n)]
    return result
lst = ["A","B","C","D","E","F","G","L","Q","U"]
n = int(input("Bo'lish uchun sonni kiriting: "))
output = split_list(lst, n)
print(output)
