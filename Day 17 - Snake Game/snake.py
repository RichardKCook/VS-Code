from turtle import Turtle as T
from scoreboard import Scoreboard
MOVE_DISTANCE = 20


class Snake:
    """Creates Snake Object"""

    def __init__(self):

        self.snake_pieces = []
        self.snake_body_postions = []

        self.init_x = 0
        self.init_y = 0
        self.create_snake()
        self.head = self.snake_pieces[0]
        # removes head from snake to allow for collision check in move method
        self.snake_body = self.snake_pieces[1:len(self.snake_pieces)]
        self.snake_body_postions.pop(0)

    def create_snake(self):
        for position in range(2):
            self.add_bite()
            self.show()
            self.init_x -= 20

    def add_bite(self):

        snake_bite = T()
        snake_bite.hideturtle()
        snake_bite.shape("square")
        snake_bite.color("green")
        snake_bite.penup()
        snake_bite.setposition(self.init_x, self.init_y)
        self.snake_pieces.append(snake_bite)
        self.snake_body_postions.append(snake_bite.pos())

    def show(self):

        self.snake_pieces[-1].showturtle()

    def move(self):
        """Moves the Snake Forward"""
        for pieces_num in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[pieces_num - 1].xcor()
            new_y = self.snake_pieces[pieces_num - 1].ycor()
            self.snake_pieces[pieces_num].setposition(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= -300:
            Scoreboard().game_over_text()
            return True
        for piece in self.snake_pieces[1:len(self.snake_pieces)]:
            
            if self.head.distance(piece) < 10:
                Scoreboard().game_over_text()
                return True

    def up(self):
        """Tells the Snake to Move in the Upwards Direction"""
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        """Tells the Snake to Move in the Downwards Direction"""
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def left(self):
        """Tells the Snake to Move in the Left Direction"""
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)

    def right(self):
        """Tells the Snake to Move in the Right Direction"""
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)
