from turtle import Turtle as T
from random import randint
import time
import gc
CAR_SPEED = 5

class Cars(T):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.color(randint(0,255),randint(0,255),randint(0,255))
        self.shape("square")
        self.turtlesize(stretch_wid=1.5,stretch_len=3)
        self.penup()
        self.speed("slowest")
        self.setpos(x=340,y=randint(-240,240))
        self.setheading(180)
        self.cars.append(self)
        
    
    def move(self):
        if 1 > 0:
            for car in range(len(self.cars)):
                self.cars[car].fd(CAR_SPEED)
        
    def create_car(self):
        new_car = Cars()
        self.cars.append(new_car)


    def remove(self):    
        if self.cars[0].xcor() <= -340 and len(self.cars) > 0:
            del self.cars[0]         
            gc.collect()
            

    