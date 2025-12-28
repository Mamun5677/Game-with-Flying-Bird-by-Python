print("\nTHE FUN GAME\n")
name = input("what is your name: ")
age = int(input(f"Hi {name}, what is your age: "))
if age >= 18:
    print("\nyou are eligible to play the game")
    play = input("\nare you ready to play: ")
    if play.lower() == "yes":
        print("\nlet's play:)")
        river_cross = input("""\nSuppose..you left your home and going to a destined place by walk,
when you reach near a river you see a crocodile under the water
so how will you cross the river?
will you cross by swim or will you look for a boat to cross the river?
swim or boat: """)
        if river_cross.lower() == "boat":
             print("\nwise decision you have crossed the river:)\nyou could not cross by swimming because a crocodile was there")
             go = input("""\nthen you continue your walk and by end of the road you see a vehicle parked near a tree
so would you continue by walking or take the vehicle to go further
walk or vehicle: """)
             if go.lower() == "walk":
                 print("\ngood decision again because the road ends and you cannot go by the vehicle")
                 food = input("""\nand you continue your walk and you reached a forest
you get hungry and when you checked your pocket you see you have 100 rupees in it
so would you buy some food from a hotel or pick some fruits from trees
hotel or trees: """)
                 if food.lower() == "trees":
                     print("\ngood move because forest got no hotels:)")
                     money = input("""\nso you kept walking and you reached near the destination
but you see a payment gate and you have to pay 75 rupees them
do you have 75 rupees to pay?
yes or no: """)
                     if money.lower() == "yes":
                         print("\nyesss you have the money in your pocket and you successfully reached your destination\nyou win:)")
                     else:
                         print("\noops! you have money in your pocket you could have paid them\nyou lose the game!")
                 else:
                     print("\noops! forest got ho hotels you failed\ngame over!!")
             else:
                 print("\noops! you fail to go because the road ends and you can't take the vehicle!\ngame over!!")
        else:
            print("\noops! the crocodile ate you!! you are dead!!!\ngame over! ")
    else:
        print("\nok thank you:)\nbye!!!")
else:
    print("\nyou are under 18, you are not eligible to play the game!\nthank you:)")
