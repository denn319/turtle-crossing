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
        self.shape("square")
        self.color(random.choice(COLORS))
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.hideturtle()
        self.x_start = 500
        self.y_start = 280
        self.all_vehicles = []
        # self.create()

    def create(self):
        # for idx in range(1, VEHICLE_NUM + 1, 1):
            # x_pos = self.x_start - random.choice(STARTING_POS) * random.choice(POS_MULTIPLIER)
            # y_pos = self.y_start - idx * VEHICLE_GAP
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            x_pos = 380
            y_pos = random.randint(-250, 250)
            xy_pos = (x_pos, y_pos)
            self.new_vehicle(xy_pos)

    def new_vehicle(self, xy_pos):
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
