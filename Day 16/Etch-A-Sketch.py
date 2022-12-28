from turtle import Turtle as T
from turtle import Screen

tim = T()

def left():
    tim.left(5)
def right():
    tim.right(5)
def forward():
    tim.forward(1)
def backward():
    tim.backward(1)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key = "a", fun = left)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "w", fun = forward)
screen.onkey(key = "s", fun = backward)
screen.onkey(key = "c", fun = clear)





screen.exitonclick()