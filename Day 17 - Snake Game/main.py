from turtle import Screen
from turtle import mode
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
mode("standard")  # facing east config


snake = Snake()
snake.create_snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    # showing snake piece iff food is eaten. Must come after update due to implementation of snake bites.
    snake.show()
    snake.move()
    snake.scoreboard.update_score()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.scoreboard.count()
        snake.add_bite()



screen.exitonclick()
