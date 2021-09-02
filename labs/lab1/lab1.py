"""
Name: Eric Beaver
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter the number of shots the player made: "))
    percentage = (made / total) * 100
    print("The player's shot percentage =", percentage, "%")


def coffee():
    customer = eval(input("Enter how many pounds of coffee would you like to purchase: "))
    pound = 10.50 * customer
    shipping = .86 * customer
    cost = pound + shipping + 1.50
    print("Your total cost is", cost)


def kilometers_to_miles():
    kilometers = eval(input("Enter how many kilometers you have traveled: "))
    conversion = kilometers / 1.61
    print("You have traveled", conversion, "miles")
