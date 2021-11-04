"""
Name: Eric Beaver
lab10.py
"""


def main():
    play_game()


def build_board():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_list


def display_board(board):
    print("{0} | {1} | {2}".format(board[0], board[1], board[2]))
    print("--------")
    print("{0} | {1} | {2}".format(board[3], board[4], board[5]))
    print("--------")
    print("{0} | {1} | {2}".format(board[6], board[7], board[8]))
    print("--------")


def fill_spot(board, pos, char):
    if (char == 'o' or char == 'x') and is_legal(board, pos):
        board[pos - 1] = char
    else:
        return


def is_legal(board, pos):
    if pos > 9 or type(board[pos - 1]) != int:
        return False
    return True


def game_won(board, char):
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    if board[0] == char and board[3] == char and board[6] == char:
        return True
    if board[3] == char and board[4] == char and board[5] == char:
        return True
    if board[1] == char and board[4] == char and board[7] == char:
        return True
    if board[6] == char and board[7] == char and board[8] == char:
        return True
    if board[2] == char and board[5] == char and board[8] == char:
        return True
    if board[0] == char and board[4] == char and board[8] == char:
        return True
    if board[6] == char and board[4] == char and board[2] == char:
        return True
    return False


def game_over(board):
    acc = 0
    for i in board:
        if type(i) == int:
            acc += 1
    if (game_won(board, 'x') or game_won(board, 'o')) or acc == 0:
        return True
    return False


def play_game():
    p1_char = input("Player 1, pick x or o: ")
    p1 = 1
    p2_char = input("Player 2, pick the character that Player 1 did not choose: ")
    p2 = 2
    board_num = build_board()
    i = 1
    display_board(board_num)
    while not game_over(board_num):
        if i == 1:
            pos = input("Player " + str(p1) + ", enter the position: ")
            if is_legal(board_num, int(pos)):
                fill_spot(board_num, int(pos), p1_char)
            display_board(board_num)
            if game_won(board_num, p1_char):
                print('Player 1 wins!')
        if i == 2:
            pos = input("Player " + str(p2) + ", enter the position: ")
            if is_legal(board_num, int(pos)):
                fill_spot(board_num, int(pos), p2_char)
            display_board(board_num)
            if game_won(board_num, p2_char):
                print('Player 2 wins!')
        i += 1
        if i > 2:
            i = 1
    if not game_won(board_num, p1_char) and not game_won(board_num, p2_char):
        print("It's a Tie!")


main()
