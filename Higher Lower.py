from art import logo, vs
from game_data import data
import random
import os


def choose_person():
    return random.choice(data)


def get_data(person):
    name = person["name"]
    desc = person["description"]
    country = person["country"]
    return f"{name}, the {desc}, from {country}"


def get_followers(person):
    return person["follower_count"]


def get_answer(A, B):
    if A > B:
        return "A"
    else:
        return "B"


def run():
    score = 0
    game_over = False
    person_A = choose_person()
    while not game_over:

        os.system("clear")
        print(logo)

        if score != 0:
            print(f"You're right! Current score: {score}")

        person_B = choose_person()

        while person_A == person_B:
            person_B = choose_person()

        follower_count_A = get_followers(person_A)
        follower_count_B = get_followers(person_B)

        print(f"Compare A: {get_data(person_A)}.\n\n")

        print(vs, "\n\n")

        print(f"Against B: {get_data(person_B)}\n")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        answer = get_answer(follower_count_A, follower_count_B)

        if guess == answer:
            score += 1
            person_A = person_B

        else:
            print(f"you lose, your score was {score}")
            game_over = True


run()
