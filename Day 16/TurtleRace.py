from turtle import Turtle as T
from turtle import Screen
from random import randint
from random import choice


colors = ["red","orange","yellow","green","blue","indigo","violet"]
turtles = []
GameOver = False

for turt in colors:
    turt = T()
    turt.hideturtle()
    turtles.append(turt)

i = 0
y = -200
for obj in turtles:
    obj.showturtle()
    obj.shape("turtle")
    obj.color(colors[i])
    i += 1
    obj.penup()
    obj.setposition(x = -300, y = y)
    y += 50

def forward(obj):
    obj.forward(randint(0,11))


screen = Screen()
screen.setup(800,600)
user_bet = screen.textinput(title = "Place your Bet", prompt = "Which Turtle will win the race? Enter a color: ")
str(user_bet).lower

while not GameOver:
    
    runner = choice(turtles)
    if runner.xcor() >= 300:
        GameOver = True
        if str(runner.pencolor().lower()) == user_bet:
            print(f"You win! The winner in {runner.pencolor().title()}")
        else:
            print(f"You lose. The winner is {runner.pencolor().title()}")
    forward(runner)


screen.exitonclick()