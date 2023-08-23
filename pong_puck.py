from turtle import Turtle

MOVING_SPEED = 20
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class Puck(Turtle):
    def __init__(self, puck_length, starting_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=puck_length, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(starting_x, 0)
        self.setheading(0)
        self.up = True
        self.score = 0

    def move_up(self):
        """Moves the puck up the screen"""
        self.up = True

    def move_down(self):
        """Moves the puck down the screen"""
        self.up = False

    def move(self):
        """Keeps Puck in constant motion"""
        if self.up:
            self.goto(self.xcor(), self.ycor() + MOVING_SPEED)
        else:
            self.goto(self.xcor(), self.ycor() - MOVING_SPEED)

    def reverse(self):
        """Reverses direction of the puck"""
        self.up = not self.up

    def check_wall_collision(self):
        """Check if puck collided with wall, and automatically reverse its direction in that case"""
        if self.ycor() <= (-SCREEN_HEIGHT/2) + 20 or self.ycor() >= (SCREEN_HEIGHT/2) - 20:
            self.reverse()

