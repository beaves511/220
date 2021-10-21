"""
Name: Eric Beaver
lab8.py
"""

from encryption import encode, encode_better


def main():
    number_words('Walrus.txt', 'Walrus_output.txt')
    hourly_wages('hourly_wages.txt', 'output_wages.txt')
    print(calc_check_sum('0072946520'))
    send_message('message.txt', 'bob')
    send_safe_message('secret_message.txt', 'aiden', 3)
    send_uncrackable_message('safest_message.txt', 'justin', 'pad.txt')
    pass


def number_words(in_file_name, out_file_name):
    my_file = open(in_file_name, 'r')
    output = open(out_file_name, 'w+')
    i = 1
    for line in my_file:
        words = line.split()
        for word in words:
            output.write(str(i) + " " + word + '\n')
            i += 1
    my_file.close()
    output.close()


def hourly_wages(in_file_name, out_file_name):
    my_file = open(in_file_name, 'r')
    output = open(out_file_name, 'w')
    for line in my_file:
        parts = line.split()
        wage = float(parts[2])
        new_wage = wage + 1.65
        final_wage = new_wage * int(parts[3])
        output.write(parts[0] + " " + parts[1] + " ${:.2f}".format(final_wage) + '\n')
    my_file.close()
    output.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += pos * (int(isbn[i]))
    return acc


def send_message(file, friend):
    my_file = open(file, 'r')
    output = open(friend, 'w+')
    for line in my_file:
        output.write(line)
    my_file.close()
    output.close()


def send_safe_message(file, friend, key):
    my_file = open(file, 'r')
    output = open(friend, 'w+')
    for line in my_file:
        output.write(encode(line, key))
    my_file.close()
    output.close()


def send_uncrackable_message(file, friend, pad):
    pad_file = open(pad, 'r')
    key = pad_file.read()
    my_file = open(file, 'r')
    output = open(friend, 'w+')
    for line in my_file:
        output.write(encode_better(line, key))
    my_file.close()
    output.close()


main()
