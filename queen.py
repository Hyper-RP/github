def print_solution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        print_solution(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solve_n_queens_util(board, 0, n)

if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    solve_n_queens(n)
