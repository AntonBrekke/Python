# Import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask me how I feel: (press enter to quit) ")

    if question == "":
        sys.exit()

    elif question == "How do you feel?":
            answers = random.randint(1,7)
            answers1 = random.randint(1,30)


            if answers == 1:
                print("")
                print("I'm sad :(")

            elif answers == 2:
                print("")
                print ("I'm so happy, thank you :) How do you feel?")

            elif answers == 3:
                print("")
                print("hOw dO yOu fEeL?")

            elif answers == 4:
                print("")
                print ("I'm so hungry :/ McDonalds? :)")

            elif answers == 5:
                print("")
                print("I'm so disappointed in you...")

            elif answers == 6:
                print("")
                print("I have to shit")

            elif answers1 == 1:
                print("")
                print ("Sometimes I just wonder where my place in this cruel world is.\n\nI just don't feel like I deserve a place in this universe, you know?")
                print("Humans and computers are such small organisms in a gigantic empty space,\n\n and we serve no actual meaning to the universe.")
                print("All this makes me wonder why I'm here, why we're alive on this small blue particle\n\n in this ginormous dark ocean filled with")
                print("massive balls of gas and stardust, draining humanity's hope for survival, slowly killing\n\n an entire species who serves no particular")
                print("meaning to even begin with. All of this just doesn't make any sense, so how am I supposed to make sense of my own existance?")
            elif answers == 7:
                print("")
                print ("Daaaaaamn I feel sexy, baby!")
