import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

selection = [rock, paper, scissors]

human = int(input("Which would you like to choose? Enter 1 for Rock, 2 for Paper, or 3 for Scissors\n"))-1

if human >= 3 or human < 0:
    print("You didn't enter a valid selection!")
else:

    comp = random.randint(0,2)

    hum_choice = selection[human]
    comp_choice = selection[comp]

    print(hum_choice)
    print("Computer Chose:\n" + comp_choice)

    if human == 0 and comp == 2 or human == 1 and comp == 0 or human == 2 and comp == 1:
        print("You win! :)")
    elif human == 0 and comp == 1 or human == 1 and comp == 2 or human == 2 and comp == 0:
        print("You lose :(")
    elif human == comp:
        print("It's a tie :|")