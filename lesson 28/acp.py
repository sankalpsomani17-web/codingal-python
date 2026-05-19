import math

class Circle:
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def get_area(self):
        """Compute and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        """Compute and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


radius_input = 5
my_circle = Circle(radius_input)

print(f"Radius: {radius_input}")
print(f"Area: {my_circle.get_area():.2f}")
print(f"Perimeter: {my_circle.get_perimeter():.2f}")
