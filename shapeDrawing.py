import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#E0C1F9")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance2 = turtle.Turtle()

''' turtle_instance.forward(100)
turtle_instance2.left(180)
turtle_instance2.forward(100)
'''
#drawing square
#  with one turtle

'''for i in range(4):
    turtle_instance.left(90)
    turtle_instance.forward(200)'''

#  with many turtles

turtle_instance3 = turtle.Turtle()
turtle_instance4 = turtle.Turtle()

#  kodu sonra bul

#drawing star

'''turtle_instance.forward(100)
for i in range(5):
    turtle_instance.left(72)
    turtle_instance.forward(100)
    if(i==4):
        break
    turtle_instance.right(144)
    turtle_instance.forward(100)'''

#dinamik şekil çizdirme

num_sides = 5
side_length = 100
angle = 360 / num_sides

for i in range(num_sides):
    turtle_instance.forward(100)
    turtle_instance.right(angle)


turtle.done()