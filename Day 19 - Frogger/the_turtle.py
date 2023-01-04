from turtle import Turtle as T
import cars

class The_Turtle(T):
    def __init__(self):
        super().__init__()
        self.color("Green")
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setpos(x=0,y=-280)
        self.setheading(90)
        
    def move_forward(self):
        self.forward(5)

    def move_backward(self):
        self.backward(5)
    
    def goto_start(self):
        self.setpos(x=0,y=-280)
        cars.CAR_SPEED *= 1.5