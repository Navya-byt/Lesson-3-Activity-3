import turtle
my = turtle.Screen()
my.bgcolor("pink")
my.title("turtle")
my = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my.fd(size+1)
        my.left(90)
        size = size - 5
    size = size + 1