from string import ascii_lowercase

class Board:
    def __init__(self, boardSize = 15):
        self.boardSize = boardSize
        #board = [["."] * size] * size
        self.boardMatrix = [["." for i in range(boardSize)] for j in range(boardSize)]

    def __str__(self):
        boardMatrixString = ""
        boardMatrixString += "   "
        for c in ascii_lowercase[:self.boardSize]:
            boardMatrixString += c + " "
        boardMatrixString += "\n"
        i = 1
        for row in self.boardMatrix:
            if(i >= 1 and i < 10):
                boardMatrixString += str(i) + "  "
            else:
                boardMatrixString += str(i) + " "
            i = i + 1
            for slot in row:
                boardMatrixString += slot + " "
            boardMatrixString += "\n"
        return boardMatrixString

        

def get_board_size():
    while True:
        try:
            return int(input("What's the size of the board? "))
        except ValueError:
            pass

size = get_board_size()
board = Board(size)

player = True
    
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
    elif str(user_input[0]).upper() not in ascii_lowercase:
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
    print(board)
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
    print(board)
    if is_winner(curr_player, board):
        print(curr_player + ", congratulations! You won!")
    print("________________________________")
    player = not player
    