import turtle
from turtle import Turtle, Screen
from pong_puck import Puck
from pong_ball import Ball
from pong_scoreboard import Scoreboard
import time

# CONSTANTS
PUCK_LENGTH = 5
P1_STARTING_X = -380
P2_STARTING_X = 370
SLEEP_TIME = 0.1
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


# LETS PLAY PING PONG #

def play_pong():
    # Create a black blank screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    # Create both pucks and the ball
    puck_p1 = Puck(PUCK_LENGTH, P1_STARTING_X)
    puck_p2 = Puck(PUCK_LENGTH, P2_STARTING_X)
    pucks = [puck_p1, puck_p2]
    ball = Ball()

    # Create the scoreboards
    p1_score = Scoreboard(-100, SCREEN_HEIGHT / 2 - 50, "ailam")
    p2_score = Scoreboard(100, SCREEN_HEIGHT / 2 - 50, "AI")

    # Create partition (A grey dashed line in the middle)
    partition = Turtle()
    partition.hideturtle()
    partition.penup()
    partition.goto(0, 300)
    partition.pensize(5)
    partition.pencolor("grey")
    partition.pendown()
    partition.setheading(270)
    for num in range(screen.window_height() // 30):
        partition.forward(30)
        partition.penup()
        partition.forward(30)
        partition.pendown()

    # Taking input from keyboard for pucks
    # Puck 1 controlled by w,s. Puck 2 controlled by Arrow Keys
    screen.listen()
    screen.onkey(puck_p1.move_up, "w")
    screen.onkey(puck_p1.move_down, "s")
    screen.onkey(puck_p2.move_up, "Up")
    screen.onkey(puck_p2.move_down, "Down")

    # Run the game
    game_over = False
    while not game_over:
        time.sleep(0.1)
        screen.update()

        # Move the pucks and reverse their direction if they hit the wall
        puck_p1.move()
        puck_p2.move()
        puck_p1.check_wall_collision()
        puck_p2.check_wall_collision()

        # Move the ball
        ball.move()
        if ball.collided_vertical():
            ball.bounce_vertical()

        # Detect ball collision with puck
        for puck in pucks:
            if puck.distance(ball) > 50:
                ball.bounce_horizontal()

        # Detect if ball has gone out of bounds
        if ball.xcor() > SCREEN_WIDTH / 2:
            # increase p1 score
            p1_score.increment()
            ball.goto(0, 0)
            ball.bounce_horizontal()
        elif ball.xcor() < - SCREEN_WIDTH / 2:
            # increase p2 score
            p2_score.increment()
            ball.goto(0, 0)
            ball.bounce_horizontal()

        if p1_score.score == 5 or p2_score.score == 5:
            game_over = True
    screen.exitonclick()