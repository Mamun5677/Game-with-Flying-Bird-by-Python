import random
print("\nROCK PAPER SCISSOR\n")
scoreu = 0
scorec = 0

for i in range(3):
    z = ["rock", "paper", "scissor"]
    a = input("Enter the choice: ")
    b = random.choice(z)
    print("computer: " + b)

    if a == "rock":
        if b == "paper":
            scorec += 1
        elif b == "scissor":
            scoreu += 1
    elif a == "paper":
        if b == "rock":
            scoreu += 1
        elif b == "scissor":
            scorec += 1
    elif a == "scissor":
        if b == "paper":
            scoreu += 1
        elif b == "rock":
            scorec += 1
    if i < 2:
        print(f"""
you:{scoreu}
computer:{scorec}\n""")

print("\nTOTAL SCORE")
print("you: " + str(scoreu))
print("computer: " + str(scorec))

if scorec > scoreu:
    print("\nYou lose!!")
elif scoreu == scorec:
    print("\nMatch tied!")
else:
    print("\nYou win:)\n")



