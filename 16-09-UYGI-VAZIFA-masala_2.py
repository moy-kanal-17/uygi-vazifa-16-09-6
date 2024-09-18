def co(lst):
    myDct = {}
    for element in lst:
        if element in myDct:
            myDct[element] += 1
        else:
            myDct[element] = 1
    return myDct
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
myDct = co(myList)
print(myDct)
