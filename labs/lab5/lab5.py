"""
Name: Eric Beaver
lab5.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    white = Circle(Point(250, 250), 250)
    black = Circle(Point(250, 250), 200)
    blue = Circle(Point(250, 250), 150)
    red = Circle(Point(250, 250), 100)
    yellow = Circle(Point(250, 250), 50)

    white.setFill("white")
    black.setFill("black")
    blue.setFill("blue")
    red.setFill("red")
    yellow.setFill("yellow")

    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)

    instruct_text = Text(Point(250, 480), "Click the screen to close the window")
    instruct_text.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    tri = Polygon(p1, p2, p3)
    tri.draw(win)

    ax = abs(p2.getX() - p1.getX())
    ay = abs(p2.getY() - p1.getY())

    bx = abs(p3.getX() - p2.getX())
    by = abs(p3.getY() - p2.getY())

    cx = abs(p3.getX() - p1.getX())
    cy = abs(p3.getY() - p1.getY())

    la = math.sqrt(math.pow(ax, 2) + math.pow(ay, 2))
    lb = math.sqrt(math.pow(bx, 2) + math.pow(by, 2))
    lc = math.sqrt(math.pow(cx, 2) + math.pow(cy, 2))
    perm = la + lb + lc

    s = (la + lb + lc) / 2
    area = math.sqrt(s * ((s - la) * (s - lb) * (s - lc)))

    area_text = Text(Point(150, 20), "The area is " + str(area))
    perm_text = Text(Point(150, 50), "The perimeter is " + str(perm))
    area_text.draw(win)
    perm_text.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    # 'Create code to allow a user to color a shape by entering rgb amounts'

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_height / 2, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_height / 2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_height / 2, win_height / 2 + 100), 5)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    message = input("Enter a string: ")
    print(message[0])
    print(message[-1])
    print(message[2:6])
    print(message[0] + message[-1])
    print(message[0:3] * 10)
    for i in message:
        print(i)
    print(len(message))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 3
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    num_terms = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(num_terms):
        x = 2 + 2 * (i % 3)
        print(x, end=" ")
        acc += x
    print("\nsum = ", acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()



main()
