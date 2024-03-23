import time
from turtle import Turtle


class Bullet:
    def __init__(self):
        self.all_bullets = []
        self.last_bullet_time = 0
        self.cooldown = 0.4

    def create_bullet(self, x, y):
        current_time = time.time()
        if current_time - self.last_bullet_time > self.cooldown:
            bullet = Turtle()
            bullet.shape('square')
            bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
            bullet.color("yellow")
            bullet.penup()
            bullet.goto(x, y + 30)
            self.all_bullets.append(bullet)
            self.last_bullet_time = current_time

    def move_bullet(self):
        for bullet in self.all_bullets:
            bullet.goto(bullet.xcor(), bullet.ycor() + 12)
