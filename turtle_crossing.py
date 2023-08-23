from turtle import Screen
from turtle_crossing_player import Player
from turtle_crossing_car import Car
from turtle_crossing_scoreboard import Scoreboard
import time

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def play_turtle_crossing():

    # Create the screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()

    # Initialize player and cars
    bob = Player()
    score = Scoreboard()
    screen.onkey(bob.move_forward, "Up")

    counter = 0
    cars = []
    move_speed = 20

    game_over = False
    while not game_over:

        if counter == 3:
            car = Car()
            cars.append(car)
            counter = 0

        time.sleep(0.1)
        screen.update()
        counter += 1

        for car in cars:
            car.move(move_speed)
            if bob.distance(car) < 20:
                screen.update()
                score.game_end()
                game_over = True

        if bob.ycor() > 280:
            score.increment()
            move_speed += 10
            bob.goto(0, -280)
            
    screen.exitonclick()

