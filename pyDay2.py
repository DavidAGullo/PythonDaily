# Program Created By David Gullo
# Tax Calculator, and how much if split
# Day 2 Assignment

print("Welcome to David's Tax Calculator")
billTotal = input("What is the Total bill? ")
split = input("How many people to split the bill? ")
tipPercent = input("What percentage tip would you like to give? 10, 12, 15, etc. ")

sol = (float(billTotal)/float(split))*(float(tipPercent)/100)
print("Tip should be: " + str(sol))