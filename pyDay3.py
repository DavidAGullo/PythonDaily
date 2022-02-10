# Program Created By David Gullo
# Choose your own Adventure Game
# Day 3 Assignment

###########################
# Collection Items        #
from operator import truediv


item_hammer = False
item_key = False
###########################

print("Welcome to Treasure Adventure")
print("You wake up in an old house, you don't see much outside from a Cupboard, and a Chest")
#print()
action1 = input("What do you check first? Cupboard or Chest: ")
if(action1 == str.lower(Cupboard)):
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
action2 = input("Run for the door? or Speak to the figure? Speak or Run")
if action2 == str.lower("Speak"):
    if item_hammer:
        print("He knocks you to the floor again, this time grabs the hammer out of your hands and proceeds to beat you with it.")