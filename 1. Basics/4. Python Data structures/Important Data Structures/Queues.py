# importing dequeue
from collections import deque

name = deque()

name.append("Yafi")
name.append("Era")

print(name)
name.popleft()
print(name)

# Empty list
names = []

# Adding items (Enqueue Operation)
names.append('Sheikh')
names.append('Mohammad')
names.append("Sowat")
names.append("Hossain")
names.append("Rafi")

names.pop(0)
names.pop(0)
names.pop(0)
print(names)

