"""
Name: Eric Beaver
hangman.py
"""
import random


def main():
    play_game()


def read_file(name):
    file = open(name, 'r')
    word_list = []
    for line in file:
        word_list.append(line.strip())
    file.close()
    return word_list


def secret_word():
    rand_word = random.choice(read_file('wordlist.txt'))
    rand_word = rand_word.lower()
    return rand_word


def display_word(sec_word, word, letter):
    for i in range(len(sec_word)):
        if sec_word[i] == letter:
            word[i] = letter
    return word


def guesses(sec_word, letter):
    acc = 0
    for i in range(len(sec_word)):
        if sec_word[i] == letter:
            acc += 1
    return acc


def guessed(word):
    acc = 0
    for i in word:
        if i == '_':
            acc += 1
    if acc == 0:
        return True
    return False


def play_game():
    sec_word = secret_word()
    word = []
    incorrect = ""
    attempts = 7
    for i in range(len(sec_word)):
        word.append("_")
    print(" ".join(word))
    while not guessed(word) and attempts != 0:
        display = input("You have " + str(attempts) + " attempts left. Incorrect letters guessed: " + incorrect + " ")
        word = display_word(sec_word, word, display)
        print()
        print(" ".join(word))
        if guesses(sec_word, display) == 0 and incorrect.find(display) == -1:
            attempts -= 1
            incorrect += display + ' '
    if attempts == 0:
        print('You lost! The word was', sec_word)
    else:
        print('You guessed the word!')

main()
