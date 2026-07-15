# from games.base_game import BaseGame
# from games.achi.engine import TapatanEngine
# from games.achi.vision import AchiVision  
# import random


# class AchiGame(BaseGame):

#     def __init__(self):

#         super().__init__("achi")

#         self.engine = TapatanEngine()

#         self.vision = AchiVision()

#         # 0 = empty
#         # 1 = robot
#         # 2 = human
#         self.board_state = [0] * 9

#         self.ai_player = 1
#         self.human_player = 2

#         self.search_depth = 4

#     # =====================================================
#     # VISION
#     # =====================================================

#     def scan_board(self):

#         board = self.vision.scan_board()

#         self.board_state = board

#         return board
    
#     def detect_human_move(self, scanned_board):
#         move = self.find_move_from_board(scanned_board)

#         if move is None:
#             return None

#         return move
    
#     def find_move_from_board(self, scanned_board):
#         """
#         Compare the stored board with a newly scanned board and
#         determine the human's move.
#         """

#         if self.board_state is None:
#             self.board_state = scanned_board.copy()
#             return None

#         old_board = self.board_state

#         start = None
#         end = None

#         for i in range(9):

#             old_piece = old_board[i]
#             new_piece = scanned_board[i]

#             # Human removed a piece from here
#             if old_piece == self.human_player and new_piece == 0:
#                 start = i

#             # Human placed/moved a piece here
#             elif old_piece == 0 and new_piece == self.human_player:
#                 end = i

#         # ---------------------------
#         # Placement phase
#         # ---------------------------
#         if start is None and end is not None:

#             move = {
#                 "type": "place",
#                 "position": end
#             }

#         # ---------------------------
#         # Movement phase
#         # ---------------------------
#         elif start is not None and end is not None:

#             move = {
#                 "type": "move",
#                 "from": start,
#                 "to": end
#             }

#         else:
#             return None

#         # Update stored board
#         self.board_state = scanned_board.copy()

#         return move

#     # =====================================================
#     # AI
#     # =====================================================

#     def get_best_move(self, board_state):

#         move = self.engine.best_move(
#             board_state,
#             self.ai_player,
#             self.search_depth
#         )

#         if move is None:
#             return None

#         if move[0] == "place":

#             return {
#                 "type": "place",
#                 "position": move[1]
#             }

#         return {
#             "type": "move",
#             "from": move[1],
#             "to": move[2]
#         }

#     # =====================================================
#     # RULES
#     # =====================================================

#     def validate_move(self, move, player=None):

#         if player is None:
#             player = self.ai_player

#         if move is None:
#             return False

#         if move["type"] == "place":

#             engine_move = (
#                 "place",
#                 move["position"]
#             )

#         else:

#             engine_move = (
#                 "move",
#                 move["from"],
#                 move["to"]
#             )

#         return self.engine.is_valid_move(
#             self.board_state,
#             engine_move,
#             player
#         )

#     # =====================================================
#     # APPLY MOVE
#     # =====================================================

#     def apply_move(self, move, player=None):

#         if player is None:
#             player = self.ai_player

#         if move["type"] == "place":

#             engine_move = (
#                 "place",
#                 move["position"]
#             )

#         else:

#             engine_move = (
#                 "move",
#                 move["from"],
#                 move["to"]
#             )

#         self.board_state = self.engine.apply_move(
#             self.board_state,
#             engine_move,
#             player
#         )

#         return self.board_state

#     # =====================================================
#     # WINNER
#     # =====================================================

#     def is_game_over(self):

#         winner = self.engine.winner(
#             self.board_state
#         )

#         return winner != 0

#     def get_winner(self):

#         winner = self.engine.winner(
#             self.board_state
#         )

#         if winner == 1:
#             return "robot"

#         if winner == 2:
#             return "human"

#         return None

#     # =====================================================
#     # PHASE
#     # =====================================================

#     def get_phase(self):

#         return self.engine.get_phase(
#             self.board_state
#         )

#     # =====================================================
#     # ROBOT MOVE FORMAT
#     # =====================================================

#     def get_robot_move(self, board_state):

#         move = self.get_best_move(
#             board_state
#         )

#         return move

#     # =====================================================
#     # BOARD COORDINATES
#     # =====================================================

#     def map_to_coordinates(self, position):

#         mapping = {

#             0: (0, 0),
#             1: (50, 0),
#             2: (100, 0),

#             3: (0, 50),
#             4: (50, 50),
#             5: (100, 50),

#             6: (0, 100),
#             7: (50, 100),
#             8: (100, 100)
#         }

#         return mapping[position]

#     # =====================================================
#     # ROBOT ACTIONS
#     # =====================================================

#     def convert_to_robot_command(self, move):

#         if move["type"] == "place":

#             return {
#                 "action": "place",
#                 "destination":
#                     self.map_to_coordinates(
#                         move["position"]
#                     )
#             }

#         return {
#             "action": "move",
#             "source":
#                 self.map_to_coordinates(
#                     move["from"]
#                 ),
#             "destination":
#                 self.map_to_coordinates(
#                     move["to"]
#                 )
#         }

#     # =====================================================
#     # GAME STATE
#     # =====================================================

#     def get_state(self):

#         return {
#             "game": self.name,
#             "board": self.board_state,
#             "phase": self.get_phase(),
#             "winner": self.get_winner(),
#             "ratings":random.randint(0,1),

#             "game_over": self.is_game_over()
#         }

#     # =====================================================
#     # RESET
#     # =====================================================

#     def reset(self):

#         self.board_state = [0] * 9









from games.base_game import BaseGame

from games.achi.engine import TapatanEngine

from games.achi.vision import AchiVision

import random



class AchiGame(BaseGame):


    def __init__(self):

        super().__init__("achi")

        self.engine = TapatanEngine()

        self.vision = AchiVision()

        # Engine owns the board
        self.engine.board = [0] * 9

        self.board_state = self.engine.board

        self.ai_player = 1
        self.human_player = 2

        self.search_depth = 4



    # =====================================================
    # VISION
    # =====================================================

    def scan_board(self):

        board = self.vision.scan_board()

        self.engine.board = board
        self.board_state = board

        return board



    # =====================================================
    # HUMAN MOVE DETECTION
    # =====================================================

    def detect_human_move(self, scanned_board):

        return self.find_move_from_board(
            scanned_board
        )



    def find_move_from_board(self, scanned_board):

        """
        Compare the stored board with a newly scanned
        board and determine the human move.
        """

        if self.board_state is None:

            self.engine.board = scanned_board.copy()

            self.board_state = self.engine.board

            return None



        old_board = self.board_state

        start = None
        end = None



        for i in range(9):

            before = old_board[i]

            after = scanned_board[i]



            # Piece removed

            if before == self.human_player and after == 0:

                start = i



            # Piece placed

            elif before == 0 and after == self.human_player:

                end = i



        # -------------------
        # Placement phase
        # -------------------

        if start is None and end is not None:

            move = {

                "type": "place",

                "position": end

            }



        # -------------------
        # Movement phase
        # -------------------

        elif start is not None and end is not None:

            move = {

                "type": "move",

                "from": start,

                "to": end

            }



        else:

            return None



        self.engine.board = scanned_board.copy()

        self.board_state = self.engine.board

        return move



    # =====================================================
    # AI
    # =====================================================

    def get_best_move(self, board_state):

        self.engine.board = board_state

        self.board_state = board_state



        move = self.engine.best_move(

            self.engine.board,

            self.ai_player,

            self.search_depth

        )



        if move is None:

            return None



        if move[0] == "place":

            return {

                "type": "place",

                "position": move[1]

            }



        return {

            "type": "move",

            "from": move[1],

            "to": move[2]

        }



    # =====================================================
    # RULES
    # =====================================================

    def validate_move(self, move, player=None):

        if player is None:

            player = self.ai_player



        if move is None:

            return False



        if move["type"] == "place":

            engine_move = (

                "place",

                move["position"]

            )



        else:

            engine_move = (

                "move",

                move["from"],

                move["to"]

            )



        return self.engine.is_valid_move(

            self.engine.board,

            engine_move,

            player

        )



    # =====================================================
    # APPLY MOVE
    # =====================================================

    def apply_move(self, move, player=None):

        if player is None:

            player = self.ai_player



        if move["type"] == "place":

            engine_move = (

                "place",

                move["position"]

            )



        else:

            engine_move = (

                "move",

                move["from"],

                move["to"]

            )



        self.engine.board = self.engine.apply_move(

            self.engine.board,

            engine_move,

            player

        )



        self.board_state = self.engine.board

        return self.engine.board
    # =====================================================
    # GAME OVER
    # =====================================================

    def is_game_over(self):

        return self.engine.winner(
            self.engine.board
        ) != 0



    def get_winner(self):

        winner = self.engine.winner(
            self.engine.board
        )

        if winner == self.ai_player:

            return "robot"

        if winner == self.human_player:

            return "human"

        return None



    # =====================================================
    # PHASE
    # =====================================================

    def get_phase(self):

        return self.engine.get_phase(
            self.engine.board
        )



    # =====================================================
    # ROBOT MOVE
    # =====================================================

    def get_robot_move(self, board_state):

        move = self.get_best_move(
            board_state
        )

        return move



    # =====================================================
    # BOARD COORDINATES
    # =====================================================

    def map_to_coordinates(self, position):

        mapping = {

            0: (0, 0),
            1: (50, 0),
            2: (100, 0),

            3: (0, 50),
            4: (50, 50),
            5: (100, 50),

            6: (0, 100),
            7: (50, 100),
            8: (100, 100)

        }

        return mapping[position]



    # =====================================================
    # ROBOT COMMAND
    # =====================================================

    def convert_to_robot_command(self, move):

        if move is None:

            return None


        if move["type"] == "place":

            return {

                "action": "place",

                "destination":
                    self.map_to_coordinates(
                        move["position"]
                    )

            }


        return {

            "action": "move",

            "source":
                self.map_to_coordinates(
                    move["from"]
                ),

            "destination":
                self.map_to_coordinates(
                    move["to"]
                )

        }



    # =====================================================
    # STATE
    # =====================================================

    def get_state(self):

        return {

            "game": self.name,

            "board": self.engine.board,

            "phase": self.get_phase(),

            "winner": self.get_winner(),

            "ratings": random.randint(0, 1),

            "game_over": self.is_game_over()

        }



    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.engine = TapatanEngine()

        self.engine.board = [0] * 9

        self.board_state = self.engine.board