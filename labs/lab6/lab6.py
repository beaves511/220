"""
Name: Eric Beaver
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter the name: ")
    split_name = name.split(" ")
    print(split_name[1] + ", " + split_name[0])


def company_name():
    domain = input("Enter a three part domain name: ")
    company = domain.split(".")
    print(company[1])


def initials():
    n = eval(input("How many names will be inputted? "))
    for i in range(n):
        first = input("Enter the name of student " + str(i + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        print(first + "'s initials are " + first[0] + last[0])


def names():
    names_list = input("Enter a list of names, separated by commas: ")
    names_list = names_list.split(",")
    print("The initials are", end=" ")
    for name in names_list:
        parts_names = name.split()
        print(parts_names[0][0] + parts_names[1][0], end=" ")


def thirds():
    n = eval(input("Enter the number of sentences that will be inputted: "))
    for _ in range(n):
        s = input("Enter the sentence: ")
        print(s[2::3])


def word_average():
    sent = input("Enter a sentence: ")
    acc = 0
    sent = sent.split(" ")
    for word in sent:
        acc = acc + len(word)
    print(acc / len(sent))


def pig_latin():
    sent = input("Enter a sentence: ")
    sent = sent.lower()
    sent = sent.split()
    for word in sent:
        print(word[1:] + word[0] + 'ay', end=" ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
