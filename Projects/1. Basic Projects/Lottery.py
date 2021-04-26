import random

owner_lottery_numbers = []
winner_lottery_number = random.randint(12345, 54321)

owner_lottery_cards = int(input("How many lotteries do you have? "))

for x in range(0, owner_lottery_cards):
    number = random.randint(12345, 54321)
    """The purpose of the while loop is to check if the random numbers generated are unique as we do not want any 
    duplicates. If there are any duplicates then the while keeps generating random numbers until all nth numbers are 
    unique. """
    while number in owner_lottery_numbers:
        number = random.randint(12345, 54321)
    owner_lottery_numbers.append(number)

if winner_lottery_number in owner_lottery_numbers:
    print(f"You have own the lottery with the number of {winner_lottery_number}")

print("\nWinning number:")
print(winner_lottery_number)

print("\nOwner Numbers")
owner_lottery_numbers.sort(reverse=True)
print(owner_lottery_numbers)
