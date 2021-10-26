"""
NAME: Eric Beaver
weighted_average.py

Problem: Calculate the weighted average from text files

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    weighted_average('grades.txt', 'avg.txt')


def weighted_average(in_file_name, out_file_name):
    my_file = open(in_file_name, 'r')
    output_file = open(out_file_name, 'w')
    class_avg = 0
    count = 0
    colon = 0
    for line in my_file:
        acc_hun = 0
        acc_out = 0
        word = line.split()
        for i in range(len(word)):
            if word[i].find(':') > -1:
                colon = i
                word[i] = word[i].replace(':', "")
        name_string = " "
        name_string = name_string.join(word[0: colon + 1])
        for i in range(colon + 1, len(word), 2):
            acc_hun = acc_hun + int(word[i])
        if acc_hun > 100:
            output_file.write(name_string + "'s average: Error: The weights are more than 100.\n")
        elif acc_hun < 100:
            output_file.write(name_string + "'s average: Error: The weights are less than 100.\n")
        else:
            for i in range(colon + 1, len(word), 2):
                acc_out = acc_out + (int(word[i]) * int(word[i + 1]))
            acc_out_f = acc_out / 100
            class_avg = class_avg + acc_out_f
            count += 1
            output_file.write(name_string + "'s average: {:.1f}".format(acc_out_f) + '\n')

    if count == 0:
        class_avg = 0
    else:
        class_avg = class_avg / count
    output_file.write('Class average: {:.1f}'.format(class_avg))

    my_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
