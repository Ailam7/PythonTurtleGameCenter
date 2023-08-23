from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-10, 280)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 16, 'normal'))

    def increment(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 16, 'normal'))

