from turtle import Turtle as T


class Scoreboard(T):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.clear()
        self.setposition(x=0, y=280)
        self.score = 0
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False,
                   align="center", font=("Arial", 14, "normal"))

    def count(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over_text(self):
        self.setpos(0, 0)
        self.clear()
        self.write("Game Over", move=False, align="center",
                   font=("Arial", 18, "normal"))
