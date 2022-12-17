import random
import os

os.system("clear")

def dealCards(whoseCards, deck):
    # deal cards from list

    whoseCards.append(random.choice(deck))
    whoseCards.append(random.choice(deck))


def hit(whoseCards, deck):
    whoseCards.append(random.choice(deck))
    print(f"Player was dealt a {whoseCards[-1]}")


print("Welcome to Blackjack!")


def run():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    playerCards = []
    compCards = []
    sel = input(
        "Would you like to play a game of Blackjack? Enter 'y' for yes and 'n' for no: ").lower()
    print("\n")
    if sel == "n":
        return
    else:
        playerCards = []
        compCards = []
        dealCards(playerCards, deck)
        dealCards(compCards, deck)
    while sum(playerCards) <= 21:
        print(f"The Dealer's visible card is {compCards[0]}.")
        print(f"Your cards are {playerCards}. Sum is {sum(playerCards)}. Would you like to Stay or Hit?")
        action = input("Enter 's' for Stay and 'h' for Hit: ").lower()
        print("\n")

        if action == "h":
            hit(playerCards, deck)
            if sum(playerCards) > 21 and 11 in playerCards:
                
                for i in range(len(playerCards)):
                    if playerCards[i] == 11:
                        playerCards[i] -= 10
                        print("Aces can be 1")
                        break

                print(playerCards)
            elif sum(playerCards) > 21:
                print(playerCards)
                print("You've bust! Dealer Wins!")
                run()
            elif sum(playerCards) == 21:
                print(playerCards)
                print("Blackjack! You win!")
                run()

        if action == "s":
            print(f"Your cards are {playerCards}.")
            print(f"The dealer's cards are {compCards}.")
            while sum(compCards) <= 17:
                hit(compCards, deck)
            if sum(compCards) > 21 and 11 in compCards:
                for i in range(len(compCards)):
                    if compCards[i] == 11:
                        compCards[i] -= 10
                        print("Aces can be 1")
                print(f"The dealer hits. {compCards}")
            if sum(compCards) > 21:
                print(compCards)
                print("The dealer's bust! You win!")
                run()
            elif sum(compCards) == 21:
                print("Dealer hit Blackjack! You lose!")
                run()
            else:
                if sum(compCards) > sum(playerCards):
                    print("Dealer wins!")
                    run()
                elif sum(compCards) == sum(playerCards):
                    print("It's a tie.")
                    run()
                else:
                    print("You win!")
                    run()


run()
