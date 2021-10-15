"""
NAME: Eric Beaver
vigenere.py

Problem: create a vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Entry, Text, GraphWin, Point, Rectangle


def code(phrase, key):
    # print("Hello")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    phrase = phrase.upper()
    phrase = phrase.replace(" ", "")
    key = key.upper()
    string_acc = ""
    j = 0
    for i in range(len(phrase)):
        if j > len(key) - 1:
            j = 0
        position_phrase = alphabet.find(phrase[i])
        position_key = alphabet.find(key[j])
        if (position_key + position_phrase) > 25:
            num = (position_key + position_phrase) - 26
        else:
            num = position_phrase + position_key
        string_acc = string_acc + alphabet[num]
        j = j+1

    return string_acc


def main():
    win = GraphWin('Vigenere', 500, 500)
    message_one = Text(Point(150, 100), "Message to Code")
    message_one_entry = Entry(Point(350, 100), 25)
    message_two = Text(Point(150, 200), "Enter Keyword")
    message_two_entry = Entry(Point(350, 200), 25)
    button_one = Rectangle(Point(175, 250), Point(350, 315))
    button_message = Text(Point(263, 283), "Encode")
    message_one.draw(win)
    message_one_entry.draw(win)
    message_two.draw(win)
    message_two_entry.draw(win)
    button_one.draw(win)
    button_message.draw(win)

    win.getMouse()
    encode = code(message_one_entry.getText(), message_two_entry.getText())
    button_one.undraw()
    button_message.undraw()
    result_text = Text(Point(245, 280), "Resulting Message:")
    encode_text = Text(Point(240, 300), encode)
    close_text = Text(Point(245, 480), "Click anywhere to close the window.")

    result_text.draw(win)
    encode_text.draw(win)
    close_text.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
