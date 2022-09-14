import turtle

turtle.goto(0, 500)
turtle.left(90)

xline = 0
count = 0
while (xline <= 4):
  count = 0
  while (count <= 3):
    turtle.right(90)
    turtle.forward(100)
    count += 1
  turtle.goto((xline + 1) * 100,500)
  xline += 1



xline = 0
count = 0
turtle.penup()
turtle.goto(0, 400)

turtle.pendown()
while (xline <= 4):
  count = 0
  while (count <= 3):
    turtle.right(90)
    turtle.forward(100)
    count += 1
  turtle.goto((xline + 1) * 100,400)
  xline += 1

xline = 0
count = 0
turtle.penup()
turtle.goto(0, 300)
turtle.pendown()
while (xline <= 4):
  count = 0
  while (count <= 3):
    turtle.right(90)
    turtle.forward(100)
    count += 1
  turtle.goto((xline + 1) * 100,300)
  xline += 1

xline = 0
count = 0
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
while (xline <= 4):
  count = 0
  while (count <= 3):
    turtle.right(90)
    turtle.forward(100)
    count += 1
  turtle.goto((xline + 1) * 100,200)
  xline += 1

xline = 0
count = 0
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
while (xline <= 4):
  count = 0
  while (count <= 3):
    turtle.right(90)
    turtle.forward(100)
    count += 1
  turtle.goto((xline + 1) * 100,100)
  xline += 1




turtle.exitonclick()
    


