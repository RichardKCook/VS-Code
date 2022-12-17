from contextlib import nullcontext
import os
bidders = {}
print("Welcome to the Blind Auction!")


def run():

    name = input("What is your name?\n")
    bid = int(input("How much would you like to bid?\n$"))

    bidders[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if others == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')

        run()
    elif others == "no":

        os.system('cls' if os.name == 'nt' else 'clear')
        highest_number = 0
        winner = ""
        for name in bidders:

            if bidders[name] > highest_number:
                highest_number = bidders[name]
                winner1 = name
            elif bidders[name] == highest_number:
                winner2 = name
        if winner2 == "":
            print(
            f"The winning bidder is {winner1} with their bid of ${highest_number}"
            )
        elif winner2 != "":
            print(
                f"We have a tie between {winner1} and {winner2} with bids of ${highest_number}"
            )

run()
