import turtle_crossing
import snake_game
import pong
import time

def main():
    # Python GameCenter
    while True:
        print("1: Turtle Crossing\n2: Snake Game\n3: Pong\nEnter 'q' to quit")
        user_choice = input("Please enter a number between 1-3 to select a game")

        if user_choice == '1':
            turtle_crossing.play_turtle_crossing()
            break
        elif user_choice == '2':
            snake_game.play_snake_game()
            break
        elif user_choice == '3':
            pong.play_pong()
        elif user_choice == 'q':
            break
        else:
            print("Please enter a valid input!")


if __name__ == '__main__':
    main()
