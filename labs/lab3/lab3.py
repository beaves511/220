"""
Name: Eric Beaver
lab3.py
"""


def average():
    number_of_grades = eval(input("Enter the number of grades:"))
    total = 0
    for i in range(number_of_grades):
        x = eval(input("Enter your grade on HW " + str(i + 1) + ": "))
        total = total + x
    mean = total / number_of_grades
    print("The average of the grades is", mean)


def tip_jar():
    total = 0
    people = 5
    for i in range(people):
        question = eval(input("Enter donation amount:"))
        total = total + question
    print("The total amount in the tip jar is", total, "dollars")


def newton():
    x = eval(input("Enter the number: "))
    refinements = eval(input("How many times do you want to improve the approximation: "))
    approx = x / 2
    for i in range(refinements):
        approx = (approx + (x / approx)) / 2
    print("The approximation is", approx)


def sequence():
    number = eval(input("Enter the number of terms: "))
    for i in range(1, number + 1):
        terms = 1 + ((i // 2) * 2)
        print(terms, end=" ")


def pi():
    acc = 1
    number = eval(input("Enter the number of terms: "))
    for i in range(number):
        num = 2 + ((i // 2) * 2)
        den = 1 + (((i + 1) // 2) * 2)
        fra = num / den
        acc = acc * fra
    print(acc * 2)

