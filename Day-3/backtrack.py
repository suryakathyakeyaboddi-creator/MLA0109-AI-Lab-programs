# Knight's Tour Problem using Backtracking

N = 8   # You can change to any NxN board size

# Utility function to check if (x, y) is inside board and not visited
def isSafe(x, y, board):
    return (0 <= x < N and 0 <= y < N and board[x][y] == -1)

# Print the board
def printSolution(board):
    for row in board:
        for cell in row:
            print(str(cell).zfill(2), end=" ")
        print()

# Recursive function to solve Knight Tour problem
def solveKT():
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # All possible moves of a knight
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2,  2,  1, -1, -2, -2, -1]

    # Knight starts at the first block
    board[0][0] = 0

    # Start recursive process
    if solveKTUtil(0, 0, 1, board, moves_x, moves_y):
        print("Knight Tour Path Found:\n")
        printSolution(board)
    else:
        print("Solution does not exist")

# Recursively solve the Knight Tour problem
def solveKTUtil(x, y, movei, board, moves_x, moves_y):
    # Base case: all squares visited
    if movei == N * N:
        return True

    # Try all next moves
    for k in range(8):
        next_x = x + moves_x[k]
        next_y = y + moves_y[k]

        if isSafe(next_x, next_y, board):
            board[next_x][next_y] = movei

            if solveKTUtil(next_x, next_y, movei + 1, board, moves_x, moves_y):
                return True

            # Backtracking
            board[next_x][next_y] = -1

    return False


# Driver Code
solveKT()
