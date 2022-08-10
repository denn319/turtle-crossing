import time
from turtle import Turtle, Screen
from vehicle import Vehicle
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

cars = Vehicle()

tur = Turtle()
tur.penup()
tur.color("black")
tur.shape("turtle")
tur.setheading(90)


def up():
    x_new = tur.xcor()
    y_new = tur.ycor() + 10
    tur.goto((x_new, y_new))


def down():
    x_new = tur.xcor()
    y_new = tur.ycor() - 10
    tur.goto((x_new, y_new))


def left():
    x_new = tur.xcor() - 10
    y_new = tur.ycor()
    tur.goto((x_new, y_new))


def right():
    x_new = tur.xcor() + 10
    y_new = tur.ycor()
    tur.goto((x_new, y_new))


screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=screen.bye, key="Escape")


game_on = True
while game_on:
    # time.sleep(0.5)
    screen.update()
    cars.drive()

screen.exitonclick()
