import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_win(board, player):
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    # Check if any winning combination is satisfied
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(spot != ' ' for spot in board)

# Function for a player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid move. Please choose a number between 1 and 9.")

# Function for computer's move (simple random AI)
def computer_move(board, player):
    print("Computer's turn...")
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = player
            break

# Main function to run the game
def tic_tac_toe():
    board = [' '] * 9  # Initialize an empty board with 9 spaces
    current_player = 'X'  # Player 'X' always starts
    
    # Ask the user if they want to play against the computer or another player
    opponent = input("Do you want to play against the computer? (yes/no): ").lower()
    vs_computer = opponent == 'yes'
    
    # Game loop
    while True:
        display_board(board)  # Display the board
        
        # Handle player moves
        if current_player == 'X' or not vs_computer:
            player_move(board, current_player)
        else:
            computer_move(board, current_player)
        
        # Check if the current player has won
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
tic_tac_toe()
