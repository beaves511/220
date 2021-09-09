"""
Name: Eric
lab2.py
"""

import math


def sum_of_threes():
    bound = eval(input("Enter the upper bound:"))
    total = 0
    for i in range(0, bound + 1, 3):
        total += i
    print("The sum of the multiples of three is", total)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter the length of the triangle's first side:"))
    b = eval(input("Enter the length of the triangle's second slide"))
    c = eval(input("Enter the length of the triangle's third slide"))
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    output = math.sqrt(area)
    print("The area of the triangle is", output)


def sum_squares():
    lower = eval(input("Enter the lower bound of the range:"))
    higher = eval(input("Enter the upper bound of the range:"))
    total = 0
    for i in range(lower, higher + 1):
        total += i ** 2
    print("The sum of the squares is", total)


def power():
    base = eval(input("Enter the base:"))
    expo = eval(input("Enter the exponent:"))
    total = 1
    for i in range(expo):
        total *= base
    print("The result is", total)
