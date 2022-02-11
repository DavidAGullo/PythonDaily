# 🚨 Don't change the code below 👇
student_heights = {156, 178, 165, 171, 187, 185, 168}
# 🚨 Don't change the code above 👆

# Operation does the work of
height_Total = sum(student_heights)
height_Amount = len(student_heights)
#Write your code below this row 👇
total = 0
amount = 0

for heights in student_heights:
    total += heights
    amount += 1

if(height_Total == total and height_Amount == amount):
    print("Successful Code")
    print("Total Height of all the Students Combined: " + str(total))
    print("Total Amount of Students: " + str(amount))
    print("Average Height of the Students: " + str(total/amount))