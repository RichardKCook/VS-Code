from turtle import Turtle as T
from turtle import Screen

timmy = T()

timmy.color("green")
timmy.shape("turtle")

for i in range(4):
    for i in range(5):

        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

    timmy.left(90)

screen = Screen()

screen.exitonclick()