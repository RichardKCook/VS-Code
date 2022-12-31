from turtle import Turtle as T
from random import randint


class Food(T):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.setposition(randint(-280, 280), randint(-280, 280))

    def refresh(self):
        self.setposition(randint(-280, 280), randint(-280, 280))
