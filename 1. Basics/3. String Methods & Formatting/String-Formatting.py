name = "rafi"
age = 22
profession = "engineer"

print(f'Hello {name.upper()}, your age is {age}.')

message = (
    f'Hi, {name.capitalize()}.'
    f'You are a {profession.capitalize()}.'
    f'You current age is {age} years old.'
)

print(message)

print()

bike = {'brand': 'Yamaha', 'model': 'MT15'}
print(f"The bike I like to buy {bike['brand']} {bike['model']}.")