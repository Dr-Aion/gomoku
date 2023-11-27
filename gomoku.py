board = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["X", "X", ".", "X", "X", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."], 
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]
numeration = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

player = True

def print_board():
    print("", end = "   ")
    for num in numeration:
        print(num, end = " ")
    print()
    i = 1
    for row in board:
        if(i >= 1 and i < 10):
            print(i, end = "  ")
        else:
            print(i, end = " ")
        i = i + 1
        for slot in row:
            print(slot, end = " ")
        print()
    
def exit_game(user_input):
    if user_input.lower() == 'q':
        return True
    else: 
        return False

def check_input(user_input):
    if len(user_input) > 3:
        return False
    elif len(user_input) == 2 and not str(user_input[1]).isnumeric():
        return False
    elif len(user_input) == 3 and not str(user_input[1] + user_input[2]).isnumeric():
        return False
    elif str(user_input[0]).upper() not in numeration:
        return False
    else:
        return True
    
def coordinates(user_input):
    if len(user_input) == 2:
        row = int(user_input[1]) - 1
    else:
        row = int(user_input[1] + user_input[2]) - 1
    col = ord(user_input[0].upper()) - 65
    print("row " + str(row) + " col " + str(col))
    return (row, col)

def is_taken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != '.':
        return True
    else:
        return False
    
def add_to_board(coords, board, current_player):
    row = coords[0]
    col = coords[1]
    board[row][col] = current_player

def current_player(player):
    if player:
        return 'X'
    else:
        return 'O'

def is_winner(cur_player, board):
    if check_row(cur_player, board): return True

def check_row(cur_player, board):
    for row in board:
        count = 0
        flag = False
        for slot in row:
            if slot == cur_player and count == 0:
                count = count + 1
                flag = True
            elif slot == cur_player and flag:
                count = count + 1
                if count == 5:
                    return True
            else:
                count = 0
                flag = False
            

while True:
    curr_player = current_player(player)
    print_board()
    user_input = input("Place your stone or enter q to exit: ")
    if exit_game(user_input): 
        break
    if not check_input(user_input):
        print("Not a valid input. Try again!")
        continue
    coords = coordinates(user_input)
    if is_taken(coords, board):
        print("The slot is taken. Try again!")
        continue
    add_to_board(coords, board, curr_player)
    print_board()
    if is_winner(curr_player, board):
        print(curr_player + ", congratulations! You won!")
    print("________________________________")
    player = not player
    