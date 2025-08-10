# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method to calculate area. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize a circle with its radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
