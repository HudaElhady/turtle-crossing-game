import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.add_car()

    def add_car(self):
        random_value = random.randint(1, 6)
        if random_value == 1:
            car = Turtle(shape="square")
            car.turtlesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(280, random.randrange(-250, 250, 10))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def remove_car(self, car):
        car.clear()
        car.hideturtle()
        self.cars.remove(car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)