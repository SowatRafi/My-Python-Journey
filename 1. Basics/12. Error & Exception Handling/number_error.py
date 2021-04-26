while True:
    try:
        number = int(input("Enter a whole number: "))
        if 3 < (len(str(number))) < 6 or len(str(number)) == 7:
            break
    except ValueError:
        print("No valid integer entered.")
    else:
        print("Number should be within the length of 4 or 5 or 7")

print("Great you have entered an integer.")
