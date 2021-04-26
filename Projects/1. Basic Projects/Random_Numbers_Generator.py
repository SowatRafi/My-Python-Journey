import random
import csv


def Passwords(passAmount):
    strPassList1 = []
    for i in range(1, passAmount+1):
        strPass = ""
        for ix in range(1, 8):
            password = random.randint(1, 101)
            strPass += str(password)

        print(f"Password: {strPass}")

        heading = ["Serial", "Password"]
        strPassList1.append([str(i), strPass])

    y = "Output/Password7.csv"
    with open(y, "w") as work:
        z = csv.writer(work)
        z.writerow(heading)
        z.writerows(strPassList1)

    print(strPassList1)


Passwords(7)
