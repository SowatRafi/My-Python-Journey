def my_decorator(function):
    def wrapper():
        myFun = function()
        convert_uppercase = myFun.upper()
        return convert_uppercase

    return wrapper


@my_decorator
def say_hello():
    return "hello world!"


# decorate = my_decorator(say_hello)
# print(decorate())

print(say_hello())


def binaryDecorator(funtion):
    def convertIntoBinary_01():
        myFun = funtion()
        result = ''.join(format(ord(i), '08b') for i in myFun)
        return int(result)
    return convertIntoBinary_01


@binaryDecorator
def myText():
    return "R"


print("\n", myText())
print(type(myText()))
