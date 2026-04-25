import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw the four sides of the square
for _ in range(4):
    my_turtle.forward(100) # Move forward 100 units
    my_turtle.right(90)    # Turn right 90 degrees

# Keep the window open until clicked
turtle.done()

