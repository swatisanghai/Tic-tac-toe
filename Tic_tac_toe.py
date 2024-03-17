def print_board(board):
    # Print each row of the board
    for row in board:
        # Join the elements of the row with '|' and print
        print(" | ".join(row))
        # Print a line of dashes for separation
        print("-" * 12)

def check_winner(board):
    # Check rows for a winner
    for row in board:
        # If all elements in the row are the same and not empty
        if row[0] == row[1] == row[2] and row[0] != ' ':
            # Return the symbol of the winner
            return row[0]

    # Check columns for a winner
    for col in range(3):
        # If all elements in the column are the same and not empty
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            # Return the symbol of the winner
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        # Return the symbol of the winner
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        # Return the symbol of the winner
        return board[0][2]

    # If there is no winner, return None
    return None

def is_full(board):
    # Check if the board is full
    for row in board:
        # If there is an empty cell, the board is not full
        if ' ' in row:
            return False
    # If no empty cells are found, the board is full
    return True

def main():
    # Initialize the empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    # Start the game with player 'X'
    current_player = 'X'

    # Print the welcome message and the initial board
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    # Game loop
    while True:
        # Get row and column input from the current player
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        # Check if the chosen position is already taken
        if board[row][col] != ' ':
            print("That position is already taken. Try again.")
            continue

        # Place the current player's symbol on the board
        board[row][col] = current_player
        # Print the updated board
        print_board(board)

        # Check if there is a winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        # If the board is full and there is no winner, it's a draw
        elif is_full(board):
            print("It's a draw!")
            break

        # Switch to the other player for the next turn
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
