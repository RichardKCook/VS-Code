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
        with open("/Users/Cook/Documents/VS Code/Day 17 - Snake Game/high_score.txt") as f:
            self.high_score = int(f.read())

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False,
                   align="center", font=("Arial", 14, "normal"))
       

    def count(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/Cook/Documents/VS Code/Day 17 - Snake Game/high_score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
            self.update_score()
        self.score = 0    

    # def game_over_text(self):
    #     self.setpos(0, 0)
    #     self.clear()
    #     self.write("Game Over", move=False, align="center",
    #                font=("Arial", 18, "normal"))
    #     self.setpos(0, -30)
    #     self.write(f"High Score is {self.high_score}", move=False, align="center",
    #                font=("Arial", 18, "normal"))
