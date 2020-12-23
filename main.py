## This is the main code of tic-tok game

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board):
    # check row
    if board[0] == board[1] == board[2] != "-":
        return True
    elif board[3] == board[4] == board[5] != "-":
        return True
    elif board[6] == board[7] == board[8] != "-":
        return True
    
    # check column
    if board[0] == board[3] == board[6] != "-":
        return True
    elif board[1] == board[4] == board[7] != "-":
        return True
    elif board[2] == board[5] == board[8] != "-":
        return True

    # check diagonal
    if board[0] == board[4] == board[8] != "-":
        return True
    elif board[2] == board[4] == board[6] != "-":
        return True

def check_gameover(board):
    if "-" not in board:
        return True

player1 = input("Please enter the name of player 1: ")
player2 = input("Please enter the name of player 2: ")
count_player = 0

while True:
    # set current player
    if count_player % 2 == 0:
        current_player = player1
        current_symbol = "O"
    else:
        current_player = player2
        current_symbol = "X"

    position = input(current_player + ", Please choose a position between 0-8: ")

    if position not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        print("invalid position")
        continue
    
    position = int(position)
    if board[position] == "-":
        board[position] = current_symbol
    else:
        print("The position is occupied already, please choose another position")
        continue
    print_board(board)
    
    if check_win(board) == True:
        print("Congratulation " + current_player + ", you win the game!")
        break
    if check_gameover(board) == True:
        print("Draw Game!")
        break
    
    count_player += 1