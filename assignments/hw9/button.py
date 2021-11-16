"""
NAME: Eric Beaver
button.py

Problem: define a button

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# from graphics import Rectangle, Text, GraphWin, Point


class Button:
    """
    Class representing a button in the game, with a shape and a text
    """
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label

    def get_label(self):
        """
        gets the text of a button
        :return self.text:
        """
        return self.text

    def get_shape(self):
        """
        gets the shape of a button
        :return self.shape:
        """
        return self.shape

    def draw(self, win):
        """
        void method, draws a button on the screen
        :param win:
        :return:
        """
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """
        void method, undraws a button from the screen
        :return:
        """
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX() and self.shape.getP1().getY() <= \
                point.getY() <= self.shape.getP2().getY():
            return True
        return False

    def color_button(self, color):
        """
        void method, sets a color to a button
        :param color:
        :return:
        """
        self.shape.setFill(color)

    def set_label(self, label):
        """
        void method, sets text equal to a label
        :param label:
        :return:
        """
        self.text = label
