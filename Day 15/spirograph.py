from turtle import Turtle as T
from turtle import Screen
from turtle import colormode
from random import choice
from random import randint


def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b


used_colors=[]


tim = T()
colormode(255)
tim.shape("turtle")
tim.color("green")
# tim.pensize(15)
tim.speed("fastest")
for i in range(1,36):
    tim.setheading(i*10)
    color = choice(random_color())
    used_colors.append(random_color())
    tim.pencolor(random_color())
    tim.circle(100)
    

print(used_colors)   

screen = Screen()
screen.exitonclick()