fruits = ['grapes', 'berries']
myFruits = ['grapes', 'berries']
favFruits = fruits

print(fruits is favFruits)
print(fruits is myFruits) #Objects are not same, even though they have same variables
print('apples' not in fruits)