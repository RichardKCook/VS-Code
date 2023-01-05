import turtle
from check_answer import Check_Answer as CA
import print_name

screen = turtle.Screen()
screen.title("US States Game")

image = "/Users/Cook/Documents/VS Code/Day 20/50 States Game/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

check_answer = CA()

GAME_OVER = False
NUM = 0
GUESSES = []
while not GAME_OVER:
    is_right = False
    
    guess = str(screen.textinput(title=f"{NUM}/50 States Correct", prompt= "Type in the name of US State")).title()
    
    is_right = check_answer.is_right(guess)

    if is_right == True and guess not in GUESSES:

        GUESSES.append(guess)
        NUM += 1

    if len(GUESSES) == 50:
        
        print("You win!")
        GAME_OVER = True
    

turtle.exitonclick()