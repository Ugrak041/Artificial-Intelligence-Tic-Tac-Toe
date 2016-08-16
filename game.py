# Arda Mavi - ardamavi.com
# Artificial Intelligence Tic Tac Toe

# Imports :
from subprocess import call
from random import randint

# Variables :
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = [board, [], []]
win = "Yet_None"
exit_game = False
order = "O"

# Functions :
def clear_screan():
    call(["clear"])

def print_board(this_board = board):
    print("\n  "+ str(this_board[0]), "|", str(this_board[1]), "|", str(this_board[2]))
    print("  - | - | -")
    print("  "+ str(this_board[3]), "|", str(this_board[4]), "|", str(this_board[5]))
    print("  - | - | -")
    print("  "+ str(this_board[6]), "|", str(this_board[7]), "|", str(this_board[8]), "\n")

def start_settings():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win = "Yet_None"
    order = "O"

def is_free(this_board, inpt):
    if this_board[inpt-1] == "X" or this_board[inpt-1] == "O":
        return False
    else:
        if int(inpt) > 0 and int(inpt) <= 9:
            return True
        else:
            return False

def who_win(this_board):
    # Horizontal
    for i in range(0,7,3):
        if (this_board[i] == 'X' and this_board[i+1] == 'X' and this_board[i+2] == 'X') or (this_board[i] == 'O' and this_board[i+1] == 'O' and this_board[i+2] == 'O'):
            return board[i+1]

    # Vertical
    for i in range(3):
        if (this_board[i] == 'X' and this_board[i+3] == 'X' and this_board[i+6] == 'X') or (this_board[i] == 'O' and this_board[i+3] == 'O' and this_board[i+6] == 'O'):
            return board[i+3]

    # Cross
    if (this_board[0] == 'X' and this_board[4] == 'X' and this_board[8] == 'X') or (this_board[0] == 'O' and this_board[4] == 'O' and this_board[8] == 'O'):
        return board[4]

    if (this_board[2] == 'X' and this_board[4] == 'X' and this_board[6] == 'X') or (this_board[2] == 'O' and this_board[4] == 'O' and this_board[6] == 'O'):
        return board[4]

    return "Yet_None"

def is_finish(this_board):
    if who_win(this_board) == "Yet_None":
        for i in range(9):
            if this_board[i] != "X" and this_board[i] != "O":
                return False
        return True
    else:
        return True

def create_children(board, turn):
    if is_finish(board):
        return []
    tree = []
    for i in range(0,9):
        board_copy = list(board)
        if board_copy[i] == "X" or board_copy[i] == "O":
            continue
        board_copy[i] = turn
        tree.append(board_copy)
    return list(tree)

def last_child(child, turn):
    if len(create_children(child, turn)) == 0:
        return True
    else:
        return False

def bf_creator(root, turn):
    tree = []
    queue = [(tree, root, turn)]
    tree.append(root)
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        children = create_children(elem[1], elem[2])
        tmp_turn = "O" if elem[2] == "X" else "X"
        for child in children:
            elem[0].append([child])
            queue.append((elem[0][-1], child, tmp_turn))
    return tree

"""def leaves(tree):
    turn = "O"
    last_children = []

    turn = "O" if turn == "X" else "X"
    if last_child(child, turn):
        last_children.append(child)

    return last_children

tree = bf_creator(['O','X','O',"O",'X','O',7 , 8, 9], 'O')
for t in tree:
    print(t)

print("\nlast_children: ")
for i in leaves(tree):
    print(i)"""

def ai_play():
    #where_ai()
    board[0] = "O"

def play_game(inpt):
        board[inpt-1] = "X"
        if who_win(board) == "Yet_None":
            play_len = 0
            for i in range(0,9):
                if board[i] == "X" or board[i] == "O":
                    play_len += 1
            if play_len <= 1:
                bf_creator(board, "O")
            ai_play()
"""
# Main :
clear_screan()
print("Artificial Intelligence Tic Tac Toe\nArda Mavi - ardamavi.com\nExit Game: 0")
start_settings()

while win == "Yet_None":
    clear_screan()
    print_board()

    while True:
        inpt = input("X's turn: ")
        if int(inpt) == 0:
            win = "None"
            break
        elif is_free(board, int(inpt)):
            play_game(int(inpt))
            win = who_win(board)
            break
        else:
            clear_screan()
            print("Try Again !")
            print_board()

clear_screan()
print_board()
print("Win: " + win)
print("Arda Mavi - ardamavi.com\nThe End !\n")
"""
