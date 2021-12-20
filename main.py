import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.go_up,"Up")

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_start_position():
        player.go_to_start()
        car_manager.new_level()
        scoreboard.level_up()






screen.exitonclick()
