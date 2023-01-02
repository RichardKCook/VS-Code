from turtle import Screen
from turtle import Turtle as T
from player import Player as P
from ball import Ball
from paddle import Paddle as Pads
from time import sleep
import time

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
screen.mode("standard")

players = P()
ball = Ball()
l_paddle = Pads(-380, 0)
r_paddle = Pads(380, 0)


screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)


game_over = False
game_over = players.update_score()

while not game_over:
    screen.update()
    time.sleep(GAME_SPEED)
    ball.move_ball()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() > 360 and ball.distance(r_paddle) < 40 or ball.xcor() < -360 and ball.distance(l_paddle) < 40:
        ball.bounce_x()
        GAME_SPEED = GAME_SPEED/1.2

    if ball.xcor() >= 400:
        players.score1 += 1
        players.update_score()
        GAME_SPEED = 0.1
        ball.reset_position()

    if ball.xcor() <= -400:
        players.score2 += 1
        players.update_score()
        GAME_SPEED = 0.1
        ball.reset_position()

    game_over = players.update_score()

screen.exitonclick()
