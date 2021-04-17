def greeting():
    def say_hello():
        return "Hello"
    return say_hello

value = greeting()

print(value())