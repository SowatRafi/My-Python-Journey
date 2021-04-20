#  Calling the Converter from the System Module
from System import Converter

Sting_binary = Converter.String_toBinary("R")
ascii_value = Converter.ASCII("R")
binary = Converter.BINARY(79)
octal = Converter.OCTAL(777)
hexadecimal = Converter.HEXADECIMAL(234)


print(Sting_binary)
print(binary)
print(ascii_value)
print(octal)
print(hexadecimal)
