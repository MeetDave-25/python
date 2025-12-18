import random

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i*3 + j], "|", end=" ")
        print()
        print("-------------")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cols
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return all(cell in ['X', 'O'] for cell in board)

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board):
    possible_moves = [i for i, cell in enumerate(board) if cell not in ['X', 'O']]
    return random.choice(possible_moves)

def play_game():
    board = [str(i+1) for i in range(9)]
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == 'X':
            move = get_player_move(board)
        else:
            print("Computer is thinking...")
            move = computer_move(board)
        
        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()