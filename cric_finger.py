import time
import random

print("\nCRIC FINGER\n")


def intro(say):
    time.sleep(0.1)
    print("\nTotal over: 2")
    time.sleep(0.1)
    print("Total wickets: 3")
    if say == "bat":
        time.sleep(0.1)
        print("\nLet's start the game!")
        time.sleep(0.1)
        print("Let's bat\n")
    else:
        time.sleep(0.1)
        print("\nLet's start the game!")
        time.sleep(0.1)
        print("Let's ball\n")


def bat(so, b):
    global score_bat
    global wicket_bat
    global ball_bat

    score_bat = 0
    wicket_bat = 0
    ball_bat = 0

    if so == "yes":
        print("\nSUPER OVER\n")
        time.sleep(0.1)
        print("Let's bat")
        while wicket_bat < 3 and ball_bat < 6:
            while True:
                you = int(input("you: "))
                if you > 6:
                    print("enter a number less than or equal to 6")
                if you <= 6:
                    break
            opponent = random.randint(1, 6)
            print("opponent: " + str(opponent))
            ball_bat += 1

            if you == opponent:
                print("\nout!\n")
                wicket_bat += 1
                print(f"score: {score_bat}/{wicket_bat}")
            else:
                score_bat += you

            if ball_bat == 6:
                print("\nover finished!")
                print(f"score: {score_bat}/{wicket_bat}")

            if b == "yes":
                if score_bat > score_ball:
                    break
    else:
        print("over 1")
        while wicket_bat < 3 and ball_bat < 12:
            while True:
               you = int(input("you: "))
               if you > 6:
                   print("enter a number less than or equal to 6")
               if you <= 6:
                   break
            opponent = random.randint(1, 6)
            print("opponent: " + str(opponent))
            ball_bat += 1

            if ball_bat == 6:
                print("\nover 2")
            if you == opponent:
                print("\nout!\n")
                wicket_bat += 1
                print(f"score: {score_bat}/{wicket_bat}")
            else:
                score_bat += you
            if b == "yes":
                if score_bat > score_ball:
                    break

    if wicket_bat == 3:
        print("\nall are out!")
    elif ball_bat == 12:
        print("\nover finished!")
        print(f"score: {score_bat}/{wicket_bat}")


def ball(so, b):
    global score_ball
    global wicket_ball
    global ball_ball

    score_ball = 0
    wicket_ball = 0
    ball_ball = 0

    if so == "yes":
        print("\nSUPER OVER\n")
        time.sleep(0.1)
        print("Let's ball")
        while wicket_ball < 3 and ball_ball < 6:
            while True:
                you = int(input("you: "))
                if you > 6:
                    print("enter a number less than or equal to 6")
                if you <= 6:
                    break
            opponent = random.randint(1, 6)
            print("opponent: " + str(opponent))
            ball_ball += 1

            if you == opponent:
                print("\nout!\n")
                wicket_ball += 1
                print(f"score: {score_ball}/{wicket_ball}")
            else:
                score_ball += opponent

            if ball_ball == 6:
                print("\nover finished!")
                print(f"score: {score_ball}/{wicket_ball}")

            if b == "yes":
                if score_ball > score_bat:
                    break
    else:
        print("over 1")
        while wicket_ball < 3 and ball_ball < 12:
            while True:
                you = int(input("you: "))
                if you > 6:
                    print("enter a number less than or equal to 6")
                if you <= 6:
                    break
            opponent = random.randint(1, 6)
            print("opponent: " + str(opponent))
            ball_ball += 1

            if ball_ball == 6:
                print("\nover 2")

            if you == opponent:
                print("\nout!\n")
                wicket_ball += 1
                print(f"score: {score_ball}/{wicket_ball}")
            else:
                score_ball += opponent

            if b == "yes":
                if score_ball > score_bat:
                    break

    if wicket_ball == 3:
        print("\nall are out!")
    elif ball_ball == 12:
        print("\nover finished!")
        print(f"score: {score_ball}/{wicket_ball}")


time.sleep(0.1)
print("Toss the coin to choose!")
time.sleep(0.1)
coin = input("Heads or Tails: ")
toss = random.choice(["Heads", "Tails"])
time.sleep(0.1)
print("Coin tossed: " + toss)

if coin.lower() == toss.lower():
    time.sleep(0.2)
    print("\nyou won the toss!")
    time.sleep(0.1)
    choose = input("Bat or Ball: ")

    if choose.lower() == "bat":
        intro("bat")
        bat("no", "no")
        time.sleep(0.1)
        print(f"\nopponent need {score_bat + 1} runs to win!\n")
        time.sleep(0.1)
        print("Lets ball\n")
        time.sleep(0.1)
        ball("no", "yes")

        if score_bat == score_ball:
            time.sleep(0.1)
            print("\nmatch tied!")
            time.sleep(0.1)
            ball("yes", "no")
            time.sleep(0.1)
            print(f"\nyou need {score_ball + 1} runs to win!\n")
            time.sleep(0.1)
            bat("yes", "yes")

        if score_bat > score_ball:
            win_score = score_bat - score_ball
            time.sleep(0.1)
            print(f"\nyou won for {win_score} runs")
        elif score_ball > score_bat:
            win_score = score_ball - score_bat
            time.sleep(0.1)
            print(f"\nopponent won for {win_score} runs!")
    elif choose.lower() == "ball":
        time.sleep(0.1)
        intro("ball")
        time.sleep(0.1)
        ball("no", "no")
        time.sleep(0.1)
        print(f"\nyou need {score_ball + 1} runs to win!\n")
        time.sleep(0.1)
        print("Lets bat\n")
        time.sleep(0.1)
        bat("no", "yes")

        if score_bat == score_ball:
            time.sleep(0.1)
            print("\nmatch tied!")
            time.sleep(0.1)
            bat("yes", "no")
            time.sleep(0.1)
            print(f"\nopponent need {score_bat + 1} runs to win!\n")
            time.sleep(0.1)
            ball("yes", "yes")

        if score_ball > score_bat:
            win_score = score_ball - score_bat
            time.sleep(0.1)
            print(f"\nopponent won for {win_score} runs")
            time.sleep(0.1)
        elif score_ball < score_bat:
            win_score = score_bat - score_ball
            time.sleep(0.1)
            print(f"\nyou won for {win_score} runs!")
else:
    time.sleep(0.1)
    print("\nopponent won the toss!")
    choose = random.choice(["bat", "ball"])
    time.sleep(0.1)
    print("opponent chose to " + choose + "!")

    if choose == "bat":
        time.sleep(0.1)
        intro("ball")
        time.sleep(0.1)
        ball("no", "no")
        time.sleep(0.1)
        print(f"\nyou need {score_ball + 1} runs to win!\n")
        time.sleep(0.1)
        print("Lets bat\n")
        time.sleep(0.1)
        bat("no", "yes")

        if score_bat == score_ball:
            time.sleep(0.1)
            print("\nmatch tied!")
            time.sleep(0.1)
            bat("yes", "no")
            time.sleep(0.1)
            print(f"\nopponent need {score_bat + 1} runs to win!\n")
            time.sleep(0.1)
            ball("yes", "yes")

        if score_ball > score_bat:
            win_score = score_ball - score_bat
            time.sleep(0.1)
            print(f"\nopponent won for {win_score} runs")
            time.sleep(0.1)
        elif score_ball < score_bat:
            win_score = score_bat - score_ball
            time.sleep(0.1)
            print(f"\nyou won for {win_score} runs!")
    else:
        time.sleep(0.1)
        intro("bat")
        time.sleep(0.1)
        bat("no", "no")
        time.sleep(0.1)
        print(f"\nopponent need {score_bat + 1} runs to win!\n")
        time.sleep(0.1)
        print("Lets ball\n")
        time.sleep(0.1)
        ball("no", "yes")

        if score_bat == score_ball:
            time.sleep(0.1)
            print("\nmatch tied!")
            time.sleep(0.1)
            ball("yes", "no")
            time.sleep(0.1)
            print(f"\nyou need {score_ball + 1} runs to win!\n")
            time.sleep(0.1)
            bat("yes", "yes")

        if score_bat > score_ball:
            win_score = score_bat - score_ball
            time.sleep(0.1)
            print(f"\nyou won for {win_score} runs")
        elif score_ball > score_bat:
            win_score = score_ball - score_bat
            time.sleep(0.1)
            print(f"\nopponent won for {win_score} runs!")
