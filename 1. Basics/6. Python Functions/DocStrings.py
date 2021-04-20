def convertInto_01(test_str):
    """
    Converting anything into binary

    :param test_str: str | int | float | bool
    :return: binary output (01)
    """

    result = ''.join(format(ord(i), '08b') for i in test_str)

    return result


name = "অ"

output = convertInto_01(name)
print(output)

print(convertInto_01.__doc__)
# print(print.__doc__)
# print("Sowat".join(".."))
# print(ord("R"))
