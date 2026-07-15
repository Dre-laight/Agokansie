class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
        ]
    def winner(self):
        red_exists = False
        white_exists = False

        for row in self.board:
            for cell in row:
                if cell == 1:
                    red_exists = True
                elif cell == 2:
                    white_exists = True

        if not red_exists:
            return "WHITE"
        if not white_exists:
            return "RED"