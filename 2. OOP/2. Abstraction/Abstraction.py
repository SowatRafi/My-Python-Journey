"""
    Python does not have its own provided abstract classes.
    However, Python comes with a module which provides the infrastructure that allows you to define abstract classes.
    The name of the module in ABC => Abstract Based Classes
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


# my_shape = Shape()

my_square = Square(5)
print(my_square.area())
print(my_square.perimeter())
