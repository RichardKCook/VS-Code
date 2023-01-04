from turtle import Turtle as T

class Scoreboard(T):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.clear()
        self.setposition(x=0, y=280)
        self.score = 1
        self.color("white")
        self.update_score()
        self.game_over_text

    def update_score(self):
        self.write(f"Level: {self.score}", move=False,
                   align="center", font=("Arial", 14, "normal"))

    def count(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over_text(self):
        self.setpos(0, 0)
        self.clear()
        self.write(f"       Game Over\nYou made it to Level {self.score}", move=False, align="center",
                   font=("Arial", 18, "normal"))
        