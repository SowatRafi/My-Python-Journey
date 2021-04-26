import random

guesses = []
my_computer = random.randint(1, 100)
player = int(input("Enter a number between 1-100: "))
guesses.append(player)

while player != my_computer:
    if player > my_computer:
        print("Number is too high")
    else:
        print("Number is too low.")

    while True:
        try:
            player = int(input("Enter your number between 1-100: "))
            if 0 < player < 101:
                guesses.append(player)
                break
        except ValueError:
            print("No valid integer entered.")
        else:
            print("Number should be within the length of 1 - 100")

else:
    print("\n\nYou have guessed right! Good job Babex...")
    print("It took you %i guesses." % len(guesses))
    print("There are your guesses: ")
    for guess in guesses:
        if guess == guesses[len(guesses)-1]:
            print(f"{guess}.")
        else:
            print(f'{guess}, ', end="")