"""
NAME: Eric Beaver
mean.py

Problem: Calculates the mean 3 different ways from a set of values.

1. The program will calculate the mean of a set of values using 3 different ways
2. The inputs will be the number of values in the set and those individual values themselves
The outputs will be the result of the 3 methods for calculating the mean, shown individually
3. It must first ask the user for the number of values.
    Accumulators for the three average methods should be made.
    Then it must ask the user for those individual values, iterating through a for loop.
    In that same for loop after asking for the value, it must have
    accumulators for each of the three mean types,
        and must complete the action that requires multiple
        iterations. For the rms, it must be the accumulator added
        to the value entered squared. For the harmonic, it must be the
        accumulator and added to 1 divided by the value
        entered. For the geometric, it must be the accumulator multiplied by
        the value entered (the accumulator must
        be one instead of 0).
    Then, the for loop should be completed and additional math must be
    conducted. For the rms, the square root of the
        accumulator over the number of values should be done.
        For the harmonic, the number of value should be divided by
        the accumulator. For the geometric, the accumulator must be put
        to the power of 1 divided by the number of
        values.
    Finally, the three results should be printed out, in the order of
    rms, harmonics, and geometric. Within the print
    statement, the results should be rounded to the thousandths place.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def main():
    # input number of values
    values_number = eval(input("enter the values to be entered: "))
    # declare accumulators
    rms_acc = 0
    harmonic_acc = 0
    geometric_acc = 1

    for i in range(values_number):
        # input specific values
        value = eval(input("enter value " + str(i+1) + ": "))
        # math required for inside for loop and iteration
        rms_acc = rms_acc + (value ** 2)
        harmonic_acc = harmonic_acc + (1 / value)
        geometric_acc = geometric_acc * value

    # math outside of for loop, once accumulators are finished
    rms_mean = math.sqrt((1 / values_number) * rms_acc)
    harmonic_mean = values_number / harmonic_acc
    geometric_mean = math.pow(geometric_acc, (1 / values_number))

    # printing and rounding results
    print(round(rms_mean, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
