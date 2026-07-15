import cv2
import json
import numpy as np
from pathlib import Path


class AchiVision:

    def __init__(self):

        self.debug_enabled = True

        self.cell_radius = 35

        self.calibration = self.load_calibration()

        self.red_lower1 = np.array([0, 100, 80])
        self.red_upper1 = np.array([10, 255, 255])

        self.red_lower2 = np.array([170, 100, 80])
        self.red_upper2 = np.array([180, 255, 255])

    # =====================================================
    # CALIBRATION
    # =====================================================

    def load_calibration(self):

        path = Path("games/achi/calibration.json")

        if not path.exists():

            return {
                "cells": {
                    "0": [100, 100],
                    "1": [200, 100],
                    "2": [300, 100],

                    "3": [100, 200],
                    "4": [200, 200],
                    "5": [300, 200],

                    "6": [100, 300],
                    "7": [200, 300],
                    "8": [300, 300]
                }
            }

        with open(path, "r") as f:
            return json.load(f)

    # =====================================================
    # MAIN SCAN
    # =====================================================

    def scan_board(self, frame):

        board = []

        for i in range(9):

            x, y = self.calibration["cells"][str(i)]

            state = self.detect_cell(
                frame,
                x,
                y
            )

            board.append(state)

        if self.debug_enabled:
            self.save_debug(frame, board)

        return board
    def detect_board(self, frame):

        return self.scan_board(frame)
    # =====================================================
    # CELL DETECTION
    # =====================================================

    def detect_cell(self, frame, x, y):

        r = self.cell_radius

        h, w = frame.shape[:2]

        x1 = max(0, x - r)
        y1 = max(0, y - r)

        x2 = min(w, x + r)
        y2 = min(h, y + r)

        roi = frame[y1:y2, x1:x2]

        if roi.size == 0:
            return 0

        return self.classify_piece(roi)

    # =====================================================
    # CLASSIFICATION
    # =====================================================

    def classify_piece(self, roi):

        hsv = cv2.cvtColor(
            roi,
            cv2.COLOR_BGR2HSV
        )

        # -------------------------
        # RED DETECTION
        # -------------------------

        red_mask1 = cv2.inRange(
            hsv,
            self.red_lower1,
            self.red_upper1
        )

        red_mask2 = cv2.inRange(
            hsv,
            self.red_lower2,
            self.red_upper2
        )

        red_mask = cv2.bitwise_or(
            red_mask1,
            red_mask2
        )

        red_pixels = cv2.countNonZero(
            red_mask
        )

        # -------------------------
        # BLACK DETECTION
        # -------------------------

        gray = cv2.cvtColor(
            roi,
            cv2.COLOR_BGR2GRAY
        )

        black_pixels = np.sum(
            gray < 60
        )

        area = roi.shape[0] * roi.shape[1]

        red_ratio = red_pixels / area
        black_ratio = black_pixels / area

        # RED = HUMAN = 2
        if red_ratio > 0.20:
            return 2

        # BLACK = ROBOT = 1
        if black_ratio > 0.40:
            return 1

        return 0

    # =====================================================
    # DEBUG IMAGE
    # =====================================================

    def save_debug(self, frame, board):

        image = frame.copy()

        for i in range(9):

            x, y = self.calibration["cells"][str(i)]

            cv2.circle(
                image,
                (x, y),
                self.cell_radius,
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                str(board[i]),
                (x - 10, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

        cv2.imwrite(
            "games/achi/debug_board.png",
            image
        )

    # =====================================================
    # LIVE TEST
    # =====================================================

    def test_camera(self):

        cap = cv2.VideoCapture(0)

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            board = self.scan_board(frame)

            cv2.imshow(
                "Achi Vision",
                frame
            )

            print(board)

            key = cv2.waitKey(1)

            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()