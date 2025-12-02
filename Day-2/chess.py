import math
import copy

EMPTY = '.'
BLACK = 'b'
WHITE = 'w'

def create_board():
    board = [[EMPTY] * 8 for _ in range(8)]
    for r in range(3):
        for c in range(8):
            if (r + c) % 2 == 1:
                board[r][c] = WHITE
    for r in range(5, 8):
        for c in range(8):
            if (r + c) % 2 == 1:
                board[r][c] = BLACK
    return board

def print_board(board):
    print("\n  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, *row)
    print()

def get_moves(board, player):
    directions = [(-1, -1), (-1, 1)] if player == BLACK else [(1, -1), (1, 1)]
    opponent = WHITE if player == BLACK else BLACK
    moves = []
    capture_moves = []

    for r in range(8):
        for c in range(8):
            if board[r][c] == player:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == EMPTY:
                        moves.append(((r, c), (nr, nc)))
                    # capture
                    nr2, nc2 = r + 2 * dr, c + 2 * dc
                    if (0 <= nr2 < 8 and 0 <= nc2 < 8 and
                        board[nr][nc] == opponent and board[nr2][nc2] == EMPTY):
                        capture_moves.append(((r, c), (nr2, nc2)))
    return capture_moves if capture_moves else moves

def apply_move(board, move):
    (sr, sc), (er, ec) = move
    new_board = copy.deepcopy(board)
    player = new_board[sr][sc]
    new_board[sr][sc] = EMPTY
    new_board[er][ec] = player

    # Handle capture
    if abs(sr - er) == 2:
        new_board[(sr + er) // 2][(sc + ec) // 2] = EMPTY

    return new_board

def evaluate(board):
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)
    return black_count - white_count  # positive = black advantage

def minimax(board, depth, alpha, beta, maximizing, player):
    opponent = WHITE if player == BLACK else BLACK
    moves = get_moves(board, player)

    if depth == 0 or not moves:
        return evaluate(board), None

    best_move = None

    if maximizing:
        max_eval = -math.inf
        for move in moves:
            board_copy = apply_move(board, move)
            eval_score, _ = minimax(board_copy, depth - 1, alpha, beta, False, opponent)
            if eval_score > max_eval:
                max_eval, best_move = eval_score, move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move

    else:
        min_eval = math.inf
        for move in moves:
            board_copy = apply_move(board, move)
            eval_score, _ = minimax(board_copy, depth - 1, alpha, beta, True, opponent)
            if eval_score < min_eval:
                min_eval, best_move = eval_score, move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def check_winner(board):
    if not get_moves(board, BLACK):
        return WHITE
    if not get_moves(board, WHITE):
        return BLACK
    return None

def play_game():
    board = create_board()
    current_player = BLACK
    mode = int(input("Enter 1 for Human vs AI, 2 for AI vs AI: "))

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Winner is: {'BLACK' if winner == BLACK else 'WHITE'}")
            break

        moves = get_moves(board, current_player)
        if not moves:
            print(f"No moves available. Winner: {('WHITE' if current_player == BLACK else 'BLACK')}")
            break

        print(f"{current_player.upper()}'s turn")

        if mode == 1 and current_player == BLACK:
            print("Possible moves:", moves)
            m = int(input("Select move index: "))
            move = moves[m]
        else:
            print("AI thinking...")
            _, move = minimax(board, 4, -math.inf, math.inf, True, current_player)

        board = apply_move(board, move)
        current_player = WHITE if current_player == BLACK else BLACK

play_game()
