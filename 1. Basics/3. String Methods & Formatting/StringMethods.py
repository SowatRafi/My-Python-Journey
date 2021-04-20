text = "Hello, Rafi"

print(len(text))
print(text.index(","))

text2 = "world is beautiful."
print(text2.capitalize())
upper = text2.upper()
print(upper)
lower = text.lower()
print(lower)
print(lower.islower())
print(lower.isupper())
print(upper.isupper())
print(upper.islower())

print(text.find("World"))
print(text.find("Rafi"))

text2 = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
print(text2.count("i"))

message = "You never give up.\nDON'T EVER TRY IT."
print(message)
print(message.split())
text2 = text2.replace("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii", "Alabu")
print(text + '\n' + text2 + "\n" + message)
