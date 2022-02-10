# Program Created By David Gullo
# Heads or Tails
# Day 4 Excercise

import random
from time import sleep

# random.randrange(stop)
# random.randrange(start, stop[, step])
# random.randint(a, b)
#
# https://docs.python.org/3/library/random.html


print("Welcome to Head's or Tail's")
sleep(5)
opp_Results = random.randint(0,100)
#print(opp_Results) #test
if opp_Results >= 50:
    print("Heads")
else:
    print("Tails")

