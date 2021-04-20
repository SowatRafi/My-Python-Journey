def String_toBinary(message):
    result = "".join(format(ord(i), '08b') for i in message)
    return int(result)


def ASCII(message):
    result = "".join(format(ord(i)) for i in message)
    return int(result)


def BINARY(number):
    result = bin(number)
    return result


def OCTAL(number):
    result = oct(number)
    return result


def HEXADECIMAL(number):
    result = hex(number)
    return result

