"""
NAME: Eric Beaver
bumper.py

Problem: Make bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb, time


def main():
    win = GraphWin("Bumper Cars", 900, 700)
    circle_one = Circle(Point(200, 300), 20)
    circle_two = Circle(Point(600, 150), 20)
    circle_one.setFill(get_random_color())
    circle_two.setFill(get_random_color())
    circle_one.draw(win)
    circle_two.draw(win)

    # while loop here
    k = 1
    x_one = get_random(8)
    y_one = get_random(8)
    x_two = get_random(8)
    y_two = get_random(8)
    while k < 100:
        circle_one.move(x_one, y_one)
        circle_two.move(x_two, y_two)
        time.sleep(.05)
        if hit_horizontal(circle_one, win):
            x_one = x_one * -1
        if hit_horizontal(circle_two, win):
            x_two = x_two * -1
        if hit_vertical(circle_one, win):
            y_one = y_one * -1
        if hit_vertical(circle_two, win):
            y_two = y_two * -1
        if did_collide(circle_one, circle_two):
            x_one = x_one * -1
            x_two = x_two * -1
            y_one = y_one * -1
            y_two = y_two * -1
            win.update()
        k = 1
        if win.checkMouse():
            k = 101

    win.close()


def get_random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def get_random(move_amount):
    random_int = randint(-move_amount, move_amount)
    return random_int


def did_collide(ball, ball2):
    distance_x = (ball2.getCenter().getX() - ball.getCenter().getX()) ** 2
    distance_y = (ball2.getCenter().getY() - ball.getCenter().getY()) ** 2
    distance_tot = math.sqrt(distance_x + distance_y)
    if distance_tot <= ball.getRadius() + ball2.getRadius():
        return True
    return False


def hit_vertical(ball, win):
    if ball.getCenter().getY() <= ball.getRadius():
        win.update()
        return True
    if ball.getCenter().getY() >= win.getHeight() - ball.getRadius():
        win.update()
        return True
    return False


def hit_horizontal(ball, win):
    if ball.getCenter().getX() <= ball.getRadius():
        win.update()
        return True
    if ball.getCenter().getX() >= win.getWidth() - ball.getRadius():
        win.update()
        return True
    return False


if __name__ == '__main__':
    main()
