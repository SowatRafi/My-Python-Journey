my_list = [2, 3, 5, 6, 365, 24, 24, 243]
desire = input("\nPlease enter your desire number.\nWe will check if it is the list or not!\n-> ")

for match in range(len(my_list)):
    if my_list[match] == int(desire):
        print(f"Element found at index[{match}]")
        break
    else:
        print(f"Element not found in index[{match}]")

# (Worst-Case Scenario) => Time Complexity -> O(n)
