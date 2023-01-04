import random
from turtle import Screen
import time
from the_turtle import The_Turtle
from cars import Cars
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.mode('standard')
screen.tracer(0)
screen.title("Frogger, but with a Turtle")
screen.colormode(255)


frogger = The_Turtle()
car = Cars()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=frogger.move_forward)
screen.onkey(key="Down", fun=frogger.move_backward)

GAME_OVER = False

while not GAME_OVER:
    screen.update()
    car.move()

    if frogger.ycor() >= 280:
        frogger.goto_start()
        scoreboard.count()
        

    if len(car.cars) < 5:
        if random.randint(0,100) % 4 == 0:
            car.create_car()

    if len(car.cars) < 10:
        if random.randint(0,100) % 13 == 0:
            car.create_car()

    for idx in range(len(car.cars)):
        if frogger.distance(car.cars[idx]) < 30:
            scoreboard.game_over_text()
            GAME_OVER = True
    
    car.remove()

    time.sleep(0.1)
    

screen.exitonclick()