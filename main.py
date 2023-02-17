import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winning = None
game_running = False


def printing_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# printing_board(board)


def user_input(board):
    inp = int(input("Enter your place: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = current_player
    elif board[inp - 1] != "-":
        print("The place is already taken by user")


def checking_hor(board):
    global winning
    if board[0] == board[1] == board[2] and board[1] != "-":
        winning = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winning = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winning = board[6]
        return True


def checking_ver(board):
    global winning
    if board[0] == board[3] == board[6] and board[3] != "-":
        winning = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winning = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winning = board[5]
        return True


def checking_dia(board):
    global winning
    if board[0] == board[4] == board[8] and board[0] != "-":
        winning = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winning = board[4]
        return True


def switch_play():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_win():
    global game_running
    if checking_ver(board) or checking_dia(board) or checking_hor(board):
        print(f"The winner is {winning}")
        game_running = True

def check_tie(board):
    global game_running
    if "-" not in board:
        print("It's tie")
        game_running = True

def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_play()

printing_board(board)
while not game_running:
    user_input(board)
    printing_board(board)
    check_win()
    check_tie(board)
    switch_play()
    computer(board)
    check_win()
    check_tie(board)

