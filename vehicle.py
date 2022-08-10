from turtle import Turtle
import random

COLORS = ["black", "yellow", "blue", "red", "green", "cyan", "magenta"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

STARTING_POS = []
VEHICLE_NUM = 10


class Vehicle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x_start = 380
        self.y_start = 320
        self.all_vehicles = []
        self.birth()

    def birth(self):
        for idx in range(1, VEHICLE_NUM + 1, 1):
            xy_pos = (self.x_start, self.y_start - idx * 40)
            self.add_vehicle(xy_pos)

    def add_vehicle(self, xy_pos):
        new_vehicle = Turtle(shape=self.shape())
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
