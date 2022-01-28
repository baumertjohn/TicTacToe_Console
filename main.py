# Tic Tac Toe - Human vs AI or Human vs Human
import random

board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' ', }


def print_board():
    # Print the game board
    print("Game       Key")
    print(f"{board[7]}|{board[8]}|{board[9]}     7|8|9")
    print(f"-----     -----")
    print(f"{board[4]}|{board[5]}|{board[6]}     4|5|6")
    print(f"-----     -----")
    print(f"{board[1]}|{board[2]}|{board[3]}     1|2|3")


def check_move(move):
    # Check if human player has valid choice and move
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
    # Check if AI can move or if game is draw
    if turn == 9:
        return False
    while True:
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
    while True:
        # Choose game - Human vs AI or Human vs Human
        players = input("Press '1' for Player vs. AI or "
                        "'2' for Player vs. Player> ")
        if players == '1':
            players = 1
            break
        elif players == '2':
            players = 2
            break
        else:
            print("Please choose '1' or '2'.")
    turn_count = 0
    while True:  # Start game loop
        print_board()
        # Check if 2 player game is at draw
        if turn_count == 9:
            print("     DRAW")
            break
        # Get player move
        while True:
            move = input("\nPick a number to place your move> ")
            if check_move(move):
                if turn_count % 2 == 0:
                    board[int(move)] = 'X'  # Player 1 move
                else:
                    board[int(move)] = 'O'  # Player 2 move if two player game
                break
        # Check if player has won
        if check_for_win():
            print_board()
            break
        turn_count += 1
        # Check if one player game and make AI move.
        if players == 1:
            if not ai_move(turn_count):
                print_board()
                print("     DRAW")
                break
            # Check if AI has won
            if check_for_win():
                print_board()
                break
            turn_count += 1


if __name__ == '__main__':
    main()
