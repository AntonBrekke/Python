# Import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    if answers == 1:
        print("It is certain")

    if answers == 2:
        print ("Outlook good")

    if answers == 3:
        print("You may rely on it")

    if answers == 4:
        print ("Ask again later")

    if answers == 5:
        print("Concentrate and ask again")

    if answers == 6:
        print("Reply hazy, try again")

    if answers == 7:
        print ("My reply is no")

    if answers == 8:
        print ("My sources say no")
