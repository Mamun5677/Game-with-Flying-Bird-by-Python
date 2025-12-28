import turtle

wn = turtle.Screen()
wn.title("turtle race")

line = turtle.Turtle()
line.speed(0)
line.right(90)

total = 6
x_axis = -100
number = 0
while total > 0:
    line.penup()
    line.goto(x_axis, 100)
    line.write(number + 1, font=("", 10, "normal"))
    line.pendown()
    line.forward(200)

    total -= 1
    x_axis += 30
    number += 1

line.penup()
line.goto(80, 100)
line.pendown()
line.left(60)
line.pensize(width=4)

count = 0
while count < 10:
    line.forward(20)
    line.right(120)
    line.forward(20)
    line.left(120)
    count += 1

line.penup()
line.goto(97, 100)
line.pendown()
line.right(120)

while count < 20:
    line.forward(20)
    line.left(120)
    line.forward(20)
    line.right(120)
    count += 1
line.hideturtle()

turtle_1 = turtle.Turtle()
turtle_1.penup()
turtle_1.shape("turtle")
turtle_1.color("red")
turtle_1.goto(-100, 50)
turtle_1.pendown()

turtle_2 = turtle.Turtle()
turtle_2.penup()
turtle_2.shape("turtle")
turtle_2.color("blue")
turtle_2.goto(-100, 10)
turtle_2.pendown()

turtle_3 = turtle.Turtle()
turtle_3.penup()
turtle_3.shape("turtle")
turtle_3.color("green")
turtle_3.goto(-100, -30)
turtle_3.pendown()

while turtle_1.xcor() < 80 and turtle_2.xcor() < 80 and turtle_3.xcor() < 80:
    turtle_1.setx(turtle_1.xcor() + 3)
    turtle_2.setx(turtle_2.xcor() + 2.7)
    turtle_3.setx(turtle_3.xcor() + 2.4)

turtle.done()
