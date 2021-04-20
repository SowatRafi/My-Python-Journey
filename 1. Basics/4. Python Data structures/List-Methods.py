friends = ['Riyad', 'Afif', 'Faiyaz', 'Rafid', 'Ismam']
travelling = ['Chittagong', 'Sitakundo', 'Chadpur', 'Sonargau']

friends.extend(travelling)
print(f"\nAfter using extend method: \n{friends}")

number1_list = [1, 23, 2, 236, 5, 2354, 24, 65, 234]
number2_list = [123, 152, 524, 521, 347, 74, 746, 432]

number1_list.append(number2_list)
print(f"\nAfter using append method: \n{number1_list}")
print(f'The length of Number 1 list is {len(number1_list)}')
print(f'\nThe list 2: \n{number2_list}')

friends.sort()
print(f"\nAfter using sort method: \n{friends}")
number2_list.sort()
print(f"\nAfter using sort method: \n{number2_list}")
friends.sort(reverse=True)
print(f"\nAfter using sort method with reverse: \n{friends}")
number2_list.sort(reverse=True)
print(f"\nAfter using sort method with reverse: \n{number2_list}")

newList = [123, 123, 1234, 123, 23, 23, 321, 3214, 231, 32, 231, 32, 123]
print(f"\nAfter using count method: \n{newList.count(123)}")

print(f"\nAfter using index method: \n{friends.index('Sitakundo')}")
print(f"Length of Friends is now {len(friends)}")

friends.insert(0, 'Sreemangal')
print(f"\nAfter using insert method: \n{friends}")
print(f"Length of Friends is now {len(friends)}")

friends.pop(0)  # It removes the the index item
print(f"\nAfter using pop method with a index: \n{friends}")
print(f"Length of Friends is now {len(friends)}")

number1_list.pop()  # It removes the last item
print(f"\nAfter using pop method without a index: \n{number1_list}")
print(f"Length of Friends is now {len(number1_list)}")

number1_list.remove(1)
print(f"\nAfter using remove method: \n{number1_list}")

del newList  # Deleted the list
print(newList)  # 'newList' is not defined problem occurs
