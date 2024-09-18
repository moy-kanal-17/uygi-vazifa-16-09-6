def co(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
string = "mississippi"
char_count = co(string)
print(char_count)
