from turtle import Turtle as T


class Paddle(T):
    def __init__(self, x, y):
        super().__init__()
        self.paddles = []
        self.color("white")
        self.shape("square")
        self.penup()
        self.tilt(90)
        self.setpos(x, y)
        self.turtlesize(stretch_wid=0.5, stretch_len=5)
        self.paddles.append(self)

    def move_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor()-20)
