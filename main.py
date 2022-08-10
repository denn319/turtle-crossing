import time
from turtle import Turtle, Screen
from vehicle import Vehicle
from player import Player
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

cars = Vehicle()
player = Player()

screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=screen.bye, key="Escape")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.drive()

screen.exitonclick()
