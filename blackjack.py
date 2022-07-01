import random as rand
import sys

dealer = 0
player = 0
n = 0

print("")
print("|Player:|Dealer:|")
print(f"|   {player}\t|  {dealer}\t|")
while n == 0:
    a = input("Press 0 to hit and 1 to hold(exit):")
    # Hit
    if a == 'exit':
        sys.exit()
    elif a == '0':
        card = rand.randint(2,14)
        cardD = rand.randint(2,14)
        if card >= 11 and card <= 13:
            card = 10
        elif card == 14:
            k = 0
            while k == 0:
                ace = input("You drew an ace! Choose it to be 1 or 11:")
                if ace == '1':
                    ace = int(ace)
                    card = ace
                    k = 1
                elif ace == '11':
                    ace = int(ace)
                    card = ace
                    k = 1
        if cardD >= 11 and cardD <= 13:
            cardD = 10
        elif cardD == 14:
            M = rand.randint(1,2)
            if M == 1:
                cardD = 1
            elif M == 2:
                cardD = 11
        player += card
        if dealer < 17:
            dealer += cardD

    # Hold
    elif a == '1':
        if dealer >= player and dealer <= 21 and dealer >=17:
            b = 0
            while b == 0:
                print("|Player:|Dealer:|")
                print(f"|   {player}\t|  {dealer}\t|")
                play = input("Aw, busted! Do you want to play again?\n('Enter' for yes, '.' for no:)")
                if play == '':      # Yes
                    b = 1
                    player = 0
                    dealer = 0
                elif play == '.':   # No
                    sys.exit()
        elif dealer < 17:
            cardD = rand.randint(2,14)
            if cardD >= 11 and cardD <= 13:
                cardD = 10
            elif cardD == 14:
                M = rand.randint(1,2)
                if M == 1:
                    cardD = 1
                elif M == 2:
                    cardD = 11
            dealer += cardD
        elif player > dealer and dealer >= 17 and dealer <=21 and player >= 17 and player <= 21:
            cardD = rand.randint(2,14)
            if cardD >= 11 and cardD <= 13:
                cardD = 10
            elif cardD == 14:
                M = rand.randint(1,2)
                if M == 1:
                    cardD = 1
                elif M == 2:
                    cardD = 11
            dealer += cardD


    # Checking scores:
    if dealer == 21:
        b = 0
        while b == 0:
            print("|Player:|Dealer:|")
            print(f"|   {player}\t|  {dealer}\t|")
            play = input("Aw, busted! Do you want to play again?\n('Enter' for yes, '.' for no:")
            if play == '':      # Yes
                b = 1
                player = 0
                dealer = 0
            elif play == '.':   # No
                sys.exit()

    elif player == 21:
        b = 0
        while b == 0:
            print("|Player:|Dealer:|")
            print(f"|   {player}\t|  {dealer}\t|")
            play = input("You won! Do you want to play again?\n('Enter' for yes, '.' for no:")
            if play == '':      # Yes
                b = 1
                player = 0
                dealer = 0
            elif play == '.':   # No
                sys.exit()


    if player < 21 and dealer > 21:
        l = 0
        while l == 0:
            print("|Player:|Dealer:|")
            print(f"|   {player}\t|  {dealer}\t|")
            play = input("You won! Do you want to play again?\n('Enter' for yes, '.' for no:")
            if play == '':      # Yes
                l = 1
                player = 0
                dealer = 0
            elif play == '.':   # No
                sys.exit()

    elif dealer > 21 and player > 21:
        b = 0
        while b == 0:
            print("|Player:|Dealer:|")
            print(f"|   {player}\t|  {dealer}\t|")
            play = input("Aw, busted! Do you want to play again?\n('Enter' for yes, '.' for no:")
            if play == '':      # Yes
                b = 1
                player = 0
                dealer = 0
            elif play == '.':   # No
                sys.exit()

    elif dealer < 21 and player > 21:
        b = 0
        while b == 0:
            print("|Player:|Dealer:|")
            print(f"|   {player}\t|  {dealer}\t|")
            play = input("Aw, busted! Do you want to play again?\n('Enter' for yes, '.' for no:")
            if play == '':      # Yes
                b = 1
                player = 0
                dealer = 0
            elif play == '.':   # No
                sys.exit()

    print("|Player:|Dealer:|")
    print(f"|   {player}\t|  {dealer}\t|")
