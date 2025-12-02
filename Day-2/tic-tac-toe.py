import math

# Create the board
board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" ", board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("---+---+---")
    print("\n")

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def winner(board, player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),  # Rows
        (0,3,6),(1,4,7),(2,5,8),  # Columns
        (0,4,8),(2,4,6)           # Diagonals
    ]
    return any(board[a] == player and board[b] == player and board[c] == player
               for a,b,c in win_positions)

def minimax(board, depth, maximizing):
    if winner(board, 'O'):  # AI wins
        return 1, None
    elif winner(board, 'X'):  # Human wins
        return -1, None
    elif not available_moves(board):
        return 0, None

    if maximizing:
        best_score = -math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = 'O'
            score, _ = minimax(board, depth+1, False)
            board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = 'X'
            score, _ = minimax(board, depth+1, True)
            board[move] = ' '
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def play_game():
    print("TIC TAC TOE GAME (Human = X, AI = O)\n")
    print_board()

    while True:
        # Human Move
        human_move = int(input("Enter position (0-8): "))
        if board[human_move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[human_move] = 'X'
        print_board()

        if winner(board, 'X'):
            print("🎉 Human Wins!")
            break
        if not available_moves(board):
            print("It's a Draw!")
            break

        # AI Move
        print("AI thinking...")
        _, ai_move = minimax(board, 0, True)
        board[ai_move] = 'O'
        print_board()

        if winner(board, 'O'):
            print("🤖 AI Wins!")
            break
        if not available_moves(board):
            print("It's a Draw!")
            break

play_game()
