from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260, 270)
        self.hideturtle()
        self.pencolor("white")
        self.level = 1
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Arial", 16, "normal"))

    def increment(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=("Arial", 16, "normal"))

    def game_end(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 32, "bold"))
