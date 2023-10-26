# Black Jack Game in Python

import random
import time
#include the time module to make the game more suspensful and slower paced so that it is easier to read along while the program is running/executing.
cards = {'2':" dealt a Two",
         '3':" dealt a Three",
         '4':" dealt a Four",
         '5':" dealt a Five",
         '6':" dealt a Six",
         '7':" dealt a Seven",
         '8':" dealt an Eight",
         '9':" dealt a Nine",
         '10':" dealt a Ten",
         '11':" dealt a Queen",
         '12':" dealt a King",
         '13':" dealt a Jack",
         '14':" dealt an Ace"}

money = 100
wager = 0
yn = "Y"

def getWager():
    print()
    time.sleep(2)
    wager = int(input("Enter a wager: $"))
    if wager > 0 and wager <= money:
        time.sleep(2)
        print("Your wager is: $" + str(wager) + "\n")
    else:
        time.sleep(2)
        print("That is not an acceptable wager.")
        getWager()
    return wager


def rand():
    return random.randint(2, 14)

print("WELCOME TO BLACKJACK")
print("You have $" + str(money))

while yn != "N":
    playerTotal = 0
    houseTotal = 0
    playerCard = None
    houseCard1 = None
    houseCard2 = None
    choice = None
    num = None
    j = 0
    x = 0

    while True:

        wager = getWager()
        money = money - wager
        time.sleep(1)
        for i in range(0, 2):

            playerCard = rand()
            if playerCard == 10 or playerCard == 11 or playerCard == 12 or playerCard == 13:
                playerTotal += 10
                time.sleep(2)
                print("You are" + cards[str(playerCard)])
                time.sleep(2)
            elif playerCard == 14:
                time.sleep(2)
                print("You are" + cards[str(playerCard)])
                time.sleep(2)
                num = int(input("Would you like your Ace to be a 1 or an 11?: "))
                time.sleep(2)
                if num == 11:
                    playerTotal += 11
                else:
                    playerTotal += 1
            else:
                playerTotal += playerCard
                time.sleep(2)
                print("You are" + cards[str(playerCard)])
                time.sleep(2)

            if (j == 1):
                time.sleep(2)
                houseCard2 = rand()
                if houseCard2 == 10 or houseCard2 == 11 or houseCard2 == 12 or houseCard2 == 13:

                    houseTotal += 10
                    houseCard2 = 10

                elif houseCard2 == 14:
                    if houseTotal + 11 == 21:
                        houseTotal += 11
                        houseCard2 = 11
                    elif houseTotal + 1 == 21:
                        houseTotal += 1
                        houseCard2 = 1
                    elif houseTotal < 10:
                        houseTotal += 11
                        houseCard2 = 11
                    else:
                        houseTotal += 1
                        houseCard2 = 1


                else:
                    houseTotal += houseCard2

                print("House is dealt a Hole Card")
                time.sleep(2)
                print("\n  Player Point Total: " + str(playerTotal))
                print("  House Point Total: " + str(houseCard1) + "+")
                break

            houseCard1 = rand()#BUG FOUND! Problem: When printing the first card dealt to the house,
            #if houseCard1 == 10, 11, 12, or 13, then that number would be stored in the variable houseCard1. Because of that,
            #when I printed the value of houseCard1, I getting the value of 10, 11, 12, or 13, and I need only 10 to be shown.
            #Solution: Set houseCard1 == 10 withing the if-statement and set houseCard1 == 11 for the ACE.
            if houseCard1 == 10 or houseCard1 == 11 or houseCard1 == 12 or houseCard1 == 13:
                time.sleep(2)
                print("House is" + cards[str(houseCard1)])
                time.sleep(2)
                houseTotal += 10
                houseCard1 = 10

            elif houseCard1 == 14:
                time.sleep(2)
                print("House is" + cards[str(houseCard1)])
                time.sleep(2)
                if houseTotal + 11 == 21:
                    houseTotal += 11
                    houseCard1 = 11
                elif houseTotal + 1 == 21:
                    houseTotal += 1
                    houseCard1 = 1
                elif houseTotal < 10:
                    houseTotal += 11
                    houseCard1 = 11
                else:
                    houseTotal += 1
                    houseCard1 = 1

            else:
                houseTotal += houseCard1
                time.sleep(2)
                print("House is" + cards[str(houseCard1)])
                time.sleep(2)

            print("\n  Player Point Total: " + str(playerTotal))
            print("  House Point Total: " + str(houseTotal) + "\n")

            j += 1

        if playerTotal == 21:
            time.sleep(2)
            print("\nThe Player was Dealt a Natural Blackjack.")
            time.sleep(2)
            print("The Winnings are 1.5x the Wager\n")
            time.sleep(2)
            money = money + wager + (wager * 1.5)
            print("  You Won: $" + str(wager * 1.5))
            print("  Total Money: $" + str(money))
            break
        print()
        time.sleep(2)
        choice = input("Hit or Stand? (H/S): ").upper()

        while choice == "H":
            print()
            playerCard = rand()
            if playerCard == 10 or playerCard == 11 or playerCard == 12 or playerCard == 13:
                playerTotal += 10
                time.sleep(2)
                print("You are" + cards[str(playerCard)])
                time.sleep(2)
                print("\n  Player Point Total: " + str(playerTotal))
                print("  House Point Total: " + str(houseCard1) + "+")
            elif playerCard == 14:
                time.sleep(2)
                print("You are" + cards[str(playerCard)])
                time.sleep(2)
                num = int(input("Would you like your Ace to be a 1 or an 11?: "))
                if num == 11:
                    playerTotal += 11
                else:
                    playerTotal += 1
                time.sleep(2)
                print("\n  Player Point Total: " + str(playerTotal))
                print("  House Point Total: " + str(houseCard1) + "+")
            else:
                playerTotal += playerCard
                time.sleep(2)
                print("You are" + cards[str(playerCard)])
                time.sleep(2)
                print("\n  Player Point Total: " + str(playerTotal))
                print("  House Point Total: " + str(houseCard1) + "+")

            if playerTotal == 21:
                money = money + (wager * 2)
                time.sleep(2)
                print("\nBlack Jack!\n")
                time.sleep(2)
                print("  You Won: $" + str(wager))
                print("  Total Money: $" + str(money))
                x = 1
                break

            elif playerTotal > 21:
                time.sleep(2)
                print("\nBust!\n")
                time.sleep(2)
                print("  Lost Wager: $" + str(wager))
                print("  Total Money: $" + str(money))
                x = 1
                break

            print()
            time.sleep(2)
            choice = input("Hit or Stand? (H/S): ").upper()
            time.sleep(2)

        if x == 1:
            break
        time.sleep(2)
        print("\nHouse Flips Hole Card Over.\n")
        time.sleep(2)
        print("  Player Point Total: " + str(playerTotal))
        print("  House Point Total: " + str(houseTotal))

        while houseTotal < 17:

            houseCard1 = rand()
            houseTotal += houseCard1
            time.sleep(2)
            print("\nHouse is" + cards[str(houseCard1)])
            time.sleep(2)
            print("\n  Player Point Total: " + str(playerTotal))
            print("  House Point Total: " + str(houseTotal))

            if houseTotal == 21:
                time.sleep(2)
                print("\nHouse Wins!\n")
                time.sleep(2)
                print("  Lost Wager: $" + str(wager))
                print("  Total Money: $" + str(money))
                x = 1
                break
            elif houseTotal > 21:
                time.sleep(2)
                print("\nHouse Busts!")
                time.sleep(2)
                print("You Win!\n")
                time.sleep(2)
                money = money + (wager * 2)
                print("  You Won: $" + str(wager))
                print("  Total Money: $" + str(money))
                x = 1
                break

        if x == 1:
            break

        if playerTotal == houseTotal:
            time.sleep(2)
            print("\nStand Off!\n")
            time.sleep(2)
            money = money + wager
            print("  Total Money: $" + str(money))
            break

        if playerTotal > houseTotal:
            time.sleep(2)
            print("\nYou Win!\n")
            time.sleep(2)
            money = money + (wager * 2)
            print("  You Won: $" + str(wager))
            print("  Total Money: $" + str(money))
            break
        else:
            time.sleep(2)
            print("\nHouse Wins!\n")
            time.sleep(2)
            print("  Lost Wager: $" + str(wager))
            print("  Total Money: $" + str(money))
            break

    if money == 0:
        time.sleep(2)
        print("\nSorry, you are out of money.")
        time.sleep(2)
        print("Come again some other time!")
        break

    print()
    yn = input("Play Again? (Y/N): ").upper()