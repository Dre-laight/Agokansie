import pygame

from engine import (
    Game,
    RED,
    WHITE,
    minimax
)


pygame.init()


WIDTH = 800
HEIGHT = 800

ROWS = 8
COLS = 8

SQUARE = WIDTH // COLS


WIN = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Checkers AI"
)



# Colors

BLACK = (0,0,0)

WHITE_COLOR = (240,240,240)

RED_COLOR = (220,50,50)

BLUE_COLOR = (50,50,220)

GREEN = (50,200,50)





class CheckersGUI:


    def __init__(self):

        self.game = Game()

        self.turn = RED

        self.selected = None

        self.valid_moves = {}


        # game over variables

        self.game_over = False

        self.winner = None




    # ---------------------------------
    # DRAW BOARD
    # ---------------------------------

    def draw_board(self):

        for row in range(ROWS):

            for col in range(COLS):

                if (row+col)%2 == 0:

                    color = WHITE_COLOR

                else:

                    color = BLACK


                pygame.draw.rect(
                    WIN,
                    color,
                    (
                        col*SQUARE,
                        row*SQUARE,
                        SQUARE,
                        SQUARE
                    )
                )





    # ---------------------------------
    # DRAW PIECES
    # ---------------------------------

    def draw_pieces(self):

        for row in range(ROWS):

            for col in range(COLS):


                value = self.game.board[row][col]


                if value != 0:


                    center = (
                        col*SQUARE + SQUARE//2,
                        row*SQUARE + SQUARE//2
                    )


                    if value == RED:

                        color = RED_COLOR

                    else:

                        color = BLUE_COLOR



                    pygame.draw.circle(
                        WIN,
                        color,
                        center,
                        SQUARE//2-10
                    )





    # ---------------------------------
    # HIGHLIGHT MOVES
    # ---------------------------------

    def draw_moves(self):

        for move in self.valid_moves:

            row,col = move


            pygame.draw.circle(
                WIN,
                GREEN,
                (
                    col*SQUARE + SQUARE//2,
                    row*SQUARE + SQUARE//2
                ),
                15
            )





    # ---------------------------------
    # GAME OVER CHECK
    # ---------------------------------

    def check_game_over(self):

        winner = self.game.get_winner()


        if winner:

            self.game_over = True

            self.winner = winner





    # ---------------------------------
    # DRAW GAME OVER
    # ---------------------------------

    def draw_game_over(self):

        font = pygame.font.SysFont(
            None,
            80
        )


        if self.winner == RED:

            text = "RED WINS"

        else:

            text = "Blue WINS"



        surface = font.render(
            text,
            True,
            GREEN
        )


        rect = surface.get_rect(
            center=(
                WIDTH//2,
                HEIGHT//2
            )
        )


        WIN.blit(
            surface,
            rect
        )






    # ---------------------------------
    # MOUSE CLICK
    # ---------------------------------

    def click(self,pos):


        # stop input after game over

        if self.game_over:

            return



        x,y = pos


        row = y//SQUARE

        col = x//SQUARE




        # selecting piece

        if self.selected is None:



            piece = self.game.get_piece(
                row,
                col
            )


            if piece and piece.color == self.turn:


                self.selected = piece


                self.valid_moves = (
                    self.game.get_valid_moves(
                        piece
                    )
                )





        else:


            destination = (
                row,
                col
            )


            if destination in self.valid_moves:


                skips = self.valid_moves[destination]


                self.game.move_piece(
                    self.selected,
                    row,
                    col
                )



                for piece in skips:


                    self.game.remove_piece(
                        piece.row,
                        piece.col
                    )



                self.game.promote()



                # check human win

                self.check_game_over()



                if self.game_over:

                    return



                self.turn = WHITE



                # AI move

                self.ai_move()



            self.selected = None

            self.valid_moves = {}







    # ---------------------------------
    # AI
    # ---------------------------------

    def ai_move(self):


        if self.game_over:

            return



        score,move = minimax(
            self.game,
            3,
            True
        )



        if move:


            self.game = move



        # check AI win

        self.check_game_over()



        if not self.game_over:

            self.turn = RED







    # ---------------------------------
    # DRAW
    # ---------------------------------

    def draw(self):


        self.draw_board()

        self.draw_moves()

        self.draw_pieces()



        if self.game_over:

            self.draw_game_over()



        pygame.display.update()







# =====================================

gui = CheckersGUI()


running = True



while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            running = False




        if event.type == pygame.MOUSEBUTTONDOWN:


            if gui.turn == RED:

                gui.click(
                    pygame.mouse.get_pos()
                )



    gui.draw()





pygame.quit()