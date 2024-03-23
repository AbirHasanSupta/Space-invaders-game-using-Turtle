from turtle import Turtle
FONT = ("Courier", 25, "normal")


class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.life = 3
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(390, 310)
        self.current_life()

    def current_life(self):
        self.clear()
        self.write(f"Life: {self.life}", align="right", font=FONT)

    def reduce_life(self):
        self.life -= 1
        self.current_life()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over!\nPress Enter to Try Again", align="center", font=FONT)
