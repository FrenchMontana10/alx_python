#!/usr/bin/python3
""" 0-main """

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

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
