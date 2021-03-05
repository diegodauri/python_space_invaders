from turtle import Screen, Turtle
import time
import random
from player import Player
from obstacle import Obstacle
from laser import Laser

POSITIONX = 220
POITIONY = 360
move_speed = 0.1
laser_move_speed = 2
life = 3

obstacles = []
lasers = []

window = Screen()

window.register_shape("icons/invader_1_small.gif")
window.register_shape("icons/invader_2_small.gif")
window.register_shape("icons/invader_3_small.gif")
window.register_shape("icons/spaceship_small.gif")

screen = Screen()
screen.bgcolor("black")
screen.setup(height=800, width=600)
screen.title("breakout")
screen.tracer(0)

for position in range(10):
    obstacle = Obstacle((POSITIONX, POITIONY), "icons/invader_3_small.gif")
    POSITIONX -= 50
    obstacles.append(obstacle)

POITIONY = 320
POSITIONX = 220

for position in range(10):
    obstacle = Obstacle((POSITIONX, POITIONY), "icons/invader_2_small.gif")
    POSITIONX -= 50
    obstacles.append(obstacle)

POITIONY = 280
POSITIONX = 220

for position in range(10):
    obstacle = Obstacle((POSITIONX, POITIONY), "icons/invader_1_small.gif")
    POSITIONX -= 50
    obstacles.append(obstacle)

player = Player((0, -370), "icons/spaceship_small.gif")


def shoot():
    time.sleep(move_speed)
    new_laser = Laser((player.xcor(), player.ycor()), "Up")
    lasers.append(new_laser)


screen.listen()
screen.onkey(key="Right", fun=player.go_right)
screen.onkey(key="Left", fun=player.go_left)
screen.onkey(key="space", fun=shoot)

game_is_on = True

right_or_left = "right"

screen.update()

while game_is_on:
    time.sleep(move_speed)
    move_speed *= 0.9
    random_num = random.randint(1, 40)
    if random_num == 5:
        for obstacle in obstacles:
            if right_or_left == "right":
                obstacle.go_right()
            elif right_or_left == "left":
                obstacle.go_left()

        if right_or_left == "right":
            right_or_left = "left"
        elif right_or_left == "left":
            right_or_left = "right"

    if random_num == 20 or random_num == 30:
        laser_move_speed += 0.1
        random_enemy = random.choice(obstacles)
        x = random_enemy.xcor()
        y = random_enemy.ycor()
        laser = Laser((x, y), "Down")
        lasers.append(laser)

    for laser in lasers:
        laser.move_laser(laser_move_speed)

    for laser in lasers:
        if laser.distance(player) < 20 and laser.direction == "Down":
            life -= 1
            laser.goto(10000, 10000)
            index = lasers.index(laser)
            lasers.pop(index)

        for obstacle in obstacles:
            if laser.distance(obstacle) < 20 and laser.direction == "Up":
                laser.goto(10000, 10000)
                obstacle.goto(10000, 10000)
                index = lasers.index(laser)
                lasers.pop(index)
                index = obstacles.index(obstacle)
                obstacles.pop(index)

    if life <= 0:
        text = Turtle()
        text.color("white")
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write(f"You lose\nEnemies remaining: {len(obstacles)}", align="center", font=("Courier", 30, "normal"))
        game_is_on = False

    if len(obstacles) == 0:
        text = Turtle()
        text.color("white")
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write(f"You win!", align="center", font=("Courier", 30, "normal"))
        game_is_on = False

    screen.update()

screen.exitonclick()