from turtle import Turtle as T
from turtle import Screen
from turtle import colormode
from random import choice
from random import randint

def colors():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b


used_colors=[]


tim = T()
colormode(255)
tim.shape("turtle")
tim.color("green")
tim.pensize(15)
for i in range(3,10):
    color = choice(colors())
    # colors.remove(color)
    used_colors.append(colors())
    tim.pencolor(colors())

    
    tim.forward(randint(0,101))
    tim.setheading(choice([0,90,180,270]))

print(used_colors)   

screen = Screen()
screen.exitonclick()