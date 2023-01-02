from turtle import Turtle as T


class Player(T):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.clear()
        self.setposition(x=0, y=260)
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"                        Score: \nPlayer 1: {self.score1}                        Player 2: {self.score2}", move=False,
                   align="center", font=("Arial", 16, "normal"))

        if self.score1 == 3 or self.score2 == 3:
            self.game_over_text()
            return True

    def game_over_text(self):
        self.setpos(0, 0)
        self.clear()
        if self.score1 > self.score2:
            self.write(f"  Game Over\nPlayer 1 Wins", move=False, align="center",
                   font=("Arial", 18, "normal"))
        else:
            self.write(f"  Game Over\nPlayer 2 Wins", move=False, align="center",
                   font=("Arial", 18, "normal"))
