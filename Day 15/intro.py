from turtle import Turtle as t
from turtle import Screen


timmy = t()

timmy.color("red")
timmy.shape("turtle")

def move():
    timmy.forward(100)
def turn():
    timmy.left(90)

for i in range(4):
    move()
    turn()









screen = Screen()
screen.exitonclick()