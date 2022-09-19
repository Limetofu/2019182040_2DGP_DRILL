import turtle

def move_w ():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_a ():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def move_s ():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def move_d ():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart ():
    turtle.reset()
    turtle.stamp()

def move_turtle ():
    turtle.onkey(move_w, 'w')
    turtle.onkey(move_a, 'a')
    turtle.onkey(move_s, 's')
    turtle.onkey(move_d, 'd')
    turtle.onkey(restart, 'Escape')

turtle.shape('turtle')
turtle.stamp()
move_turtle()
turtle.listen()
