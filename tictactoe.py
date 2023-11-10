import random

board = [" " for _ in range(9)]
human = "X"
computer = "O"

def print_board(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))

def is_full(board):
    return " " not in board

def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(board, depth, is_maximizing):
    if check_win(board, computer):
        return 1
    if check_win(board, human):
        return -1
    if is_full(board):
        return 0
    if is_maximizing:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = computer
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(eval, max_eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = human
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(eval, min_eval)
        return min_eval

def computer_move(board):
    best_move = None
    best_score = float("-inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = computer
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = computer

while True:
    print_board(board)
    
    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move] == " ":
            board[move] = human
            break
    
    if check_win(board, human):
        print_board(board)
        print("You win!")
        break
 
    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break
 
    computer_move(board)
 
    if check_win(board, computer):
        print_board(board)
        print("You lose!")
        break
   
    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break

