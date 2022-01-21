# Tic Tac Toe - Human vs AI
import random

board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' ', }


def print_board():
    print(f"{board[7]}|{board[8]}|{board[9]}          7|8|9")
    print(f"-----          -----")
    print(f"{board[4]}|{board[5]}|{board[6]}          4|5|6")
    print(f"-----          -----")
    print(f"{board[1]}|{board[2]}|{board[3]}          1|2|3")


def check_move(move):
    if board[move] == ' ':
        return True
    else:
        return False


def ai_move():
    move = random.randint(1, 9)
    check_move(move)
    if check_move(move):
        board[move] = 'O'
        return
    else:
        ai_move()


def check_for_win():
    # Parse through board to check for winner
    if board[7] != ' ' and board[7] == board[8] and board[7] == board[9]:
        winner = board[7]
    else:
        pass


def check_for_tie():
    pass


def main():
    while True:
        print_board()
        while True:
            move = int(input("\nPick a number to place your move.> "))
            if check_move(move):
                board[move] = 'X'
                break
            else:
                print("That move is taken, try again.\n")
        ai_move()


if __name__ == '__main__':
    main()
