"""
NAME: Eric Beaver
greeting.py

Problem: create a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Polygon, Rectangle, Point, Circle, Text, time


def main():
    win_width = 500
    win_height = 500
    win = GraphWin("Greeting Card", win_width, win_height)

    heart_s_one = Circle(Point(200, 200), 50)
    heart_s_two = Circle(Point(290, 200), 50)
    heart_t = Polygon(Point(150, 200), Point(150, 215),
                      Point(240, 340), Point(340, 215), Point(340, 200))

    arrow = Polygon(Point(150, 318), Point(160, 299), Point(140, 304), Point(144, 309),
                    Point(102, 340), Point(106, 344), Point(148, 311))
    arrow_head = Polygon(Point(150, 318), Point(160, 299), Point(140, 304))
    arrow_tail = Polygon(Point(105, 349), Point(108, 343), Point(107, 340),
                         Point(104, 336), Point(102, 337), Point(98, 338))
    background = Rectangle(Point(0, 0), Point(500, 500))
    text_one = Text(Point(250, 50), "Happy Valentine's Day!")
    text_one.setSize(20)

    background.setFill("pink")

    background.draw(win)
    text_one.draw(win)

    heart_s_one.setFill("red")
    heart_s_two.setFill("red")
    heart_t.setFill("red")

    heart_s_one.setOutline("red")
    heart_s_two.setOutline("red")
    heart_t.setOutline("red")

    arrow.setFill("brown")
    arrow_head.setFill("grey")
    arrow_tail.setFill("grey")

    arrow.draw(win)
    arrow_head.draw(win)
    arrow_tail.draw(win)

    heart_s_one.draw(win)
    heart_s_two.draw(win)
    heart_t.draw(win)

    for _ in range(35):
        arrow.move(10, -7)
        arrow_head.move(10, -7)
        arrow_tail.move(10, -7)
        time.sleep(.1)

    arrow.undraw()
    arrow_head.undraw()
    arrow_tail.undraw()
    text_one.undraw()

    text_two = Text(Point(240, 460), "Click anywhere to close.")
    text_two.setSize(8)
    text_two.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
