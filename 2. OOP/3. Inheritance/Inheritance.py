class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(f'\nYour name is {self.fname} {self.lname}')


R = Person("Sowat", "Rafi")
R.printName()


class Engineers(Person):
    pass


employee_01 = Engineers("Engr.", "Rafi")
employee_01.printName()
