import turtle

# Set up the screen
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300, 400)

# Create a turtle object
polygon = turtle.Turtle()

# Define the number of sides and the length of each side
num_sides = 6
side_length = 70

# Calculate the angle to turn at each vertex
angle = 360.0 / num_sides

# Draw the polygon
for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

# Finish the drawing
turtle.done()