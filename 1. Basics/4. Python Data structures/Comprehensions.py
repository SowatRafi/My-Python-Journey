"""
Comprehensions in Python

Comprehensions in Python provide us with a short and concise way to construct new sequence(list, set and dictionary) 
using sequences which has already been defined.
* List Comprehensions,
* Set Comprehension &
* Dictionary Comprehensions.

"""

# Defining a list

my_list = [97, 90, 85, 75, 70]

# Using list comprehension
ultimate_list = [value ** 2 for value in my_list if value % 2 == 1]  # Square of odd numbers
print(ultimate_list)
even_half = [value/2 for value in my_list if value % 2 == 0]  # Half of even numbers
print(even_half)

for ix in even_half:
    ultimate_list.append(ix)

print(f'\nList: {ultimate_list}')

# Using set comprehensions
numbers = {ix for ix in range(1, 11)}  # Making a set using a loop
print(f'Set: {numbers}')

# Using dictionary comprehensions
di = {number: number**2 for number in range(1, 11)}  # Making a dictionary using a loop
print(f'Dictionary: {di}')
