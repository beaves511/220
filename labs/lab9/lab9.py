"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import GraphWin, Circle, Text, Point
import math


def main():
    # add other function calls here
    x = [5, 2, -3]
    addTen(x)
    print(x)
    y = [3, 5.7, 2]
    squareEach(y)
    print(y)
    a = sumList(y)
    print(a)
    z = ["3", '5.7', '2']
    toNumbers(z)
    print(z)
    writeSumOfSquares()
    starter()
    leapYear(2011)
    circleOverlap()


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    return sum


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    initial = input("What is the name of the input file?: ")
    infile = open(initial, "r")
    output = open('output.txt', 'w+')
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        x = sumList(nums)
        output.write("The sum of squares is " + str(x) + '\n')


def starter():
    weight = float(input("What is the weight of the player?: "))
    num_wins = int(input("How many games has the player won?: "))
    if 150 <= weight <= 160 and num_wins >= 5:
        print('Is starter.')
    elif weight > 199 or num_wins > 20:
        print("Is starter.")
    else:
        print("Is not starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + " is a leap year")
        return True
    else:
        print(str(year) + ' is not a leap year')
        return False

def circleOverlap():
    win = GraphWin("CircleOverlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius1)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle1 = Circle(p3, radius2)
    circle1.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    if distance <= radius1 + radius2:
        result_text = Text(Point(150, 20), "The circles overlap.")
    else:
        result_text = Text(Point(150, 20), "The circles do not overlap.")
    result_text.draw(win)

    close_text = Text(Point(150, 380), "Click to close the program.")
    close_text.draw(win)

    win.getMouse()
    win.close()


main()
