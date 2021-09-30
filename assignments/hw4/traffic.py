"""
NAME: Eric Beaver
traffic.py

Problem: analyzes traffic patterns through average number of
    vehicles that have traveled over all roads.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    number_of_roads = eval(input("How many roads were surveyed? "))
    total_cars = 0
    for i in range(number_of_roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        acc = 0
        for j in range(days):
            cars = eval(input("     How many cars traveled on day " + str(j + 1) + "? "))
            total_cars = total_cars + cars
            acc = acc + cars
            average = acc / days
            if j == days - 1:
                print("Road " + str(i + 1) + " average vehicles per day: ", round(average, 2))
    average_vehicles_pr = total_cars / number_of_roads
    print("Total number of vehicles traveled on all roads: ", total_cars)
    print("Average number of vehicles per road: ", round(average_vehicles_pr, 2))


if __name__ == '__main__':
    main()
