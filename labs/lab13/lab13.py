"""
Name: Eric Beaver
lab13.py
"""

from random import randint


def main():
    x = [5, 2, 1, 3]
    selection_sort(x)
    print(x)
    print(is_in_binary(4, x))
    trade_alert('trades.txt')


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while values[mid] != search_val and len(values) != 1:
        if values[mid] < search_val:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values) // 2
    if values[mid] == search_val:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def calc_area(rect):
    return randint(1, 100)


def rect_sort(rectangles):
    diction = {}
    areas = []
    for rect in rectangles:
        diction[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = diction[areas[i]]
    print(areas)


def trade_alert(file_name):
    in_file = open(file_name, 'r')
    data = in_file.read().split()
    for i in range(len(data)):
        if int(data[i]) > 830:
            print(str(i+1) + " seconds: Alert!")
        if 500 < int(data[i]) < 831:
            print(str(i+1) + " seconds: Warning!")


main()
