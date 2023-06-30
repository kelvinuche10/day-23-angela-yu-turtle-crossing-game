from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RAND_Y = random.randint(-280, 280)


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []


    def create_car(self):
        new_tutle = Turtle('square')
        new_tutle.penup()
        new_tutle.color(random.choice(COLORS))
        rand_y = random.randint(-250, 280)
        new_tutle.goto(250, rand_y)
        new_tutle.shapesize(stretch_wid=1, stretch_len=2)
        self.all_cars.append(new_tutle)
                


    def move_car(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
