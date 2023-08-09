# models/rectangle.py

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
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
