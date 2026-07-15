import cv2
import numpy as np


EMPTY = 0

RED = 1
WHITE = 2

RED_KING = 11
WHITE_KING = 22

class DameVision:

    def __init__(self):
        self.board_size = 8

    # =====================================================
    # MAIN ENTRY
    # =====================================================

    def scan_board(self, frame):

        board_img = self._crop_board(frame)

        squares = self._split_board(board_img)

        return self._classify_board(squares)
    def detect_board(self, frame):

        return self.scan_board(frame)
    # =====================================================
    # STEP 1: ISOLATE BOARD
    # =====================================================

    def _crop_board(self, frame):

        h, w = frame.shape[:2]

        size = min(h, w)

        x = (w - size) // 2
        y = (h - size) // 2

        return frame[y:y+size, x:x+size]

    # =====================================================
    # STEP 2: SPLIT INTO 64 SQUARES
    # =====================================================

    def _split_board(self, board_img):

        size = board_img.shape[0]
        cell = size // 8

        squares = []

        for r in range(8):

            row = []

            for c in range(8):

                square = board_img[
                    r*cell:(r+1)*cell,
                    c*cell:(c+1)*cell
                ]

                row.append(square)

            squares.append(row)

        return squares

    # =====================================================
    # STEP 3: CLASSIFY PIECE
    # =====================================================

    def _detect_piece(self, square):

        hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)

        # RED MASK
        red1 = cv2.inRange(hsv, (0, 80, 80), (10, 255, 255))
        red2 = cv2.inRange(hsv, (170, 80, 80), (180, 255, 255))
        red_mask = red1 + red2

        red_score = cv2.countNonZero(red_mask)

        # WHITE MASK (bright pieces)
        white_mask = cv2.inRange(hsv, (0, 0, 160), (180, 60, 255))
        white_score = cv2.countNonZero(white_mask)

        # thresholds (you will tune later)
        if red_score > 400:
            return 1

        if white_score > 400:
            return 2

        return EMPTY

    # =====================================================
    # STEP 4: BUILD BOARD
    # =====================================================

    def _classify_board(self, squares):

        board = []

        for r in range(8):

            row = []

            for c in range(8):

                piece = self._detect_piece(squares[r][c])

                row.append(piece)

            board.append(row)

        return board