import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


RAND_Y = random.randint(-250, 280)
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_turtle, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    car_manager.create_car()
    car_manager.move_car()
    screen.update()

    if player.ycor() > 290:
        scoreboard.increase_score()
        player.reset_turtle()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
