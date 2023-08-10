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
        
    # ... (previous methods and properties)
    
    def update(self, *args):
        """Update attributes based on arguments."""
        attributes = ["id", "width", "height", "x", "y"]
        for index, value in enumerate(args):
            if index < len(attributes):
                setattr(self, attributes[index], value)
    
    # ... (previous methods and properties)

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(12)
    print(r1)

    r1.update(12, 4)
    print(r1)

    r1.update(12, 4, 3)
    print(r1)

    r1.update(12, 4, 3, 2)
    print(r1)

    r1.update(12, 4, 3, 2, 1)
    print(r1)
