from copy import deepcopy

RED = "RED"
WHITE = "WHITE"


# =========================
# MINIMAX (PURE ENGINE)
# =========================
def minimax(position, depth, max_player):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None

        for move in get_all_moves(position, WHITE):
            evaluation = minimax(move, depth - 1, False)[0]

            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None

        for move in get_all_moves(position, RED):
            evaluation = minimax(move, depth - 1, True)[0]

            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move

        return min_eval, best_move


# =========================
# MOVE GENERATION
# =========================
def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)

        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)

            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves


# =========================
# SIMULATE MOVE
# =========================
def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])

    if skip:
        board.remove(skip)

    return board