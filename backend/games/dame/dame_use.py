# from dame_board import Board
# from dame_engine import minimax

# # =========================
# # GAME CONTROLLER
# # =========================
# class Game:
#     def __init__(self):
#         self.board = Board()
#         self.turn = "RED"

#     def play_ai_turn(self):
#         value, new_board = minimax(self.board, 3, True)
#         self.board = new_board
#         self.switch_turn()

#     def play_move(self, piece, move):
#         valid_moves = self.board.get_valid_moves(piece)

#         if move in valid_moves:
#             self.board.move(piece, move[0], move[1], valid_moves[move])
#             self.switch_turn()
#             return True

#         return False

#     def switch_turn(self):
#         self.turn = "WHITE" if self.turn == "RED" else "RED"

#     def is_game_over(self):
#         return self.board.winner() is not None


# # =========================
# # SIMPLE LOOP (NO UI)
# # =========================
# def print_board(board):
#     symbols = {
#         0: ".",
#         1: "R",
#         2: "W",
#         3: "RK",
#         4: "WK"
#     }

#     print("\n  0 1 2 3 4 5 6 7")
#     print(" +-----------------")

#     for i, row in enumerate(board.board):
#         print(i, "|", end=" ")

#         for cell in row:
#             print(symbols.get(cell, "?"), end=" ")

#         print()

#     print()
    
# def main():
#     game = Game()

#     while not game.is_game_over():

#         print_board(game.board)

#         print("Current turn:", game.turn)

#         if game.turn == "WHITE":
#             print("AI thinking...")
#             value, new_board = minimax(game.board, 3, True)
#             game.board = new_board
#             game.switch_turn()
#             print("AI moved")

#         else:
#             print("RED turn (manual input required)")
#             break  # for now (later we can add input or robot control)

#     print_board(game.board)
#     print("Game Over!")


# main()
board=[4]*12
print(board)