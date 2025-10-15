import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun= player.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()

    car_manager.move_cars()

    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_car_speed()
        scoreboard.increase_level()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.show_game_over()
            game_is_on = False

        if car.xcor() < -300:
            car_manager.remove_car(car)


screen.exitonclick()