from turtle import Turtle
from pong_puck import SCREEN_HEIGHT

BALL_MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.setheading(180)
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE

    def move(self):
        """Keeps the ball in constant diagonal motion"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collided_vertical(self):
        """Returns true if ball collides with the top or bottom wall"""
        return self.ycor() > SCREEN_HEIGHT/2 - 10 or self.ycor() < -SCREEN_HEIGHT/2 + 10

    def bounce_vertical(self):
        """Causes the ball to bounce off vertically"""
        self.y_move *= -1

    def bounce_horizontal(self):
        """Causes the ball to bounce off horizontally"""
        self.x_move *= -1
