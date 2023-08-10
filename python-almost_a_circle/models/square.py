#!/usr/bin/python3
""" Base class module """

class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize instance with ID """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize instance attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Other methods of Rectangle class...

class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize instance attributes """
        super().__init__(size, size, x, y, id)

    # Other methods of Square class...

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
