# Program Created By David Gullo
# Rock Paper Scissor (Mersenne Twister Randomizer Method)
# Day 4 Assignment

import random

print("Welcome to Rock Paper Scissors")
#Starting Input from user
user_input = input("Rock, Paper, or Scissors? ")
#Converting variable to lowercase now
user_input = str.lower(user_input)
#Generating a response from Program
rps = ["Rock", "Paper", "Scissors"] #Catagories
opp_input = random.randint(0,2) #Generates a number corelated with rps array
result = rps[opp_input]
print(result)

# The Logic
if(user_input == str.lower(result)):
    print("Draw")
elif(user_input == "rock"):
    if(str.lower(result) == "paper"):
        print("Paper covers Rock. \nYou Lose.")
    elif(str.lower(result) == "scissors"):
        print("Rock breaks Scissors. \nYou Win!")
elif(user_input == "paper"):
    if(str.lower(result) == "scissors"):
        print("Scissors cut through Paper. \nYou Lose.")
    elif(str.lower(result) == "rock"):
        print("Paper covers Rock. \nYou Win!")
elif(user_input == "scissors" or user_input == "scissor"): #A bit of user help...
    if(str.lower(result) == "rock"):
        print("Rock smashes Scissors. \nYou Lose.")
    elif(str.lower(result) == "paper"):
        print("Scissors cut Paper. \nYou Win!")