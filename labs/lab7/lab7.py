"""
Name: Eric Beaver
Partner: Oliver Aschenbrenner
lab7.py
"""
import math
from math import *


def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(5))
    print(sum_n_cubes(3))
    encode_better()


def cash_conversion():
    value = eval(input("Enter an integer: "))
    print("${:.2f}".format(value))


def encode():
    message = input("Enter a message: ")
    key = eval(input("Enter an integer key value: "))
    acc = ""
    for i in message:
        num = ord(i)
        add = num + key
        cha = chr(add)
        acc = acc + cha
    print(acc)


def sphere_area(radius):
    surface_area = 4 * math.pi * math.pow(radius, 2)
    return surface_area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    return volume


def sum_n(n):
    acc = 0
    for i in range(n+1):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n+1):
        acc = acc + math.pow(i, 3)
    return acc


def encode_better():
    message = input("Enter a message: ")
    key_word = input("Enter a key: ")
    acc = ""
    for i in range(len(message)):
        char = message[i]
        key = key_word[i % len(key_word)]
        char_val = ord(char)
        key_val = ord(key) - 97
        code = char_val + key_val
        code_char = chr(code)
        acc = acc + code_char
    print(acc)


main()
