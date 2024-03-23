import random
import time
from turtle import Turtle, Screen
from spaceship import SpaceShip
from enemies import Enemy
from bullet import Bullet
from enemy_bullet import EnemyBullet
from scoreboard import Scoreboard
from life import Life


def setup_game():
    global life, spaceship, score, enemies, bullets, enemy_bullets, screen

    screen.clear()
    screen.bgcolor("black")
    screen.bgpic("images/resized_bg.gif")
    screen.tracer(0)
    screen.listen()

    life = Life()
    spaceship = SpaceShip()
    score = Scoreboard()
    enemies = Enemy()
    bullets = Bullet()
    enemy_bullets = EnemyBullet()

    for j in range(90, 310, 60):
        for i in range(-300, 300, 60):
            enemies.create_enemy(i, j)

    screen.onkeypress(spaceship.move_left, "Left")
    screen.onkeypress(spaceship.move_right, 'Right')
    screen.onkey(start_game, 'Return')
    screen.onkey(lambda: bullets.create_bullet(spaceship.xcor(), spaceship.ycor()), 'space')


def start_game():
    global is_game_on
    is_game_on = True
    setup_game()
    run_game()


def run_game():
    global is_game_on
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        enemies.move_all()
        random_enemy = random.choice(enemies.all_enemy)
        enemy_bullets.create_enemy_bullet(random_enemy.xcor(), random_enemy.ycor())
        enemy_bullets.move_enemy_bullet()
        bullets.move_bullet()
        if enemies.bottom_most_enemy < -275:
            life.game_over()
            is_game_on = False
        for enemy_bullet in enemy_bullets.e_bullets:
            if spaceship.distance(enemy_bullet) < 30:
                life.reduce_life()
                spaceship.goto(0, -295)
                enemy_bullet.hideturtle()
                time.sleep(0.5)
                if life.life == 0:
                    life.game_over()
                    is_game_on = False
            if enemy_bullet.ycor() < -290:
                enemy_bullet.hideturtle()
                enemy_bullets.e_bullets.remove(enemy_bullet)

        for bullet in bullets.all_bullets:
            for enemy_bullet in enemy_bullets.e_bullets:
                if bullet.distance(enemy_bullet) < 8:
                    try:
                        bullets.all_bullets.remove(bullet)
                        bullet.hideturtle()
                    except ValueError:
                        pass
                    enemy_bullets.e_bullets.remove(enemy_bullet)
                    enemy_bullet.hideturtle()

            if bullet.ycor() > 330:
                try:
                    bullet.hideturtle()
                    bullets.all_bullets.remove(bullet)
                except ValueError:
                    pass
            else:
                for enemy in enemies.all_enemy:
                    if enemy.distance(bullet) < 20:
                        score.update_score()
                        try:
                            bullet.hideturtle()
                            bullets.all_bullets.remove(bullet)
                        except ValueError:
                            pass
                        enemy.hideturtle()
                        enemies.all_enemy.remove(enemy)
                        if enemy_bullets.rand_c > 2 and len(enemies.all_enemy) % 4 == 0:
                            enemy_bullets.rand_c -= 1
                            enemies.dir += 1
                        if not enemies.all_enemy:
                            score.winning()
                            is_game_on = False


screen = Screen()
screen.title("Space Invader")
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.bgpic("images/resized_bg.gif")

screen.tracer(0)
screen.listen()

start_text = Turtle()
start_text.hideturtle()
start_text.color("white")
start_text.penup()
start_text.goto(0, 0)
start_text.write("Press Enter to Start the Game", align="center", font=("Ariel", 30, "bold"))
screen.onkey(start_game, 'Return')
screen.mainloop()
