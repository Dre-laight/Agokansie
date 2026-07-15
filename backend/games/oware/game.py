import copy,random
from games.base_game import BaseGame

from games.oware.engine import (
    Oware,
    minimax
)

from games.oware.vision import OwareVision


class OwareGame(BaseGame):

    def __init__(self):

        super().__init__("oware")

        self.engine = Oware()

        self.vision = OwareVision()

        self.search_depth = 2
        self.human_select=None

    # =====================================================
    # VISION
    # =====================================================

    def scan_board(self):

        """
        Uses camera vision.

        Returns:
            [4,4,4,4,4,4,4,4,4,4,4,4]
        """

        board = self.vision.scan_board()
        # board=[4,4,4,4,4,4,4,4]

        self.engine.board = board

        self.board_state = board

        return board
    

    def find_user_move(self, scanned_board):

        current_board = self.engine.board
        current_player = self.engine.current_player

        # Determine which pits belong to the current player
        # if current_player == 1:
        #     pits = range(0, 6)
        # else:
        #     pits = range(6, 12)
        pits = range(0, 6)
        matches = []

        for pit in pits:

            # Skip empty pits
            if current_board[pit] == 0:
                continue

            # Make a deep copy of the engine
            test_engine = copy.deepcopy(self.engine)

            try:
                # Simulate the move
                test_engine.play_move(pit)

                # Check if the result matches what the camera saw
                if test_engine.board == scanned_board:
                    matches.append(pit)

            except Exception as e:
                print(f"Simulation failed for pit {pit}: {e}")

        # No matching move
        if len(matches) == 0:
            return None

        # Exactly one matching move
        if len(matches) == 1:
            return matches[0]

        # Multiple matches (should be rare)
        raise ValueError(f"Multiple possible moves found: {matches}")   
# human move 
    def play_human_move(self, pit):

        if not self.engine.is_valid_move(pit):
            raise ValueError(f"Invalid move: pit {pit}")

        result = self.engine.play_move(pit)

        self.board_state = self.engine.board

        return result
    
    # OwareGame
    def detect_human_move(self, scanned_board):
        pit = self.find_user_move(scanned_board)

        if pit is None:
            return self.human_select
        

        return {
            "type": "pit",
            "pit": pit
        }
    # =====================================================
    # AI
    # =====================================================

    def get_best_move(self, board_state):

        self.engine.board = board_state

        score, move = minimax(
            self.engine,
            self.search_depth,
            float("-inf"),
            float("inf"),
            True
        )

        if move is None:
            raise ValueError("Minimax returned None (no valid moves)")

        return {"pit": move}

    # =====================================================
    # RULES
    # =====================================================

    def validate_move(self, move):

        pit = move["pit"]

        return self.engine.is_valid_move(pit)

    def apply_move(self, move):

        pit = move["pit"]

        result = self.engine.play_move(pit)

        self.board_state = self.engine.board

        return result

    # =====================================================
    # GAME OVER
    # =====================================================

    def is_game_over(self):

        return self.engine.game_over()

    def finalize_game(self):

        self.engine.finalize_game()

    # =====================================================
    # SCORES
    # =====================================================
    # def get_sow_path(self, pit):

    #     board = self.engine.board   # ✅ FIX HERE

    #     path = []
    #     seeds = board[pit]
    #     print("the seeds are ")
    #     print(seeds)
    #     index = pit

    #     while seeds > 0:
    #         index = (index + 1) % 12

    #         path.append(index)
    #         seeds -= 1

    #     return path
    
    
    def get_sow_path(self, pit):

        result = self.engine.make_move(pit)   # ✅ FIX HERE
        path=result["sow_path"]
        
        print("the seeds are ")
        return path
    def get_captures(self, pit):

        result = self.engine.make_move(pit)   # ✅ FIX HERE
        captures=result["captures"]
        
        print("the seeds are ")
        return captures
    def get_moves(self, pit):

        result = self.engine.make_move(pit)   # ✅ FIX HERE
        moves=result["moves"]
        
        print("the seeds are ")
        return moves
    def get_scores(self):

        return {
            "player": self.engine.scores[0],
            "robot": self.engine.scores[1]
        }

    # =====================================================
    # STATE
    # =====================================================

    def get_state(self):

        return {
            "game": self.name,

            "board": self.engine.board,

            "scores": {
                "player": self.engine.scores[0],
                "robot": self.engine.scores[1]
            },
            "ratings":random.randint(0,1),

            "current_player":
                self.engine.current_player,

            "game_over":
                self.engine.game_over()
        }

    # =====================================================
    # ROBOT COORDINATES
    # =====================================================

    def map_to_coordinates(self, pit):

        pit_map = {

            6: (15, 20),
            7: (70, 20),
            8: (120, 20),
            9: (180, 20),
            10: (230, 20),
            11: (290, 20),

            0: (290, 80),
            1: (230, 80),
            2: (180, 80),
            3: (120, 80),
            4: (70, 80),
            5: (15, 80)
        }

        return pit_map[pit]

    # =====================================================
    # SPECIAL ROBOT MOVE FOR OWARE
    # =====================================================

    def get_robot_move(self, board_state):

        ai_move = self.get_best_move(board_state)

        # return {
        #     "type": "oware_action",
        #     "action": "sow",
        #     "data": {
        #         "pit": ai_move["pit"],
        #         "sow_path": self.get_sow_path(ai_move["pit"]),
        #         "captures":self.get_captures(ai_move["pit"])
        #     }
        # }
        return {
            "type": "oware_action",
            "action": "sow",
            "data": {
                "pit": ai_move["pit"],
                "moves": self.get_moves(ai_move["pit"]),
                
            }
        }

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.engine = Oware()

        self.board_state = self.engine.board 