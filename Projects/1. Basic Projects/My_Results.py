total_courses = int(input("How many courses have you completed? => "))

GPA = {}
for x in range(total_courses):
    course = input('Course Name? => ')
    gpa = float(input(f"Enter GPA of {course}: "))
    GPA[course] = gpa
    print("Updated Dictionary is: ", GPA)


def Safe_Subjects(gpa=GPA):
    safe_subjects = dict(filter(lambda x: x[1] > 2.24, gpa.items()))
    return safe_subjects


def Risk_Subjects(gpa=GPA):
    risk_subjects = dict(filter(lambda x: x[1] < 2.24, gpa.items()))
    return risk_subjects


def GPA4_Subjects(gpa=GPA):
    gpa4_subjects = dict(filter(lambda x: x[1] == 4.0, gpa.items()))
    return gpa4_subjects


def GPA_3_7_Subjects(gpa=GPA):
    gpa_3_7_subjects = dict(filter(lambda x: x[1] == 3.7, gpa.items()))
    return gpa_3_7_subjects


def GPA_3_3_Subjects(gpa=GPA):
    gpa_3_3_subjects = dict(filter(lambda x: x[1] == 3.3, gpa.items()))
    return gpa_3_3_subjects


def GPA3_Subjects(gpa=GPA):
    gpa3_subjects = dict(filter(lambda x: x[1] == 3.0, gpa.items()))
    return gpa3_subjects


def GPA_2_7_Subjects(gpa=GPA):
    gpa_2_7_subjects = dict(filter(lambda x: x[1] == 2.7, gpa.items()))
    return gpa_2_7_subjects


def GPA_2_3_Subjects(gpa=GPA):
    gpa_2_3_subjects = dict(filter(lambda x: x[1] == 2.3, gpa.items()))
    return gpa_2_3_subjects


def GPA2_Subjects(gpa=GPA):
    gpa2_subjects = dict(filter(lambda x: x[1] == 2.0, gpa.items()))
    return gpa2_subjects


def GPA_1_7_Subjects(gpa=GPA):
    gpa_1_7_subjects = dict(filter(lambda x: x[1] == 1.7, gpa.items()))
    return gpa_1_7_subjects


def GPA_1_3_Subjects(gpa=GPA):
    gpa_1_3_subjects = dict(filter(lambda x: x[1] == 1.3, gpa.items()))
    return gpa_1_3_subjects


def GPA1_Subjects(gpa=GPA):
    gpa1_subjects = dict(filter(lambda x: x[1] == 1.0, gpa.items()))
    return gpa1_subjects


def GPA_0_7_Subjects(gpa=GPA):
    gpa_0_7_subjects = dict(filter(lambda x: x[1] == 0.7, gpa.items()))
    return gpa_0_7_subjects


def GPA0_Subjects(gpa=GPA):
    gpa0_subjects = dict(filter(lambda x: x[1] == 0.0, gpa.items()))
    return gpa0_subjects


def Printing_Dict(dicto):
    for k, v in dicto.items():
        print(k, ":", v)


def CGPA_WISE(desire2):

    gpa4 = GPA4_Subjects()
    gpa_3_7 = GPA_3_7_Subjects()
    gpa_3_3 = GPA_3_3_Subjects()
    gpa3 = GPA3_Subjects()
    gpa_2_7 = GPA_2_7_Subjects()
    gpa_2_3 = GPA_2_3_Subjects()
    gpa2 = GPA2_Subjects()
    gpa_1_7 = GPA_1_7_Subjects()
    gpa_1_3 = GPA_1_3_Subjects()
    gpa1 = GPA1_Subjects()
    gpa_0_7 = GPA_0_7_Subjects()
    gpa0 = GPA0_Subjects()

    if desire2 == 4.00 or desire2 == 4 or desire2 == 4.0:
        print(f'\nTotal credits: {len(gpa4) * 3}')
        Printing_Dict(gpa4)

    elif desire2 == 3.70 or desire2 == 3.7:
        print(f'\nTotal credits: {len(gpa_3_7) * 3}')
        Printing_Dict(gpa_3_7)
    elif desire2 == 3.30 or desire2 == 3.3:
        print(f'\nTotal credits: {len(gpa_3_3) * 3}')
        Printing_Dict(gpa_3_3)
    elif desire2 == 3.00 or desire2 == 3 or desire2 == 3.0:
        print(f'\nTotal credits: {len(gpa4) * 3}')
        Printing_Dict(gpa3)

    elif desire2 == 2.70 or desire2 == 2.7:
        print(f'\nTotal credits: {len(gpa_2_7) * 3}')
        Printing_Dict(gpa_2_7)
    elif desire2 == 2.30 or desire2 == 2.3:
        print(f'\nTotal credits: {len(gpa_2_3) * 3}')
        Printing_Dict(gpa_2_3)
    elif desire2 == 2.00 or desire2 == 2 or desire2 == 2.0:
        print(f'\nTotal credits: {len(gpa2) * 3}')
        Printing_Dict(gpa2)

    elif desire2 == 1.70 or desire2 == 1.7:
        print(f'\nTotal credits: {len(gpa_1_7) * 3}')
        Printing_Dict(gpa_1_7)
    elif desire2 == 1.30 or desire2 == 1.3:
        print(f'\nTotal credits: {len(gpa_1_3) * 3}')
        Printing_Dict(gpa_1_3)
    elif desire2 == 1.00 or desire2 == 1 or desire2 == 1.0:
        print(f'\nTotal credits: {len(gpa1) * 3}')
        Printing_Dict(gpa1)

    elif desire2 == 0.70 or desire2 == 0.7:
        print(f'\nTotal credits: {len(gpa_0_7) * 3}')
        Printing_Dict(gpa_0_7)
    elif desire2 == 0.00 or desire2 == 0 or desire2 == 0.0:
        print(f'\nWasted credits: {len(gpa0) * 3}')
        Printing_Dict(gpa0)


if __name__ == '__main__':
    safe = Safe_Subjects()
    risk = Risk_Subjects()

    desire = input("What do you want to see?\n'Risk' or 'Safe' => ")
    try:
        if desire.lower() == "risk":
            print(f'\nWasted credits: {len(risk) * 3}')
            Printing_Dict(risk)
        elif desire.lower() == "safe":
            print(f'\nSolid credits: {len(safe) * 3}')
            Printing_Dict(safe)
        else:
            print("(Input is not as expected)...\nShowing you all the list by the way!")
            Printing_Dict(GPA)
    except:
        print("Something went wrong with our program.")

    desire2 = float(input("\nWhich GPA you want to see now?\n4.00, 3.70, 3.30, 3.00, 2.70, 2.30, 2.00, 1.70, 1.30, 1.00, 0.7 or 0.00? => "))
    try:
        CGPA_WISE(desire2)

    except:
        print("Something went wrong with our program.")
    else:
        print("\nProgram finished.")