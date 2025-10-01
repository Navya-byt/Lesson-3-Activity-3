import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # background colour

# Create turtle
pen = turtle.Turtle()
pen.pensize(3)                # thickness of the pen
pen.speed(3)                  # drawing speed (1=slow, 10=fast)

# List of colours for each side of the square
colors = ["red", "green", "blue", "orange"]

# Draw a square
for i in range(4):
    pen.color(colors[i])      # set pen colour
    pen.forward(100)          # move forward 100 units
    pen.right(90)             # turn 90 degrees to the right

# Keep the window open until clicked
screen.exitonclick()
print("The circumference of the circle is:",i)