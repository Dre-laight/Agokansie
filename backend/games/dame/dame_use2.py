

# import pygame

# # ================= GAME ENGINE =================
# class Game:
#     def __init__(self):
#         self.board = self.create_board()
#         self.turn = 1  # 1 = RED (human), 2 = WHITE (AI)

#     def create_board(self):
#         return [
#             [1, 0, 1, 0, 1, 0, 1, 0],
#             [0, 1, 0, 1, 0, 1, 0, 1],
#             [1, 0, 1, 0, 1, 0, 1, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 2, 0, 2, 0, 2, 0, 2],
#             [2, 0, 2, 0, 2, 0, 2, 0],
#             [0, 2, 0, 2, 0, 2, 0, 2],
#         ]

#     # ---------------- KING PROMOTION ----------------
#     def promote(self):
#         for c in range(8):
#             if self.board[0][c] == 2:
#                 self.board[0][c] = 22
#             if self.board[7][c] == 1:
#                 self.board[7][c] = 11

#     # ---------------- WIN ----------------
#     def winner(self):
#         red = any(p in [1, 11] for row in self.board for p in row)
#         white = any(p in [2, 22] for row in self.board for p in row)

#         if not red:
#             return "WHITE"
#         if not white:
#             return "RED"
#         return None

#     # ---------------- MOVE VALIDATION ----------------
#     def valid_move(self, r1, c1, r2, c2):
#         if not (0 <= r2 < 8 and 0 <= c2 < 8):
#             return False

#         if self.board[r2][c2] != 0:
#             return False

#         piece = self.board[r1][c1]

#         is_king = piece in [11, 22]

#         # normal movement direction (non-king)
#         if piece == 1 and not is_king and r2 <= r1:
#             return False
#         if piece == 2 and not is_king and r2 >= r1:
#             return False

#         # ---------------- NORMAL MOVE ----------------
#         if abs(r2 - r1) == 1 and abs(c2 - c1) == 1:
#             return True

#         # ---------------- CAPTURE (FORWARD + BACKWARD) ----------------
#         if abs(r2 - r1) == 2 and abs(c2 - c1) == 2:
#             mid_r = (r1 + r2) // 2
#             mid_c = (c1 + c2) // 2
#             middle = self.board[mid_r][mid_c]

#             if piece in [1, 11] and middle in [2, 22]:
#                 return True
#             if piece in [2, 22] and middle in [1, 11]:
#                 return True

#         return False

#     # ---------------- CAPTURE DETECTION ----------------
#     def get_capture_moves(self, player):
#         moves = []

#         for r1 in range(8):
#             for c1 in range(8):
#                 if self.board[r1][c1] in [player, player + 10]:

#                     for r2 in range(8):
#                         for c2 in range(8):

#                             if abs(r2 - r1) == 2 and abs(c2 - c1) == 2:
#                                 if self.valid_move(r1, c1, r2, c2):
#                                     moves.append((r1, c1, r2, c2))

#         return moves

#     # ---------------- MOVE ----------------
#     def move(self, r1, c1, r2, c2):
#         piece = self.board[r1][c1]

#         self.board[r1][c1] = 0
#         self.board[r2][c2] = piece

#         # capture remove
#         if abs(r2 - r1) == 2:
#             mid_r = (r1 + r2) // 2
#             mid_c = (c1 + c2) // 2
#             self.board[mid_r][mid_c] = 0

#         self.promote()
#         self.turn = 2 if self.turn == 1 else 1


# # ================= AI =================
# def ai_move(game):
#     captures = game.get_capture_moves(2)

#     # MUST capture if available
#     if captures:
#         return captures[0]

#     moves = []

#     for r1 in range(8):
#         for c1 in range(8):
#             if game.board[r1][c1] in [2, 22]:
#                 for r2 in range(8):
#                     for c2 in range(8):
#                         if game.valid_move(r1, c1, r2, c2):
#                             moves.append((r1, c1, r2, c2))

#     return moves[0] if moves else None


# # ================= PYGAME UI =================
# WIDTH, HEIGHT = 600, 600
# SQ = WIDTH // 8

# RED = (200, 50, 50)
# WHITE = (240, 240, 240)
# KING = (255, 215, 0)
# BLACK = (30, 30, 30)
# BROWN = (139, 69, 19)


# class App:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("🇬🇭 Ghana Dame (Full Rules)")
#         self.clock = pygame.time.Clock()

#         self.game = Game()
#         self.selected = None

#     def draw_board(self):
#         for r in range(8):
#             for c in range(8):
#                 color = BROWN if (r + c) % 2 == 0 else BLACK
#                 pygame.draw.rect(self.screen, color, (c * SQ, r * SQ, SQ, SQ))

#     def draw_pieces(self):
#         for r in range(8):
#             for c in range(8):
#                 p = self.game.board[r][c]

#                 if p in [1, 11]:
#                     pygame.draw.circle(self.screen, RED, (c * SQ + 37, r * SQ + 37), 25)

#                 elif p in [2, 22]:
#                     pygame.draw.circle(self.screen, WHITE, (c * SQ + 37, r * SQ + 37), 25)

#                 # KING MARK
#                 if p in [11, 22]:
#                     pygame.draw.circle(self.screen, KING, (c * SQ + 37, r * SQ + 37), 10)

#     def get_pos(self, pos):
#         x, y = pos
#         return y // SQ, x // SQ

#     # ================= MAIN LOOP =================
#     def run(self):
#         running = True

#         while running:
#             self.clock.tick(60)

#             self.draw_board()
#             self.draw_pieces()

#             winner = self.game.winner()
#             if winner:
#                 print(winner, "wins!")
#                 pygame.time.delay(2000)
#                 running = False

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False

#                 # ---------------- HUMAN TURN ----------------
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if self.game.turn == 1:
#                         r, c = self.get_pos(pygame.mouse.get_pos())

#                         captures = self.game.get_capture_moves(1)

#                         if self.selected:
#                             r1, c1 = self.selected

#                             # FORCE CAPTURE RULE
#                             if captures:
#                                 if (r1, c1, r, c) in captures:
#                                     self.game.move(r1, c1, r, c)
#                             else:
#                                 if self.game.valid_move(r1, c1, r, c):
#                                     self.game.move(r1, c1, r, c)

#                             self.selected = None
#                         else:
#                             if self.game.board[r][c] in [1, 11]:
#                                 self.selected = (r, c)

#             # ---------------- AI TURN ----------------
#             if self.game.turn == 2:
#                 pygame.time.delay(300)

#                 move = ai_move(self.game)
#                 if move:
#                     r1, c1, r2, c2 = move
#                     self.game.move(r1, c1, r2, c2)

#             pygame.display.flip()

#         pygame.quit()


# if __name__ == "__main__":
#     App().run()










import pygame

# ================= GAME ENGINE =================

class Game:

    def __init__(self):
        self.board = self.create_board()
        self.turn = 1


    def create_board(self):

        return [
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0]*8,
            [0]*8,
            [0,2,0,2,0,2,0,2],
            [2,0,2,0,2,0,2,0],
            [0,2,0,2,0,2,0,2],
        ]


    def promote(self):

        for c in range(8):

            if self.board[0][c] == 2:
                self.board[0][c] = 22

            if self.board[7][c] == 1:
                self.board[7][c] = 11



    def winner(self):

        red = any(
            p in [1,11]
            for row in self.board
            for p in row
        )

        white = any(
            p in [2,22]
            for row in self.board
            for p in row
        )


        if not red:
            return "WHITE"

        if not white:
            return "RED"

        return None



    def valid_move(self,r1,c1,r2,c2):

        if not (0<=r2<8 and 0<=c2<8):
            return False


        if self.board[r2][c2] != 0:
            return False


        piece = self.board[r1][c1]

        king = piece in [11,22]


        if piece == 1 and not king and r2 <= r1:
            return False


        if piece == 2 and not king and r2 >= r1:
            return False



        # normal move

        if abs(r2-r1)==1 and abs(c2-c1)==1:
            return True



        # capture

        if abs(r2-r1)==2 and abs(c2-c1)==2:

            mr = (r1+r2)//2
            mc = (c1+c2)//2

            middle = self.board[mr][mc]


            if piece in [1,11] and middle in [2,22]:
                return True


            if piece in [2,22] and middle in [1,11]:
                return True


        return False



    def get_capture_moves(self,player):

        moves=[]


        for r1 in range(8):
            for c1 in range(8):

                if self.board[r1][c1] in [player,player+10]:

                    for r2 in range(8):
                        for c2 in range(8):

                            if abs(r2-r1)==2 and abs(c2-c1)==2:

                                if self.valid_move(r1,c1,r2,c2):
                                    moves.append(
                                        (r1,c1,r2,c2)
                                    )

        return moves



    def move(self,r1,c1,r2,c2):

        piece=self.board[r1][c1]


        self.board[r1][c1]=0
        self.board[r2][c2]=piece



        if abs(r2-r1)==2:

            mr=(r1+r2)//2
            mc=(c1+c2)//2

            self.board[mr][mc]=0



        self.promote()


        self.turn = 2 if self.turn==1 else 1





# ================= AI =================


def ai_move(game):

    captures = game.get_capture_moves(2)


    if captures:
        return captures[0]


    moves=[]


    for r1 in range(8):
        for c1 in range(8):

            if game.board[r1][c1] in [2,22]:

                for r2 in range(8):
                    for c2 in range(8):

                        if game.valid_move(r1,c1,r2,c2):

                            moves.append(
                                (r1,c1,r2,c2)
                            )


    return moves[0] if moves else None





# ================= PYGAME =================


WIDTH = 600
HEIGHT = 600

SQ = WIDTH//8



RED=(200,50,50)
WHITE=(240,240,240)

BLACK=(40,40,40)
BROWN=(150,100,50)

KING=(255,215,0)

GREEN=(50,220,80)
BLUE=(50,150,255)
ORANGE=(255,150,0)





class App:


    def __init__(self):

        pygame.init()


        self.screen = pygame.display.set_mode(
            (WIDTH,HEIGHT)
        )


        pygame.display.set_caption(
            "Ghana Dame"
        )


        self.clock=pygame.time.Clock()


        self.game=Game()


        self.selected=None


        self.last_move=None


        self.font=pygame.font.SysFont(
            None,
            28
        )


        self.human_wins=0
        self.ai_wins=0



    def count_piece(self,player):

        total=0

        for row in self.game.board:

            for p in row:

                if p in [player,player+10]:
                    total+=1


        return total



    def count_kings(self,player):

        total=0

        for row in self.game.board:

            for p in row:

                if p==player+10:
                    total+=1


        return total
    
    
    def draw_board(self):

        for r in range(8):
            for c in range(8):

                color = (
                    BROWN
                    if (r+c)%2==0
                    else BLACK
                )


                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        c*SQ,
                        r*SQ,
                        SQ,
                        SQ
                    )
                )



    def draw_last_move(self):

        if self.last_move:

            for r,c in self.last_move:

                pygame.draw.rect(
                    self.screen,
                    BLUE,
                    (
                        c*SQ,
                        r*SQ,
                        SQ,
                        SQ
                    ),
                    4
                )




    def draw_possible_moves(self):

        if self.selected is None:
            return


        r1,c1=self.selected


        captures=self.game.get_capture_moves(1)



        for r in range(8):

            for c in range(8):


                if captures:


                    if (r1,c1,r,c) in captures:

                        pygame.draw.circle(
                            self.screen,
                            ORANGE,
                            (
                                c*SQ+SQ//2,
                                r*SQ+SQ//2
                            ),
                            8
                        )


                else:


                    if self.game.valid_move(
                        r1,c1,r,c
                    ):

                        pygame.draw.circle(
                            self.screen,
                            GREEN,
                            (
                                c*SQ+SQ//2,
                                r*SQ+SQ//2
                            ),
                            8
                        )





    def draw_pieces(self):

        for r in range(8):

            for c in range(8):

                p=self.game.board[r][c]


                x=c*SQ+SQ//2
                y=r*SQ+SQ//2



                if p in [1,11]:

                    pygame.draw.circle(
                        self.screen,
                        RED,
                        (x,y),
                        25
                    )


                elif p in [2,22]:

                    pygame.draw.circle(
                        self.screen,
                        WHITE,
                        (x,y),
                        25
                    )



                # selected piece

                if self.selected==(r,c):

                    pygame.draw.circle(
                        self.screen,
                        GREEN,
                        (x,y),
                        32,
                        4
                    )



                # king

                if p in [11,22]:

                    txt=self.font.render(
                        "K",
                        True,
                        KING
                    )

                    rect=txt.get_rect(
                        center=(x,y)
                    )

                    self.screen.blit(
                        txt,
                        rect
                    )






    def draw_info(self):


        human=self.count_piece(1)
        ai=self.count_piece(2)


        lines=[

            "GHANA DAME",

            "",

            f"Turn: {'Human' if self.game.turn==1 else 'AI'}",

            "",

            f"Human Wins: {self.human_wins}",

            f"AI Wins: {self.ai_wins}",

            "",

            f"Red Pieces: {human}",

            f"White Pieces: {ai}",

            "",

            f"Red Kings: {self.count_kings(1)}",

            f"White Kings: {self.count_kings(2)}",

        ]



        y=10


        for line in lines:

            img=self.font.render(
                line,
                True,
                WHITE
            )


            self.screen.blit(
                img,
                (10,y)
            )

            y+=30



        if self.game.get_capture_moves(1):

            img=self.font.render(
                "CAPTURE REQUIRED!",
                True,
                ORANGE
            )


            self.screen.blit(
                img,
                (10,y+10)
            )






    def get_pos(self,pos):

        x,y=pos

        return (
            y//SQ,
            x//SQ
        )





    def restart(self):

        self.game=Game()

        self.selected=None

        self.last_move=None





    def run(self):

        running=True



        while running:


            self.clock.tick(60)



            self.screen.fill(
                (20,20,20)
            )



            self.draw_board()

            self.draw_last_move()

            self.draw_possible_moves()

            self.draw_pieces()

            self.draw_info()



            winner=self.game.winner()



            if winner:


                if winner=="RED":
                    self.human_wins+=1

                else:
                    self.ai_wins+=1



                print(
                    winner,
                    "wins"
                )


                pygame.time.delay(1500)

                self.restart()




            for event in pygame.event.get():



                if event.type==pygame.QUIT:

                    running=False




                if event.type==pygame.KEYDOWN:


                    if event.key==pygame.K_r:

                        self.restart()






                if event.type==pygame.MOUSEBUTTONDOWN:


                    if self.game.turn==1:


                        r,c=self.get_pos(
                            pygame.mouse.get_pos()
                        )



                        captures=self.game.get_capture_moves(1)




                        if self.selected:


                            r1,c1=self.selected



                            valid=False



                            if captures:


                                if (r1,c1,r,c) in captures:

                                    valid=True



                            else:


                                if self.game.valid_move(
                                    r1,c1,r,c
                                ):

                                    valid=True





                            if valid:


                                self.game.move(
                                    r1,c1,r,c
                                )


                                self.last_move=[
                                    (r1,c1),
                                    (r,c)
                                ]



                            self.selected=None





                        else:


                            if self.game.board[r][c] in [1,11]:

                                self.selected=(r,c)






            # AI TURN


            if self.game.turn==2 and not winner:


                pygame.time.delay(300)


                move=ai_move(
                    self.game
                )



                if move:

                    r1,c1,r2,c2=move


                    self.game.move(
                        r1,c1,r2,c2
                    )


                    self.last_move=[
                        (r1,c1),
                        (r2,c2)
                    ]





            pygame.display.flip()




        pygame.quit()





if __name__=="__main__":

    App().run()