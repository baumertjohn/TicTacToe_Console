# Tic Tac Toe - Human vs AI
import random

board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' ', }


def print_board():
    print(f"{board[7]}|{board[8]}|{board[9]}     7|8|9")
    print(f"-----     -----")
    print(f"{board[4]}|{board[5]}|{board[6]}     4|5|6")
    print(f"-----     -----")
    print(f"{board[1]}|{board[2]}|{board[3]}     1|2|3")


def check_move(move):
    try:
        if board[int(move)] == ' ':
            return True
        else:
            print("That move is taken, try again.")
            return False
    except KeyError:
        print("Pick a number between 1 and 9")
    except ValueError:
        print("Pick an integer")
    print_board()


def ai_move(turn):
    if turn == 4:
        return False
    ai_choice = True
    while ai_choice:
        move = random.randint(1, 9)
        if board[move] == ' ':
            board[move] = 'O'
            return True


def check_for_win():
    # Parse through board to check for winner
    if board[7] != ' ' and board[7] == board[8] and board[7] == board[9]:
        print(f"The winner is {board[7]}.")
        return True
    if board[4] != ' ' and board[4] == board[5] and board[4] == board[6]:
        print(f"The winner is {board[4]}.")
        return True
    if board[1] != ' ' and board[1] == board[2] and board[1] == board[3]:
        print(f"The winner is {board[1]}.")
        return True
    if board[7] != ' ' and board[7] == board[4] and board[7] == board[1]:
        print(f"The winner is {board[7]}.")
        return True
    if board[8] != ' ' and board[8] == board[5] and board[8] == board[2]:
        print(f"The winner is {board[8]}.")
        return True
    if board[9] != ' ' and board[9] == board[6] and board[9] == board[3]:
        print(f"The winner is {board[9]}.")
        return True
    if board[7] != ' ' and board[7] == board[5] and board[7] == board[3]:
        print(f"The winner is {board[7]}.")
        return True
    if board[1] != ' ' and board[1] == board[5] and board[1] == board[9]:
        print(f"The winner is {board[1]}.")
        return True


def main():
    running = True
    turn = 0
    while running:
        print_board()
        # Get player 1 move
        while True:
            move = input("\nPick a number to place your move> ")
            if check_move(move):
                board[int(move)] = 'X'
                break
        # Check if player 1 has won
        if check_for_win():
            print_board()
            break
        # Make AI move
        if not ai_move(turn):
            print("DRAW")
            print_board()
            break
        # Check if AI has won
        if check_for_win():
            print_board()
            break
        turn += 1


if __name__ == '__main__':
    main()
