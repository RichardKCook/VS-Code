from turtle import Turtle as T
from random import randint


class Ball(T):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
