def myNum(b):
    return b + 1


def addNum(c):
    newNum = 7
    return c(newNum)


print(addNum(myNum))
