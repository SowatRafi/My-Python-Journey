x = 10

def my():
    global x  # Converting the inside x to global
    print(x)
    x = 7
    print("My favourite number is ", x)

my()
print(x)