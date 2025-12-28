import turtle

wn = turtle.Screen()
wn.bgcolor("cyan")
wn.title("pong")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(350, 0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(-350, 0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.shape("circle")
ball.color("black")
ball.dx = 0.3
ball.dy = 0.3

# score
player_a = 0
player_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(0, 220)
pen.hideturtle()
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "bold"))


# paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y > 240:
        paddle_a.sety(y)
    else:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y < -238:
        paddle_a.sety(y)
    else:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y > 240:
        paddle_b.sety(y)
    else:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y < -238:
        paddle_b.sety(y)
    else:
        y -= 20
        paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")
wn.onkeypress(paddle_b_up, "w")
wn.onkeypress(paddle_b_down, "s")
wn.onkeypress(paddle_b_up, "W")
wn.onkeypress(paddle_b_down, "S")

# main loop
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.dy *= -1

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b += 1
        pen.clear()
        pen.write(f"Player A: {player_a}   Player B: {player_b}", align="center", font=("Courier", 24, "bold"))

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a += 1
        pen.clear()
        pen.write(f"Player A: {player_a}   Player B: {player_b}", align="center", font=("Courier", 24, "bold"))

    if (ball.xcor() > 330 and ball.xcor() < 350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50:
        ball.setx(-330)
        ball.dx *= -1
