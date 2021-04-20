def total_numbers(a=7, *numbers, **phonebook):
    print("My favoruite number is ", a)

    for num in numbers:
        print("num", num)

    for name, phone_number in phonebook.items():
        print(name, phone_number)


total_numbers(8, 2, 215, 43, 263, Sheikh=88019, Rafi=88017, Sowat=88015, Hossain=88016)
