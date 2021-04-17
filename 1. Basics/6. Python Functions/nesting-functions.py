def mynum(a):
    def num(a):
        return a + 1
    result = num(a)
    return result

print(mynum(4))