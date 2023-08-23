from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y, player_name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.color("white")
        self.score = 0
        self.write(arg=f"{self.score}", move=False, align="center", font=('Arial', 32, 'bold'))

    def increment(self):
        """Increments the score and update the scoreboard"""
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", move=False, align="center", font=('Arial', 32, 'bold'))
