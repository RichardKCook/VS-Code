from turtle import Turtle as T
from turtle import Screen

def move_forward():
    tim.forward(100)

tim = T()
screen = Screen()
screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()