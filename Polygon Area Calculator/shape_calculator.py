# FCC Course: Scientific Computing with Python
# Project: Polygon Area Calculator
# Author: Wojciech Woźniak
# Date: 12.05.2023


# Definition of the Rectangle class
class Rectangle:

    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # set_width() method
    def set_width(self, width):
        self.width = width

    # set_height() method
    def set_height(self, height):
        self.height = height

    # get_area() method
    def get_area(self):
        return self.width * self.height

    # get_perimeter() method
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # get_diagonal() method
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    # get_picture() method
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
                picture += "*" * self.width + "\n"
            return picture

    # get_amount_inside() method
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    # __str__() method
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Definition of the Square class
class Square(Rectangle):

    # Constructor
    def __init__(self, side):
        self.width = side
        self.height = side

    # set_side() method
    def set_side(self, side):
        self.width = side
        self.height = side

    # set_width() method
    def set_width(self, width):
        self.width = width
        self.height = width

    # set_height() method
    def set_height(self, height):
        self.width = height
        self.height = height

    # __str__() method
    def __str__(self):
        return f"Square(side={self.width})"
