"""
# Opening the file
f = open('quotes.txt', 'r')  # reading mode

print(f.readable(), "\n")  # checking readable or not

print(f.read())  # reading the file
f.close()  # closing

print(f.readable())

"""

files = open("quotes.txt")

# print(files.read(10))  # Prints the characters

# print(files.readline())  # 1 line only
# print(files.readlines())  # makes lines into a list

# reading line with a for loop
for line in files:
    print(line)

files.close()
