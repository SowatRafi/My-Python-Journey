# Defining a list of marks of the students of 100
scores = [48, 45, 78, 95, 98, 87, 85, 85, 72, 67, 56, ]


# Defining a function which checks if marks scored are > 50
def score_check(s):
    if s > 50:
        return True
    else:
        return False


# Filtering the students with marks > 50
students_passed = filter(score_check, scores)
for i in students_passed:
    print(i)
