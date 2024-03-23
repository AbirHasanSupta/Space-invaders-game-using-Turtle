from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-390, 310)
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.score += 10
        self.current_score()

    def winning(self):
        self.goto(0, 0)
        self.write("Congratulations!!!\nYou Have Won!", align="center", font=FONT)
