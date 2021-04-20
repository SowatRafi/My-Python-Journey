import random
import platform


x = random.random()
print(x)

x = random.randint(12, 24)
print(x)

y = platform.system()
print(f'The Operating Sysem name is {y}')