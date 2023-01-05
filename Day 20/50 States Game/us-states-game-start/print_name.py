from turtle import Turtle as T



class Print_Name(T):
    def __init__(self, guess, x, y):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(x,y)
        self.write(guess, move=False, align="center",
                    font=("Arial", 12, "normal"))