from turtle import Turtle

class GameEnd(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 16, 'normal'))

