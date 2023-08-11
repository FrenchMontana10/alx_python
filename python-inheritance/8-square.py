#!/usr/bin/python3
""" Rectangle module """
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initialize instance attributes """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Return a string representation of the object """
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
