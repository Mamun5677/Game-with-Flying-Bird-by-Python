print("GUESSING GAME\n")

sw = "mom"
print("~HINT: Only 3 letters\n One who gave you birth")
print("\nYou only get 3 chances\n")
limit = 0
while limit < 3:
    a = input("Enter the secret word: ")
    if a != sw:
        print("wrong guess")
        limit += 1
    elif a == sw:
        print("wooh:) wright guess")
        break
if limit == 3:
    print("oops! out of chances")
