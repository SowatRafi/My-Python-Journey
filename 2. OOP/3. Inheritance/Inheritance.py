class Person:
    def __init__(self, fname, lname=None):
        self.fname = fname
        self.lname = lname

    def printName(self):
        if self.lname is None:
            print(f'\nYour name is {self.fname}')
        else:
            print(f'\nYour name is {self.fname} {self.lname}')


R = Person("Sowat", "Rafi")
R.printName()


class Engineers(Person):
    def __init__(self, fname, projectType, lname=None):
        Person.__init__(self, fname, lname)  # It is inheriting from the Person (Parent Class)
        self.projectType = projectType

    def printInformation(self):
        self.printName()  # Calling the Parent class method
        print(f"He is being specialized on {employee_01.projectType}")


employee_01 = Engineers(fname="Engr.", lname="Rafi", projectType="Web Applications")
employee_01.printInformation()
