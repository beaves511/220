"""
Name: <your name goes here – first and last>
lab12.py
"""
from random import randint


def main():
    # add other function calls here
    lst = [1, 2, 3, 4, 5, 6]
    find_and_remove_first(lst, 4)
    good_input()
    num_digits()
    read_data('nums.txt')
    is_in_linear(10, lst)
    hi_lo_game()


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Eric"
    except:
        pass


def read_data(filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def good_input():
    inp = eval(input("Enter a number between 1 and 10: "))
    while not (1 < inp < 10):
        inp = eval(input("Please enter a number between 1 and 10: "))
    return inp


def num_digits():
    num = eval(input("Enter a positive number: "))
    while num > 0:
        digits = 0
        while num != 0:
            num //= 10
            digits += 1
        print("The number of digits is", digits)
        num = eval(input("Enter a positive number: "))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 1
    guess = eval(input("Guess a number in between 1 and 100: "))
    while guess != num and guesses != 7:
        guesses += 1
        if guess < num:
            print("The guess was too low")
        elif guess > num:
            print("The guess was too high")
        if guess != num and guesses != 7:
            guess = eval(input("Enter a guess:"))
    if guess == num:
        print("You won! Number of guesses was", guesses)
    else:
        print("You lost")


main()
