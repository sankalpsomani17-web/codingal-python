import math

def calculate_circumference(radius):
    """Calculates the circumference of a circle given its radius."""
    return 2 * math.pi * radius

# Get user input
try:
    r = float(input("Enter the radius of the circle: "))
    if r < 0:
        print("Radius cannot be negative.")
    else:
        circumference = calculate_circumference(r)
        print(f"The circumference of the circle is: {circumference:.2f}")
except ValueError:
    print("Invalid input. Please enter a numerical value.")
