# Defining a list which stores the total marks of 500
total_score = [356, 405, 290, 389, 207, 403]


# Defining a function which calculates the total percentage
def percent(li):
    ans = (li * 100) / 500
    return ans


# Using map function
mapped_list = map(percent, total_score)
print(list(mapped_list))
