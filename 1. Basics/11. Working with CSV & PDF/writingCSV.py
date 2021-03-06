import csv

data = ["Month", "1998", "1999", "2000"]
x = [
    ["JAN", 340, 360, 417],
    ["FEB", 318, 342, 391],
    ["MAR", 362, 406, 419],
    ["APR", 348, 396, 461],
    ["MAY", 363, 420, 535],
    ["JUN", 349, 340, 234],
    ["JUL", 343, 760, 235],
    ["AUG", 346, 860, 836],
    ["SEP", 343, 460, 844],
    ["OCT", 345, 345, 242],
    ["NOV", 343, 308, 625],
    ["DEC", 343, 960, 725],
]

y = "CSV files/Years.csv"
with open(y, "w") as work:
    z = csv.writer(work)
    z.writerow(data)
    z.writerows(x)

print("Check in the '", y, "' folder.")
