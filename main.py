from turtle import Turtle, Screen
from vehicle import Vehicle
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

cars = Vehicle()
player = Player()
board = ScoreBoard()

screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=screen.bye, key="Escape")

vehicle_speed = 0.1
game_on = True
while game_on:
    time.sleep(vehicle_speed)
    screen.update()
    cars.create()
    cars.drive()

    # detect if player hit by a vehicle
    for car in cars.all_vehicles:
        if car.distance(player) < 20:
            game_on = False
            board.game_over()

    if player.at_finish_line():
        board.update_level()
        player.start()

screen.exitonclick()
