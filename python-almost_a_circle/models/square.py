#!/usr/bin/python3
""" Combined Code """

class Base:
    # ... (same as before)

class Rectangle(Base):
    # ... (same as before)

class Square(Rectangle):
    """This class inherits from Rectangle and represents a square.
    """
    
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The ID for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

# Example usage
if __name__ == "__main__":
    r1 = Rectangle(4, 6)
    r1.display()
    print(r1)

    print("---")

    r2 = Rectangle(2, 2)
    r2.display()
    print(r2)

    print("---")

    s1 = Square(5)
    s1.display()
    print(s1)
    print(s1.area())

    print("---")

    s2 = Square(2, 2)
    s2.display()
    print(s2)
    print(s2.area())

    print("---")

    s3 = Square(3, 1, 3)
    s3.display()
    print(s3)
    print(s3.area())
    