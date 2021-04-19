class Person:
    def __init__(self, fname, lname=None):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f'\nYour name is {self.fname} {self.lname}')


R = Person("Sowat", "Rafi")
R.printName()


class Engineers(Person):
# It is inheriting from the Person (Parent Class)
    # def __init__(self, fname=None, lname=None):
        # Person.__init__(self, fname, lname)

    def printInformation(self):
        if self.lname is None:
            print(f'\nYour name is {self.fname}')
        else:
            print(f'\nYour name is {self.fname} {self.lname}')


employee_01 = Engineers("Engr.", "Rafi")
employee_01.printInformation()
