"""this is an empty class"""
class metaclassbase(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    """this is my class"""
class BaseGeometry(metaclass = metaclassbase):
    """this is a place holder for this empty class"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    
    def area(self):
        raise Exception("area() is not implemented")

    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        



class Rectangle(BaseGeometry):
    """This is a class that inherits from the BaseGeometry Class"""
    def __init__(self, width, height):
      
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)  