def ha(lst):
    return len(lst) != len(set(lst))
lst1 = ['olma', 'anor', 'gilos', True, 12, 10, 'olma', 'gilos', 1]
lst2 = ['olma', 'anor', 'gilos', True, 12, 10, 'banan', 9]

if ha(lst1):
    print("Bu listda dublikatlar bor.")
else:
    print("Bu listda dublikatlar yo'q.")

if ha(lst2):
    print("Bu listda dublikatlar bor.")
else:
    print("Bu listda dublikatlar yo'q.")
