from turtle import Turtle

ALIGN = "Left"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("Black")
        self.level = 1
        self.setpos(-380, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def reset_pos(self):
        x_new = 0
        y_new = 280
        xy_pos = (x_new, y_new)
        self.setposition(xy_pos)

    def update_level(self):
        self.level += 1
        self.display_score()

    def reset_level(self):
        self.level = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
