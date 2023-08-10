#!/usr/bin/python3
"""
9-main
This script demonstrates the use of the Square class.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square. Inherits attributes and methods from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The ID for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloaded __str__ method to represent the Square object as a string.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

if __name__ == "__main__":
    # Creating Square instances and testing methods
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

       
