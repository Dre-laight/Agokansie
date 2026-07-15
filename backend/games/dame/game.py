# from games.base_game import BaseGame
# import random

# from games.dame.engine import (
#     minimax,
#     RED,
#     WHITE
# )

# from games.dame.vision import DameVision


# class DameGame(BaseGame):

#     def __init__(self):

#         super().__init__("dame")

#         # =========================
#         # CORE COMPONENTS
#         # =========================
#         self.vision = DameVision()
#         self.board_state = None
#         self.search_depth = 4

#     # =====================================================
#     # REQUIRED: VISION
#     # =====================================================
#     def scan_board(self, frame):

#         board = self.vision.scan_board(frame)

#         self.board_state = board

#         return board

#     # =====================================================
#     # REQUIRED: AI
#     # =====================================================
#     def get_best_move(self, board_state):

#         score, new_engine = minimax(
#             self._wrap_board(board_state),
#             self.search_depth,
#             True
#         )

#         move = self._find_move(board_state, new_engine.board)

#         return {
#             "from": move["from"],
#             "to": move["to"]
#         }

#     # =====================================================
#     # REQUIRED: APPLY MOVE
#     # =====================================================
#     def apply_move(self, move):

#         if not self.validate_move(move):
#             raise ValueError("Invalid move")

#         start = move["from"]
#         end = move["to"]

#         piece = self.board_state[start[0]][start[1]]

#         # move piece
#         self.board_state[start[0]][start[1]] = 0
#         self.board_state[end[0]][end[1]] = piece

#         return True

#     # =====================================================
#     # REQUIRED: GAME OVER CHECK
#     # =====================================================
#     def is_game_over(self):

#         if self.board_state is None:
#             return False

#         red_exists = any(RED in row for row in self.board_state)
#         white_exists = any(WHITE in row for row in self.board_state)

#         return not (red_exists and white_exists)

#     # =====================================================
#     # REQUIRED: VALIDATION
#     # =====================================================
#     def validate_move(self, move):

#         if not move:
#             return False

#         if "from" not in move or "to" not in move:
#             return False

#         start = move["from"]
#         end = move["to"]

#         if start is None or end is None:
#             return False

#         # bounds check
#         for x in start + end:
#             if x < 0 or x > 7:
#                 return False

#         return True

#     # =====================================================
#     # REQUIRED: COORDINATE MAPPING
#     # =====================================================
#     def map_to_coordinates(self, location):

#         # Vision already returns grid coords (row, col)
#         return location

#     # =====================================================
#     # STATE
#     # =====================================================
#     def get_state(self):

#         return {
#             "game": self.name,
#             "board": self.board_state,
#             "ratings":random.randint(0,1),

#             "game_over": self.is_game_over()
#         }

#     # =====================================================
#     # WRAP FOR MINIMAX
#     # =====================================================
#     def _wrap_board(self, board_state):

#         class Wrapper:
#             def __init__(self, board):
#                 self.board = board

#         return Wrapper(board_state)

#     # =====================================================
#     # MOVE DETECTION
#     # =====================================================
#     def _find_move(self, old_board, new_board):

#         start = None
#         end = None

#         for r in range(8):
#             for c in range(8):

#                 old_piece = old_board[r][c]
#                 new_piece = new_board[r][c]

#                 if old_piece != 0 and new_piece == 0:
#                     start = (r, c)

#                 if old_piece == 0 and new_piece != 0:
#                     end = (r, c)

#         if start is None or end is None:
#             raise ValueError("Could not detect move")

#         return {
#             "from": start,
#             "to": end
#         }
    
#     def detect_human_move(self, scanned_board):
#         move = self.find_move_from_board(scanned_board)

#         if move is None:
#             return None

#         return move
    
    
#     def find_move_from_board(self, scanned_board):
#         """
#         Compare the previous board with a newly scanned board
#         and determine the player's move.
#         """

#         if self.board_state is None:
#             self.board_state = scanned_board
#             return None

#         old_board = self.board_state

#         start = None
#         end = None

#         for r in range(8):
#             for c in range(8):

#                 old_piece = old_board[r][c]
#                 new_piece = scanned_board[r][c]

#                 # Piece moved away
#                 if old_piece != 0 and new_piece == 0:
#                     start = (r, c)

#                 # Piece arrived here
#                 elif old_piece == 0 and new_piece != 0:
#                     end = (r, c)

#                 # Promotion or king change
#                 elif (
#                     old_piece != 0
#                     and new_piece != 0
#                     and old_piece != new_piece
#                 ):
#                     end = (r, c)

#         if start is None or end is None:
#             return None

#         move = {
#             "from": start,
#             "to": end
#         }

#         # Update stored board
#         self.board_state = scanned_board

#         return move
#     # =====================================================
#     # ROBOT MOVE
#     # =====================================================
#     def get_robot_move(self, board_state):

#         move = self.get_best_move(board_state)

#         return {
#     "type": "dame_action",
#     "action": "move",
#     "data": {
#         "from": move["from"],
#         "to": move["to"]
#     }
# }

#     # =====================================================
#     # RESET
#     # =====================================================
#     def reset(self):

#         self.board_state = None




from games.base_game import BaseGame
import random

from games.dame.engine import (
    Dame,
    minimax,
    RED,
    WHITE
)

from games.dame.vision import DameVision



class DameGame(BaseGame):


    def __init__(self):

        super().__init__("dame")

        self.engine = Dame()

        self.vision = DameVision()

        self.board_state = self.engine.board
        # print(self.board_state)

        self.search_depth = 4



    # =====================================================
    # VISION
    # =====================================================

    def scan_board(self, frame):

        board = self.vision.scan_board(frame)

        self.board_state = board

        self.engine.load_board(board)

        return board



    # =====================================================
    # AI MOVE USING MINIMAX
    # =====================================================

    # def get_best_move(self, board_state):


    #     # Create engine board

    #     engine = Game()

    #     engine.load_board(
    #         board_state
    #     )


    #     # Run minimax

    #     score, new_engine = minimax(
    #         engine,
    #         self.search_depth,
    #         True
    #     )


    #     if new_engine is None:

    #         return None



    #     move = self._find_move(
    #         board_state,
    #         new_engine.board
    #     )


    #     return move
    
    def get_best_move(self, board_state):

        self.engine.load_board(board_state)

        score, new_engine = minimax(
            self.engine,
            self.search_depth,
            True
        )

        if new_engine is None:
            return None

        return self._find_move(
            board_state,
            new_engine.board
        )



    # =====================================================
    # APPLY MOVE
    # =====================================================

    def apply_move(self, move):


        if not self.validate_move(move):

            return False



        r1,c1 = move["from"]

        r2,c2 = move["to"]



        piece = self.board_state[r1][c1]


        self.board_state[r1][c1] = 0


        self.board_state[r2][c2] = piece



        return True



    # =====================================================
    # GAME OVER
    # =====================================================

    def is_game_over(self):


        if self.board_state is None:

            return False



        red = False
        white = False



        for row in self.board_state:

            for p in row:


                if p in [RED,11]:

                    red = True


                if p in [WHITE,22]:

                    white = True



        return not(red and white)



    # =====================================================
    # VALIDATE MOVE
    # =====================================================

    def validate_move(self,move):


        if move is None:

            return False



        if "from" not in move or "to" not in move:

            return False



        for x in move["from"] + move["to"]:


            if x < 0 or x > 7:

                return False



        return True



    # =====================================================
    # FIND MOVE FROM BOARD DIFFERENCE
    # =====================================================

    def _find_move(self,old_board,new_board):


        start = None

        end = None



        for r in range(8):

            for c in range(8):


                old = old_board[r][c]

                new = new_board[r][c]



                # piece moved away

                if old != 0 and new == 0:

                    start = (r,c)



                # piece arrived

                if old == 0 and new != 0:

                    end = (r,c)



        if start is None or end is None:

            raise Exception(
                "Cannot detect AI move"
            )



        return {

            "from":start,

            "to":end

        }



    # =====================================================
    # HUMAN MOVE DETECTION
    # =====================================================

    def detect_human_move(self, scanned_board):

        return self.find_move_from_board(
            scanned_board
        )



    def find_move_from_board(self,new_board):


        if self.board_state is None:

            self.board_state = new_board

            return None



        old = self.board_state


        start=None

        end=None



        for r in range(8):

            for c in range(8):


                before = old[r][c]

                after = new_board[r][c]



                if before != 0 and after == 0:

                    start=(r,c)



                elif before == 0 and after !=0:

                    end=(r,c)



        if start is None or end is None:

            return None



        self.board_state = new_board



        return {

            "from":start,

            "to":end

        }



    # =====================================================
    # ROBOT COMMAND
    # =====================================================

    def get_robot_move(self,board_state):


        move = self.get_best_move(
            board_state
        )



        if move is None:

            return None



        return {


            "type":"dame_action",


            "action":"move",


            "data":{

                "from":move["from"],

                "to":move["to"]

            }

        }



    # =====================================================
    # STATE
    # =====================================================

    def get_state(self):

        print(self.board_state)
        return {

            "game":self.name,

            "board":self.board_state,

            "rating":random.randint(0,1),

            "game_over":self.is_game_over()

        }

        # =====================================================
    # COORDINATE MAPPING
    # =====================================================

    def map_to_coordinates(self, location):

        # Dame already uses row,col coordinates
        return location

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):
        # print("RESET CALLED")

        self.board_state=self.engine.board