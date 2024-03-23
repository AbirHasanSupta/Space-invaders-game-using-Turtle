import random
from turtle import Turtle


class EnemyBullet:
    def __init__(self):
        self.e_bullets = []
        self.rand_f = 1
        self.rand_c = 9

    def create_enemy_bullet(self, x, y):
        random_chance = random.randint(self.rand_f, self.rand_c)
        if random_chance == 1:
            bullet = Turtle()
            bullet.shape('circle')
            bullet.shapesize(stretch_wid=0.2, stretch_len=0.2)
            bullet.color("orange")
            bullet.penup()
            bullet.goto(x, y - 13)
            self.e_bullets.append(bullet)

    def move_enemy_bullet(self):
        for bullet in self.e_bullets:
            bullet.goto(bullet.xcor(), bullet.ycor() - 9)







