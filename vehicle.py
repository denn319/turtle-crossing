from turtle import Turtle
import random

COLORS = ["black", "yellow", "blue", "red", "green", "cyan", "magenta"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

STARTING_POS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
POS_MULTIPLIER = [1, 2, 3, 4, 5]
VEHICLE_NUM = 10
VEHICLE_GAP = 35


class Vehicle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_vehicles = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            x_pos = 380
            y_pos = random.randint(-250, 250)
            xy_pos = (x_pos, y_pos)
            new_vehicle = Turtle("square")
            new_vehicle.pu()
            new_vehicle.color(random.choice(COLORS))
            new_vehicle.shapesize(stretch_wid=1, stretch_len=2)
            new_vehicle.setpos(xy_pos)
            self.all_vehicles.append(new_vehicle)

    def drive(self):
        for idx in range(len(self.all_vehicles)):
            x_new = self.all_vehicles[idx].xcor() - STARTING_MOVE_DISTANCE
            y_new = self.all_vehicles[idx].ycor()
            self.all_vehicles[idx].goto((x_new, y_new))

