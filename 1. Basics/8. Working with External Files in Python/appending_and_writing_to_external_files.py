file = open("quotes.txt", "a")

file.write("\nNot all those who wander are lost.")
file.write("\nFor those to whom much is given, much is required.")
file.write("\nGenius is one percent inspiration and ninety-nine percent perspiration.")

file.close()

file = open("quotes-02.txt", "w")
file.write("Go ahead, make my day.")

file.close()