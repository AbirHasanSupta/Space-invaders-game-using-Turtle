from turtle import Turtle
import turtle
turtle.register_shape("images/resized_enemy.gif")


class Enemy:
    def __init__(self):
        self.all_enemy = []
        self.direction = 1
        self.dir = 5
        self.bottom_most_enemy = 0

    def create_enemy(self, x, y):
        enemy = Turtle()
        enemy.shape('images/resized_enemy.gif')
        enemy.penup()
        enemy.goto(x, y)
        self.all_enemy.append(enemy)

    def move_all(self):
        for enemy in self.all_enemy:
            enemy.setx(enemy.xcor() + self.direction*self.dir)

        left_most_enemy = min(enemy.xcor() for enemy in self.all_enemy)
        right_most_enemy = max(enemy.xcor() for enemy in self.all_enemy)

        if left_most_enemy < -370 or right_most_enemy > 365:
            self.direction *= -1
            for enemy in self.all_enemy:
                enemy.sety(enemy.ycor() - 10)
        self.bottom_most_enemy = min(enemy.ycor() for enemy in self.all_enemy)
