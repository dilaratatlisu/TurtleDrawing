import  turtle

turtle_screen = turtle.Screen()
turtle_screen.title("Spiral Helix")
turtle_screen.bgcolor("light blue")
turtle_colors = ["yellow", "dark blue", "purple", "black", "orange", "red"]
turtle_instance = turtle.Turtle()

for i in range(10):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(i*10)
    turtle_instance.circle(i*-10)
    turtle_instance.right(10)




turtle.done()