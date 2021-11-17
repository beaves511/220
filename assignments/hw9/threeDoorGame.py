"""
NAME: Eric Beaver
threeDoorGame.py

Problem: make a game with three doors

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from button import Button
from graphics import Rectangle, Text, GraphWin, Point
import random


def main():
    win = GraphWin("Three Door Game", 500, 500)

    game_message = Text(Point(240, 100), "I have a secret door")
    game_message.draw(win)
    game_message2 = Text(Point(240, 450), "Click to choose my door")
    game_message2.draw(win)

    button_one = build_button(Point(65, 200), Point(140, 250), "Door 1")
    button_one.draw(win)

    button_two = build_button(Point(215, 200), Point(290, 250), "Door 2")
    button_two.draw(win)

    button_three = build_button(Point(365, 200), Point(440, 250), "Door 3")
    button_three.draw(win)

    rand = [button_one, button_two, button_three]
    secret = random.choice(rand)

    point = win.getMouse()
    if secret.is_clicked(point):
        game_message.setText("You won!")
        game_message2.setText("Click to close")
        secret.color_button("green")
    else:
        game_message.setText("You lost!")
        game_message2.setText(str(secret.get_label()) + " is my secret door")
        for i in rand:
            if i.get_shape().getP1().getX() <= point.getX() <= i.get_shape().getP2().getX():
                i.color_button("red")

    win.getMouse()
    win.close()


def build_button(point1, point2, text):
    rect = Rectangle(point1, point2)
    label = text
    return Button(rect, label)


main()
