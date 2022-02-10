# Program Created By David Gullo
# Choose your own Adventure Game
# Day 3 Assignment

from operator import truediv
from time import sleep

###########################
# Collection Items        #
item_hammer = False
item_key = False
# Stats                   #
isDead = False
###########################

print("Welcome to Treasure Adventure")
print("You wake up in an old house, you don't see much outside from a Cupboard, and a Chest")
#print()
action1 = input("What do you check first? Cupboard or Chest? ")
if(action1 == str.lower("Cupboard")):
    #Add Key
    item_key = True
    print("You found a Key!")
else:
    #Add Hammer
    item_hammer = True
    print("You found a Hammer!")
print("Just as you put it away, a Whoosh knocks you to the ground. ")
print("A figure stands over you")
sleep(1)
print(".")
sleep(1)
print("The figure points to the door")
action2 = input("Run for the door? or Speak to the figure? Speak or Run? ")
if action2 == str.lower("Speak"):
    if item_hammer:
        print("He knocks you to the floor again, this time grabs the hammer out of your hands and proceeds to beat you with it.")
        print("Game Over")
        isDead = True
    else:
        print("He points to the door and you leave.")
else:
    print("You bolt out the door")
if not isDead:
    #Continues Story
    print("You run out the door")
    sleep(2)
    action3 = input("While running you see the path splits are you going to go left or right? ")
    if action3 == str.lower("left"):
        print("You curve left")
        sleep(3)
        print("You approach a town, with a motto on the sign")
        print("Motto reads: The True Adventure is the Friends you meet along the way")
    else:
        print("You run down the right path")
        sleep(3)
        print("You found a cave!")
        print("You enter it and see a chest")
        if item_key:
            print("You grab the key from your pocket and open it")
            sleep(2)
            print("Inside you find a note, the note reads...")
            print("The actual adventure is the friends you met along the way.")
        else:
            print("It is locked")
            print("The cave goes dark")
            print("The End")
else:
    #GAME OVER
    print("Retry next time")
