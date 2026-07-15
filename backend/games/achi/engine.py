class TapatanEngine:
    def __init__(self):
        self.adj = {
            0: [1,3,4],
            1: [0,2,4],
            2: [1,4,5],
            3: [0,4,6],
            4: [0,1,2,3,5,6,7,8],
            5: [2,4,8],
            6: [3,4,7],
            7: [4,6,8],
            8: [4,5,7]
        }
        self.board = [0] * 9


        self.win_sets = [
            {0,1,2}, {3,4,5}, {6,7,8},
            {0,3,6}, {1,4,7}, {2,5,8},
            {0,4,8}, {2,4,6}
        ]

    # ---------- GAME STATE ----------
    def winner(self, board):
        for combo in self.win_sets:
            vals = [board[i] for i in combo]
            if vals == [1,1,1]:
                return 1
            if vals == [2,2,2]:
                return 2
        return 0

    def count_pieces(self, board):
        return board.count(1), board.count(2)

    def get_phase(self, board):
        p1, p2 = self.count_pieces(board)
        if p1 < 3 or p2 < 3:
            return "placement"
        return "movement"

    # ---------- MOVES ----------
    def get_moves(self, board, player):
        phase = self.get_phase(board)
        moves = []

        if phase == "placement":
            for i in range(9):
                if board[i] == 0:
                    moves.append(("place", i))
        else:
            for src in range(9):
                if board[src] == player:
                    for dest in self.adj[src]:
                        if board[dest] == 0:
                            moves.append(("move", src, dest))

        return moves

    # ---------- APPLY MOVE ----------
    def apply_move(self, board, move, player):
        new_board = board[:]

        if move[0] == "place":
            _, pos = move
            new_board[pos] = player

        else:
            _, src, dest = move
            new_board[dest] = new_board[src]
            new_board[src] = 0

        return new_board

    # ---------- EVALUATION ----------
    def evaluate(self, board):
        w = self.winner(board)
        if w == 1:
            return 1000
        if w == 2:
            return -1000

        # small heuristic
        score = 0
        for i in range(9):
            if board[i] == 1:
                score += 1
                if i == 4:
                    score += 2
            elif board[i] == 2:
                score -= 1
                if i == 4:
                    score -= 2

        return score

    # ---------- MINIMAX ----------
    def minimax(self, board, depth, maximizing):
        w = self.winner(board)
        if depth == 0 or w != 0:
            return self.evaluate(board), None

        player = 1 if maximizing else 2
        best_move = None

        moves = self.get_moves(board, player)

        if not moves:
            return self.evaluate(board), None

        if maximizing:
            best_score = -9999
            for move in moves:
                new_board = self.apply_move(board, move, player)
                score, _ = self.minimax(new_board, depth-1, False)

                if score > best_score:
                    best_score = score
                    best_move = move

            return best_score, best_move

        else:
            best_score = 9999
            for move in moves:
                new_board = self.apply_move(board, move, player)
                score, _ = self.minimax(new_board, depth-1, True)

                if score < best_score:
                    best_score = score
                    best_move = move

            return best_score, best_move
    def is_valid_move(self, board, move, player):
        phase = self.get_phase(board)
        
        if move is None:
            return False

        if not isinstance(move, tuple):
            return False

        if len(move) == 0:
            return False

        if move[0] == "place":
            if phase != "placement":
                return False

            _, pos = move

            # must be empty
            if board[pos] != 0:
                return False

            # max 3 pieces
            p1, p2 = self.count_pieces(board)
            if player == 1 and p1 >= 3:
                return False
            if player == 2 and p2 >= 3:
                return False

            return True

        elif move[0] == "move":
            if phase != "movement":
                return False

            _, src, dest = move

            # must own the piece
            if board[src] != player:
                return False

            # dest must be empty
            if board[dest] != 0:
                return False

            # must be adjacent
            if dest not in self.adj[src]:
                return False

            return True

        return False

    # ---------- PUBLIC API ----------
    def best_move(self, board, player, depth=4):
        maximizing = (player == 1)
        _, move = self.minimax(board, depth, maximizing)
        return move