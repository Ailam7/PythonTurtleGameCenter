from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "white"]
        self.penup()
        self.shape("square")
        self.setheading(270)
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(random.choice(self.colors))
        self.goto((280, random.randint(-250, 250)))

    def move(self, move_speed):
        self.goto(self.xcor() - move_speed, self.ycor())

