def initialize_board():
    """Create an empty 3x3 Tic-Tac-Toe board."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    """Display the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def get_player_move():
    """Get the player's move (row and column)."""
    try:
        row, col = map(int, input("Enter row and column numbers (1-3): ").split())
        return row - 1, col - 1
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")
        return get_player_move()

def is_valid_move(board, row, col):
    """Check if the move is valid (empty cell)."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, player, row, col):
    """Make the player's move on the board."""
    board[row][col] = player

def check_winner(board, player):
    """Check if the player has won."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player

def is_board_full(board):
    """Check if the board is full (tie)."""
    return all(all(cell != ' ' for cell in row) for row in board)

def play_tic_tac_toe():
    current_player = 'X'
    game_board = initialize_board()

    while True:
        display_board(game_board)
        print(f"Player {current_player}'s turn.")
        move = get_player_move()

        if is_valid_move(game_board, *move):
            make_move(game_board, current_player, *move)

            if check_winner(game_board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(game_board):
                print("The game ends in a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
