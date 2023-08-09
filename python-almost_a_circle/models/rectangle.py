""" we import the base class"""
from .base import Base
"""this is definition of class Rectangle"""
class Rectangle(Base):
    """here we have the constructor of the Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = self.__validate_integer_positive("width", width)
        self.__height = self.__validate_integer_positive("height", height)
        self.__x = self.__validate_integer_nonnegative("x", x)
        self.__y = self.__validate_integer_nonnegative("y", y)
        
        
        
    """ 
    This the 
    Getter  for width specifies
    the getter method for the Rectangle class
    """
    def get_width(self):
        return self.__width
    
    
    """setter for width"""
    def set_width(self, width):
        if width > 0:
            self.__width = width
    
    """Getter  for height"""
    def get_height(self):
        return self.__height
    """setter for width"""
    def set_height(self, height):
        if height > 0:
            self.__height = height
    
    """Getter  for x"""
    def get_x(self):
        return self.__x
    """setter for x"""
    def set_x(self, x):
        self.__x = x
    
    """Getter for y"""
    def get_y(self):
        return self.__y
    """setter for y"""
    def set_y(self, y):
        self.__y = y
        
        """the validator methods are here"""

    def __validate_integer_positive(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
        return value

    def __validate_integer_nonnegative(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        return value
