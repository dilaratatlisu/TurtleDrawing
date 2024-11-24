import turtle

turtle_screen = turtle.Screen()
turtle_screen.title("Shrinking Square")
turtle_screen.bgcolor("#e0c1f9")
turtle_instance6 = turtle.Turtle()

sizeSquare = 250
def shrinking_turtle(size):
    for i in range(28):
        turtle_instance6.forward(size)
        turtle_instance6.right(90)
        size-=10

shrinking_turtle(sizeSquare)

turtle.done()