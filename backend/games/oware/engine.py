



import copy

class Oware:
    def __init__(self):
        self.board = [4] * 12
        self.scores = [0, 0]
        self.current_player = 2

    def clone(self):
        return copy.deepcopy(self)

    # ---------------------------------------------------
    # HELPERS
    # ---------------------------------------------------

    def player_range(self, player):
        return range(0, 6) if player == 1 else range(6, 12)

    def opponent_range(self, player):
        return range(6, 12) if player == 1 else range(0, 6)

    def opponent(self, player):
        return 2 if player == 1 else 1

    # ---------------------------------------------------
    # VALID MOVES
    # ---------------------------------------------------

    def is_valid_move(self, pit):
        if pit not in self.player_range(self.current_player):
            return False

        if self.board[pit] == 0:
            return False

        # starvation rule
        opponent_side = self.opponent_range(self.current_player)

        if sum(self.board[i] for i in opponent_side) == 0:
            temp = self.clone()
            temp.make_move(pit)

            if sum(temp.board[i] for i in opponent_side) == 0:
                return False

        return True

    def valid_moves(self):
        return [p for p in self.player_range(self.current_player)
                if self.is_valid_move(p)]

    # ---------------------------------------------------
    # MAIN MOVE LOGIC
    # ---------------------------------------------------

    def play_move(self, pit):
        if not self.is_valid_move(pit):
            return None

        result = self.make_move(pit)

        # self.current_player = self.opponent(self.current_player)

        return result
    def play_move2(self, pit):
        if not self.is_valid_move(pit):
            return None

        result = self.make_move2(pit)

        self.current_player = self.opponent(self.current_player)

        return result

    def make_move_for_test(self, pit):

        result = {
            "sow_path": [],
            "captures": []
        }

        current_player = self.current_player

        current = pit

        while True:

            seeds = self.board[current]
            self.board[current] = 0

            pos = current

            # -----------------------------
            # SOWING
            # -----------------------------
            while seeds > 0:

                pos = (pos + 1) % 12

                if pos == current:
                    continue

                self.board[pos] += 1
                result["sow_path"].append(pos)

                seeds -= 1

                # -----------------------------------
                # GLOBAL 4-SEED CAPTURE CHECK
                # happens immediately during sowing
                # -----------------------------------

                owner = 1 if pos < 6 else 2

                if self.board[pos] == 4:

                    # last-seed override handled later
                    if pos == result["sow_path"][-1] and seeds == 0:
                        continue

                    # normal capture
                    self.scores[owner - 1] += 4
                    self.board[pos] = 0
                    result["captures"].append(pos)

            # -----------------------------
            # LAST SEED RULE (OVERRIDE)
            # -----------------------------
            last = pos

            owner = 1 if last < 6 else 2

            if self.board[last] == 4:

                # ONLY active player captures last seed result
                self.scores[current_player - 1] += 4

                self.board[last] = 0

                result["captures"].append(last)

            # -----------------------------
            # RELAY RULE
            # -----------------------------
            if self.board[last] > 1:
                current = last
            else:
                break

        return result  
    
    def make_move(self, pit):

        result = {
            "moves": []
        }

        current_player = self.current_player
        current = pit

        while True:

            seeds = self.board[current]
            self.board[current] = 0

            pos = current

            # -----------------------------
            # SOWING
            # -----------------------------
            while seeds > 0:

                pos = (pos + 1) % 12

                # Skip the pit we picked from
                if pos == current:
                    continue

                self.board[pos] += 1

                # Record a sow move
                result["moves"].append({
                    "type": "sow",
                    "from": current,
                    "to": pos
                })

                seeds -= 1

                owner = 1 if pos < 6 else 2

                # Immediate 4-seed capture
                if self.board[pos] == 4:

                    # Don't handle the last seed here
                    if seeds == 0:
                        continue

                    # Add 4 capture moves
                    for _ in range(4):
                        result["moves"].append({
                            "type": "capture",
                            "from": pos,
                            "owner": owner
                        })

                    self.scores[owner - 1] += 4
                    self.board[pos] = 0

            # -----------------------------
            # LAST SEED RULE
            # -----------------------------
            last = pos
            owner = 1 if last < 6 else 2

            if self.board[last] == 4:

                # Add 4 capture moves
                for _ in range(4):
                    result["moves"].append({
                        "type": "capture",
                        "from": last,
                        "owner": owner
                    })

                self.scores[current_player - 1] += 4
                self.board[last] = 0

            # -----------------------------
            # RELAY RULE
            # -----------------------------
            if self.board[last] > 1:
                current = last
            else:
                break

        return result
    # ---------------------------------------------------
  
    def make_move2(self, pit):

        result = {
            "sow_path": [],
            "captures": []
        }

        current_player = self.current_player
        current = pit

        # SAFETY AGAINST INFINITE RELAYS
        relay_count = 0
        visited = set()

        while True:

            relay_count += 1

            if relay_count > 100:
                raise RuntimeError(
                    "Infinite relay detected (relay_count > 100)"
                )

            if current in visited:
                raise RuntimeError(
                    f"Relay loop detected at pit {current}"
                )

            visited.add(current)

            print("\n====================")
            print("CURRENT PIT:", current)
            print("BOARD:", self.board)

            seeds = self.board[current]
            self.board[current] = 0

            pos = current

            # -----------------------------
            # SOWING
            # -----------------------------
            while seeds > 0:

                pos = (pos + 1) % 12

                if pos == current:
                    continue

                self.board[pos] += 1

                result["sow_path"].append(pos)

                seeds -= 1

                owner = 1 if pos < 6 else 2

                if self.board[pos] == 4:

                    if seeds == 0:
                        continue

                    self.scores[owner - 1] += 4
                    self.board[pos] = 0

                    result["captures"].append(pos)

            # -----------------------------
            # LAST SEED RULE
            # -----------------------------
            last = pos

            owner = 1 if last < 6 else 2

            if self.board[last] == 4:

                self.scores[current_player - 1] += 4
                self.board[last] = 0

                result["captures"].append(last)

            print("LAST PIT:", last)
            print("SEEDS IN LAST PIT:", self.board[last])

            # -----------------------------
            # RELAY RULE
            # -----------------------------
            if self.board[last] > 1:

                print("RELAYING TO:", last)

                current = last

            else:

                print("MOVE COMPLETE")

                break

        return result
    
        # GAME OVER
        # ---------------------------------------------------

    # def game_over(self):

    #     if self.scores[0] >= 25 or self.scores[1] >= 25:
    #         return True

    #     if len(self.valid_moves()) == 0:
    #         return True

    #     return False
    
    
    def game_over(self):

        p1_side = sum(self.board[0:6])
        p2_side = sum(self.board[6:12])

        total = p1_side + p2_side

        # Case 1: one side empty
        if p1_side == 0 or p2_side == 0:
            return True

        # Case 2: exactly 4 seeds left
        if total == 4:
            return True

        return False


    def finalize_game(self):

        p1_side = sum(self.board[0:6])
        p2_side = sum(self.board[6:12])

        total = p1_side + p2_side

        # --------------------------------------------------
        # CASE 1: side empty → collect remaining seeds
        # --------------------------------------------------
        if p1_side == 0 or p2_side == 0:

            self.scores[0] += p1_side
            self.scores[1] += p2_side

            for i in range(12):
                self.board[i] = 0

        # --------------------------------------------------
        # CASE 2: exactly 4 seeds left
        # all go to starter (Player 1 in your game)
        # --------------------------------------------------
        elif total == 4:

            self.scores[0] += 4

            for i in range(12):
                self.board[i] = 0
# ======================================================
# AI EVALUATION
# ======================================================

def evaluate(game):

    ai_score = game.scores[1]
    human_score = game.scores[0]

    ai_seeds = sum(game.board[6:12])
    human_seeds = sum(game.board[0:6])

    mobility = len(game.valid_moves())

    value = 0

    value += (ai_score - human_score) * 20
    value += (ai_seeds - human_seeds) * 2
    value += mobility * 3

    # reward capture opportunities
    for i in range(6, 12):

        if game.board[i] > 0:

            test = game.clone()
            before = test.scores[1]

            test.current_player = 2
            test.play_move(i)

            gain = test.scores[1] - before

            value += gain * 8

    return value


# ======================================================
# MINIMAX + ALPHA BETA
# ======================================================

def minimax(state, depth, alpha, beta, maximizing):

    if depth == 0 or state.game_over():
        return evaluate(state), None
    #ny add
    # if not valid_moves:
    #     return 0, 0
    moves = state.valid_moves()

    if not moves:
        return evaluate(state), None

    best_move = moves[0]

    if maximizing:

        max_eval = -float("inf")

        for move in moves:

            child = state.clone()
            child.play_move(move)

            eval_score, _ = minimax(
                child,
                depth - 1,
                alpha,
                beta,
                False
            )

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move

            alpha = max(alpha, eval_score)

            if beta <= alpha:
                break

        return max_eval, best_move

    else:

        min_eval = float("inf")

        for move in moves:

            child = state.clone()
            child.play_move(move)

            eval_score, _ = minimax(
                child,
                depth - 1,
                alpha,
                beta,
                True
            )

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

            beta = min(beta, eval_score)

            if beta <= alpha:
                break

        return min_eval, best_move