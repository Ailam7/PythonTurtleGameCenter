from turtle import Screen
from snake_game_snake import Snake
from snake_game_food import Food
from snake_game_scoreboard import Scoreboard
from snake_game_game_end import GameEnd
import time


def play_snake_game():
    screen = Screen()

    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    game_over = False
    while not game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if food.distance(snake.head) < 15:
            food.refresh()
            scoreboard.increment()
            snake.extend()

        xcor = int(snake.head.xcor())
        ycor = int(snake.head.ycor())

        if xcor > 300 or xcor < -300 or ycor > 300 or ycor < -300:
            GameEnd()
            game_over = True


    screen.exitonclick()
