#!/usr/bin/python3
""" Combined Code """

class Base:
    """This class will be the base of all other classes in the project.
    
    It manages the id attribute for all future classes and avoids duplicating code.
    """

    # Private class attribute to keep track of the number of objects created
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Constructor for the Base class.

        Args:
            id (int, optional): The ID for the instance. Defaults to None.
        """
        if id is not None:
            # If an id is provided, assign it to the instance's id attribute
            self.id = id
        else:
            # If no id is provided, increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

class Rectangle(Base):
    """This class inherits from the Base class and represents a rectangle.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The ID for the instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def display(self):
        """Display the rectangle using # characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def update(self, *args, **kwargs):
        """Update attributes based on arguments."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

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
