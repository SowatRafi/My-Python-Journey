# import Module
from Module import say_hello
from Module import fruits


# Module.say_hello("Rafi")
say_hello("Rafi")
print()

for k, v in fruits.items():
    print(f'{k}: {v}')
