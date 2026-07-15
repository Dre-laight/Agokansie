# from engine import TapatanEngine

# engine = TapatanEngine()

# board = [
#     0,0,0,
#     0,0,0,
#     0,0,0
# ]

# player = 2  # AI starts

# def print_board(board):
#     print()
#     for i in range(0, 9, 3):
#         print(board[i:i+3])
#     print()

# # ---------- GAME LOOP ----------
# while True:

#     print_board(board)

#     # ---------------- AI TURN ----------------
#     if player == 1:
#         move = engine.best_move(board, player, depth=6)

#         if engine.is_valid_move(board, move, player):
#             board = engine.apply_move(board, move, player)
#             print("AI move:", move)
            
#         else:
#             print("AI made invalid move (error)")
#             break

#     # ---------------- HUMAN TURN ----------------
#     else:
#         phase = engine.get_phase(board)
#         print("Current phase:", phase)

#         if phase == "placement":
#             pos = int(input("Enter position to PLACE (0–8): "))
#             move = ("place", pos)

#         else:
#             src = int(input("Enter SOURCE (0–8): "))
#             dest = int(input("Enter DESTINATION (0–8): "))
#             move = ("move", src, dest)

#         if engine.is_valid_move(board, move, player):
#             board = engine.apply_move(board, move, player)
#             print("Human move:", move)
#         else:
#             print("Invalid move! Try again.")
#             continue
#         print(engine.winner(board))
#     # ---------------- SWITCH PLAYER ----------------
#     player = 2 if player == 1 else 1


import pygame
import sys
from engine import TapatanEngine

pygame.init()

# -----------------------------
# SETTINGS
# -----------------------------
WIDTH, HEIGHT = 600, 700
BOARD_SIZE = 600
CELL = BOARD_SIZE // 3

WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
RED = (220, 60, 60)
BLUE = (70, 120, 255)
GRAY = (180, 180, 180)
GREEN = (60, 200, 60)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tapatan")

font = pygame.font.SysFont(None, 35)

engine = TapatanEngine()

board = [0] * 9

HUMAN = 2
AI = 1

player = HUMAN

selected = None
game_over = False


# -----------------------------------
# DRAW BOARD
# -----------------------------------
def draw():

    screen.fill(WHITE)

    # Grid
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK,
                         (0, i * CELL),
                         (BOARD_SIZE, i * CELL), 3)

        pygame.draw.line(screen, BLACK,
                         (i * CELL, 0),
                         (i * CELL, BOARD_SIZE), 3)

    # Pieces
    for i in range(9):

        r = i // 3
        c = i % 3

        x = c * CELL + CELL // 2
        y = r * CELL + CELL // 2

        if board[i] == HUMAN:
            pygame.draw.circle(screen, BLUE, (x, y), 45)

        elif board[i] == AI:
            pygame.draw.circle(screen, RED, (x, y), 45)

        if selected == i:
            pygame.draw.circle(screen, GREEN, (x, y), 52, 4)

    phase = engine.get_phase(board)

    txt = font.render(
        f"Turn: {'Human' if player==HUMAN else 'AI'}   Phase: {phase}",
        True,
        BLACK,
    )
    screen.blit(txt, (20, 620))

    winner = engine.winner(board)

    if winner:
        txt = font.render(
            f"Winner: {'Human' if winner==HUMAN else 'AI'}",
            True,
            GREEN,
        )
        screen.blit(txt, (20, 655))

    pygame.display.flip()


# -----------------------------------
# MAIN LOOP
# -----------------------------------

running = True

while running:

    draw()

    winner = engine.winner(board)
    if winner:
        game_over = True

    # ---------------- AI ----------------
    if not game_over and player == AI:

        pygame.time.delay(500)

        move = engine.best_move(board, AI, depth=6)

        if engine.is_valid_move(board, move, AI):
            board = engine.apply_move(board, move, AI)

        player = HUMAN

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if game_over:
            continue

        if player != HUMAN:
            continue

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()

            if y > BOARD_SIZE:
                continue

            col = x // CELL
            row = y // CELL

            pos = row * 3 + col

            phase = engine.get_phase(board)

            # ---------------- Placement ----------------
            if phase == "placement":

                move = ("place", pos)

                if engine.is_valid_move(board, move, HUMAN):
                    board = engine.apply_move(board, move, HUMAN)
                    player = AI

            # ---------------- Movement ----------------
            else:

                if selected is None:

                    if board[pos] == HUMAN:
                        selected = pos

                else:

                    move = ("move", selected, pos)

                    if engine.is_valid_move(board, move, HUMAN):
                        board = engine.apply_move(board, move, HUMAN)
                        player = AI

                    selected = None

pygame.quit()
sys.exit()