# List containing name of students
student_names = ['Sheikh', 'Mohammad', 'Sowat', 'Hossain', "Rafi"]

# List containing marks of students
student_marks = [97, 90, 85, 75, 70]

# Zipping names & marks of students
zipped_list = zip(student_names, student_marks)
zipped_list = list(zipped_list)

print(zipped_list)

# Unzipping the name & mark of the students
student_names, student_marks = zip(*zipped_list)
print("Names: ", list(student_names))
print("Marks: ", list(student_marks))
