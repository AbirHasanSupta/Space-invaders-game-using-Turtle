from turtle import Turtle
import turtle
turtle.register_shape("images/resized_spaceship.gif")


class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/resized_spaceship.gif")
        self.penup()
        self.goto(0, -295)

    def move_left(self):
        new_x = self.xcor() - 8
        self.goto(new_x, self.ycor())
        if new_x < -370:
            self.goto(-370, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 8
        self.goto(new_x, self.ycor())
        if new_x > 365:
            self.goto(365, self.ycor())
