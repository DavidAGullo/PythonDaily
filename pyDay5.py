from random import randint, random


#Constants
characterSelect = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( )" #All Available Characters For Password
characterSelectArray = characterSelect.split(" ") # The Split Function

#Place Holders
password = ""
count = 0

#Main
inputVal = input("How many Characters for the password generation: ") #Input

while(count < int(inputVal)):
    number = randint(0, len(characterSelectArray))
#    print(count)
    password += characterSelectArray[number]
    count += 1

print(password) #Output

