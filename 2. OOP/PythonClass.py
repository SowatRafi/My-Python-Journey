class Instructors:
    companyName = "SoWaT"

    def __init__(self, course, duration):
        self.course = f"\n{course} for everybody"
        self.duration = f"{duration} hours\n"

    def printInformation(self):
        print("\nMy Company name is ", Instructors.companyName)


class Pets:
    pass


programming_learning = Instructors("Python", 8)
framework_learning = Instructors("Django", 4)

programming_learning.printInformation()

print(programming_learning.course)
print(programming_learning.duration)

print(framework_learning.course)
print(framework_learning.duration)

programming_learning.course = "JavaScript"
print(programming_learning.course)

del programming_learning.duration
print(programming_learning.duration)  # Give me an error because already deleted.
