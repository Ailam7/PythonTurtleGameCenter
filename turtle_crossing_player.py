from turtle import Turtle

MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_forward(self):
        self.forward(20)

