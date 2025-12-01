# Function to check if placing a queen is safe
def is_safe(board, row, col):
    # Check left side of the row
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper diagonal on left side
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check lower diagonal on left side
    r, c = row, col
    while r < 8 and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True

# Backtracking function to place queens
def solve(board, col):
    if col == 8:  # All queens placed
        return True

    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen

            if solve(board, col + 1):  # Recur to place next queen
                return True

            board[row][col] = 0  # Backtrack

    return False

# Main program to initialize board and solve
def solve_eight_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]

    if solve(board, 0):
        print("Solution Found:\n")
        for row in board:
            print(row)
    else:
        print("No solution exists")

# Run the program
solve_eight_queens()
