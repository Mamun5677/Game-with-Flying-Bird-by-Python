import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("cyan")
wn.setup(height=500, width=500)
wn.title("Snake Game")
wn.tracer(0)

title = turtle.Turtle()
title.penup()
title.color("brown")
title.goto(0, 50)
title.write("Snake Game", align="center", font=("Courier", 40, "bold"))
title.hideturtle()

title.goto(0, -10)
title.color("red")
title.write("choose mode", align="center", font=("Courier", 20, "normal"))

title.goto(-80, -40)
title.pendown()
title.pencolor("black")
title.fd(70)
title.left(90)
title.fd(20)
title.left(90)
title.fd(70)
title.left(90)
title.fd(20)

title.penup()
title.goto(20, -40)
title.pendown()
title.pencolor("black")
title.left(90)
title.fd(70)
title.left(90)
title.fd(20)
title.left(90)
title.fd(70)
title.left(90)
title.fd(20)

title.penup()
title.goto(-72, -38)
title.write("classic", font=("Courier", 10, "normal"))

title.penup()
title.goto(33, -38)
title.write("modern", font=("Courier", 10, "normal"))


def game(mode):
    # snake
    snake = turtle.Turtle()
    snake.speed(0)
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.direction = "null"

    # body
    segments = []

    # food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("square")
    if mode == "m": food.color("green")
    else: food.color("red")
    food.penup()
    food.goto(0, 100)

    barriers = []
    if mode == "m":
        # barriers
        barr1 = turtle.Turtle()
        barr1.speed(0)
        barr1.shape("square")
        barr1.shapesize(stretch_len=5)
        barr1.color("brown")
        barr1.penup()
        barr1.goto(-120, 125)
        barriers.append(barr1)

        barr2 = turtle.Turtle()
        barr2.speed(0)
        barr2.shape("square")
        barr2.shapesize(stretch_len=5)
        barr2.color("brown")
        barr2.penup()
        barr2.goto(120, -125)
        barriers.append(barr2)

        # borders
        border1 = turtle.Turtle()
        border1.speed(0)
        border1.shape("square")
        border1.penup()
        border1.goto(-240, -40)
        border1.shapesize(stretch_wid=30, stretch_len=1)
        border1.color("brown")

        border2 = turtle.Turtle()
        border2.speed(0)
        border2.shape("square")
        border2.penup()
        border2.goto(230, 40)
        border2.shapesize(stretch_wid=30, stretch_len=1)
        border2.color("brown")

        border3 = turtle.Turtle()
        border3.speed(0)
        border3.shape("square")
        border3.penup()
        border3.goto(-40, -230)
        border3.shapesize(stretch_wid=1, stretch_len=30)
        border3.color("brown")

        border4 = turtle.Turtle()
        border4.speed(0)
        border4.shape("square")
        border4.penup()
        border4.goto(40, 240)
        border4.shapesize(stretch_wid=1, stretch_len=30)
        border4.color("brown")

    # score
    score = turtle.Turtle()
    score.speed(0)
    score.color("black")
    score.penup()
    score.goto(0, 200)
    score.write("SCORE:0  HIGH SCORE:0 ", align="center", font=("Courier", 15, "italic"))
    score.hideturtle()
    scores = 0
    high_score = 0

    delay = 0.1

    # movement
    def up():
        if snake.direction != "down":
            snake.direction = "up"

    def down():
        if snake.direction != "up":
            snake.direction = "down"

    def right():
        if snake.direction != "left":
            snake.direction = "right"

    def left():
        if snake.direction != "right":
            snake.direction = "left"

    # key function
    wn.listen()
    wn.onkeypress(up, "Up")
    wn.onkeypress(down, "Down")
    wn.onkeypress(right, "Right")
    wn.onkeypress(left, "Left")

    def move():
        if snake.direction == "up":
            snake.sety(snake.ycor() + 20)
        if snake.direction == "down":
            snake.sety(snake.ycor() - 20)
        if snake.direction == "right":
            snake.setx(snake.xcor() + 20)
        if snake.direction == "left":
            snake.setx(snake.xcor() - 20)
    if mode == "m":
        while True:
            wn.update()

            # collision with food
            if snake.distance(food) < 20:
                while True:
                    x = random.randint(-210, 210)
                    y = random.randint(-210, 210)
                    if not (((x < -40 and x > -200) and (y < 145 and y > 105)) or (
                            (x > 40 and x < 200) and (y > -145 and y < -105))):
                        if x % 20 == 0 and y % 20 == 0:
                            break

                food.goto(x, y)
                scores += 10
                if scores > high_score:
                    high_score = scores

                score.clear()
                score.write(f"SCORE:{scores}  HIGH SCORE:{high_score} ", align="center", font=("Courier", 15, "italic"))

                # add new segment to snake
                new_seg = turtle.Turtle()
                new_seg.speed(0)
                new_seg.shape("square")
                new_seg.color("black")
                new_seg.penup()
                segments.append(new_seg)
                delay -= 0.001

            # move  the segments in reverse order
            for i in range(len(segments) - 1, 0, -1):
                x = segments[i - 1].xcor()
                y = segments[i - 1].ycor()
                segments[i].goto(x, y)

            # move segment 0 to head
            if len(segments) > 0:
                x = snake.xcor()
                y = snake.ycor()
                segments[0].goto(x, y)

            # Collision with border
            if snake.xcor() >= 210 or snake.xcor() <= -210 or snake.ycor() >= 210 or snake.ycor() <= -210:
                snake.direction = "null"
                time.sleep(1)
                snake.goto(0, 0)
                food.goto(0, 100)
                delay = 0.1

                for i in segments:
                    i.goto(1000, 1000)
                segments.clear()

                scores = 0
                score.clear()
                score.write(f"SCORE:{scores}  HIGH SCORE:{high_score} ", align="center", font=("Courier", 15, "italic"))

            # collision with barriers
            for i in barriers:
                if (snake.xcor() < i.xcor() + 80 and snake.xcor() > i.xcor() - 80) and (
                        snake.ycor() > i.ycor() - 20 and snake.ycor() < i.ycor() + 20):
                    snake.direction = "null"
                    time.sleep(1)
                    snake.goto(0, 0)
                    food.goto(0, 100)
                    delay = 0.1

                    for j in segments:
                        j.goto(1000, 1000)
                    segments.clear()

                    scores = 0
                    score.clear()
                    score.write(f"SCORE:{scores}  HIGH SCORE:{high_score} ", align="center", font=("Courier", 15, "italic"))

            move()

            # collision with body
            for i in segments:
                if i.distance(snake) < 20:
                    snake.direction = "null"
                    time.sleep(1)
                    snake.goto(0, 0)
                    food.goto(0, 100)
                    delay = 0.1

                    for j in segments:
                        j.goto(1000, 1000)
                    segments.clear()

                    scores = 0
                    score.clear()
                    score.write(f"SCORE:{scores}  HIGH SCORE:{high_score} ", align="center", font=("Courier", 15, "italic"))

            time.sleep(delay)

    else:
        while True:
            wn.update()

            # collision with food
            if snake.distance(food) < 20:
                while True:
                    x = random.randint(-230, 230)
                    y = random.randint(-230, 230)
                    if x % 20 == 0 and y % 20 == 0:
                        break
                food.goto(x, y)
                scores += 10
                if scores > high_score:
                    high_score = scores

                score.clear()
                score.write(f"SCORE:{scores}  HIGH SCORE:{high_score} ", align="center", font=("Courier", 15, "italic"))

                # add new segment to snake
                new_seg = turtle.Turtle()
                new_seg.speed(0)
                new_seg.shape("square")
                new_seg.color("black")
                new_seg.penup()
                segments.append(new_seg)
                delay -= 0.001

            # move the segments in reverse order
            for i in range(len(segments) - 1, 0, -1):
                x = segments[i - 1].xcor()
                y = segments[i - 1].ycor()
                segments[i].goto(x, y)

            # move segment 0 to head
            if len(segments) > 0:
                x = snake.xcor()
                y = snake.ycor()
                segments[0].goto(x, y)

            # Collision with border
            if snake.xcor() > 250 or snake.xcor() < -250:
                snake.goto(-snake.xcor(), snake.ycor())
            if snake.ycor() > 250 or snake.ycor() < -250:
                snake.goto(snake.xcor(), -snake.ycor())

            move()

            # collision with body
            for i in segments:
                if i.distance(snake) < 20:
                    snake.direction = "null"
                    time.sleep(1)
                    snake.goto(0, 0)
                    food.goto(0, 100)
                    delay = 0.1

                    for j in segments:
                        j.goto(1000, 1000)
                    segments.clear()

                    scores = 0
                    score.clear()
                    score.write(f"SCORE:{scores}  HIGH SCORE:{high_score} ", align="center",
                                font=("Courier", 15, "italic"))

            time.sleep(delay)


def click(x, y):
    if (x > -80 and x < -10) and (y < -20 and y > -40):
        title.clear()
        game("")

    if (x > 20 and x < 90) and (y < -20 and y > -40):
        title.clear()
        game("m")


wn.listen()
wn.onclick(click, 1)
while True:
    wn.update()
