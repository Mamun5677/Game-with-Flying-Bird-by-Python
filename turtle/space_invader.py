import turtle
import time

# screen
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.title("Space Invader")
wn.tracer(0)

# comet
comet = turtle.Turtle()
comet.speed(0)
comet.color("brown")
comet.penup()
comet.goto(0, 250)
comet.shape("circle")
comet.shapesize(stretch_len=2, stretch_wid=2)
comet.dx = 0.4
stretch_size = 1.8

# fire
fire = turtle.Turtle()
fire.speed(0)
fire.color("orange")
fire.penup()
fire.goto(0, -235)
fire.shape("square")
fire.shapesize(stretch_len=0.3, stretch_wid=0.3)

# ship
ship = turtle.Turtle()
ship.speed(0)
ship.color("green")
ship.penup()
ship.goto(0, -235)
ship.shape("triangle")
ship.shapesize(stretch_len=2, stretch_wid=2)

# title
txt = turtle.Turtle()
txt.speed(0)
txt.color("red")
txt.penup()
txt.goto(0, -20)
txt.write("SPACE INVADER", align="center", font=("Courier", 50, "bold"))
txt.hideturtle()
time.sleep(0.6)

# border
txt.penup()
txt.goto(-400, -180)
txt.pendown()
txt.color("blue")
txt.forward(800)

# score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto(-290, 250)
score.color("yellow")
score.write("SCORE: 0/10", align="center", font=("Courier", 20, "bold"))
score_p = 0


# movement
def ship_right():
    x = ship.xcor()
    fx = fire.xcor()
    if x > 360 or fx > 360:
        ship.setx(x)
        fire.setx(fx)
    else:
        x += 20
        if fire.ycor() == -235:
            fx += 20
            fire.setx(fx)
        ship.setx(x)


def ship_left():
    x = ship.xcor()
    fx = fire.xcor()
    if x < -375 or fx < -375:
        ship.setx(x)
        fire.setx(fx)
    else:
        x -= 20
        if fire.ycor() == -235:
            fx -= 20
            fire.setx(fx)
        ship.setx(x)


firing = "no"


def make_fire():
    global firing
    if firing == "no":
        firing = "yes"


def shoot():
    global firing
    global score_p
    global stretch_size
    if firing == "yes":
        fire.sety(fire.ycor() + 7)
        if ((fire.ycor() > comet.ycor() - 20) and
                (comet.xcor() - 20 < fire.xcor() < comet.xcor() + 20)):
            comet.shapesize(stretch_len=stretch_size, stretch_wid=stretch_size)
            stretch_size -= 0.15
            fire.goto(ship.xcor(), ship.ycor())
            score_p += 1
            score.clear()
            score.write(f"SCORE: {score_p}/10", align="center", font=("Courier", 20, "bold"))
            firing = "no"
        if fire.ycor() > 300:
            firing = "no"
            fire.goto(ship.xcor(), ship.ycor())


# key function
wn.listen()
wn.onkeypress(ship_right, "Right")
wn.onkeypress(ship_left, "Left")
wn.onkeypress(make_fire, "Up")

# main loop
while True:
    wn.update()

    # comet movement
    comet.setx(comet.xcor() + comet.dx)
    if comet.xcor() > 360:
        comet.dx *= -1
        comet.sety(comet.ycor() - 40)
    if comet.xcor() < -370:
        comet.dx *= -1
        comet.sety(comet.ycor() - 40)
    if comet.ycor() <= -190 or score_p == 10:
        comet.sety(comet.xcor())
        comet.sety(comet.ycor())

        ship.hideturtle()
        comet.hideturtle()
        fire.hideturtle()

        txt.clear()
        txt.penup()
        txt.goto(0, -20)
        txt.color("orange")
        txt.pendown()
        if score_p == 10:
            txt.write("YOU WIN :)", align="center", font=("Courier", 50, "bold"))
        else:
            txt.write("GAME OVER!!", align="center", font=("Courier", 50, "bold"))

    shoot()
