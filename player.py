from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.birth()

    def birth(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        x_new = self.xcor()
        y_new = self.ycor() + MOVE_DISTANCE
        self.goto((x_new, y_new))

    def move_down(self):
        x_new = self.xcor()
        y_new = self.ycor() - MOVE_DISTANCE
        self.goto((x_new, y_new))

    def move_left(self):
        x_new = self.xcor() - MOVE_DISTANCE
        y_new = self.ycor()
        self.goto((x_new, y_new))

    def move_right(self):
        x_new = self.xcor() + MOVE_DISTANCE
        y_new = self.ycor()
        self.goto((x_new, y_new))
