student_marks = {
    'Sheikh': {'CSE': 3.50, 'MNS': 3.00, 'GEN': 3.30},
    'Mohammed': {'CSE': 3.30, 'MNS': 3.50, 'GEN': 4.00},
    'Sowat': {'CSE': 3.50, 'MNS': 3.75, 'GEN': 3.00},
    'Hossain': {'CSE': 4.00, 'MNS': 4.00, 'GEN': 4.00},
    'Rafi': {'CSE': 3.75, 'MNS': 3.00, 'GEN': 3.30},
}

s3 = student_marks['Sowat']
print(s3)

s4 = student_marks['Sowat']['CSE']
print(s4)

# Adding a dictionary inside a dictionary
student_marks["Rafi"] = {}
student_marks["Rafi"]["CS"] = 4.00
student_marks["Rafi"]["BBS"] = 3.75
student_marks["Rafi"]["Law"] = 2.3

print(student_marks["Rafi"])

student_marks.pop("Rafi")
print(student_marks)