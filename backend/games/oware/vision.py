
# import cv2
# import json
# import os


# class OwareVision:

#     CALIBRATION_FILE = "games/oware/pits.json"

#     def __init__(self, camera_index=0):

#         self.camera_index = camera_index

#         self.cap = cv2.VideoCapture(camera_index)

#         self.pits = []

#         # print("=" * 50)
#         # print("OWARE VISION INITIALIZING")
#         # print("Calibration file:", self.CALIBRATION_FILE)
#         # print(
#         #     "Calibration exists:",
#         #     os.path.exists(self.CALIBRATION_FILE)
#         # )

#         if os.path.exists(self.CALIBRATION_FILE):

#             self.load_calibration()

#             # print(
#             #     f"Loaded {len(self.pits)} pits"
#             # )

#         else:

#             print(
#                 "WARNING: Calibration file not found."
#             )
#             print(
#                 "Run calibrate() first."
#             )

#         print("=" * 50)

#     # =====================================================
#     # CALIBRATION
#     # =====================================================

#     def save_calibration(self):

#         with open(
#             self.CALIBRATION_FILE,
#             "w"
#         ) as f:

#             json.dump(
#                 self.pits,
#                 f,
#                 indent=4
#             )

#         # print(
#         #     f"Saved {len(self.pits)} pits"
#         # )

#     def load_calibration(self):

#         with open(
#             self.CALIBRATION_FILE,
#             "r"
#         ) as f:

#             self.pits = json.load(f)

#         # print("Calibration loaded")

#     def calibrate(self):

#         ret, frame = self.cap.read()

#         if not ret:
#             raise RuntimeError(
#                 "Camera not found"
#             )

#         display = frame.copy()

#         self.pits = []

#         def click(
#             event,
#             x,
#             y,
#             flags,
#             param
#         ):

#             if event == cv2.EVENT_LBUTTONDOWN:

#                 self.pits.append({
#                     "x": x,
#                     "y": y,
#                     "r": 45
#                 })

#                 cv2.circle(
#                     display,
#                     (x, y),
#                     5,
#                     (0, 255, 0),
#                     -1
#                 )

#                 cv2.putText(
#                     display,
#                     str(len(self.pits) - 1),
#                     (x + 10, y),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.6,
#                     (0, 255, 0),
#                     2
#                 )

#                 # print(
#                 #     f"Pit {len(self.pits)-1}: "
#                 #     f"({x},{y})"
#                 # )

#         cv2.namedWindow(
#             "Oware Calibration"
#         )

#         cv2.setMouseCallback(
#             "Oware Calibration",
#             click
#         )

#         # print(
#         #     "Click all 12 pits."
#         # )
#         # print(
#         #     "Press Q when finished."
#         # )

#         while True:

#             cv2.imshow(
#                 "Oware Calibration",
#                 display
#             )

#             key = cv2.waitKey(1)

#             if key == ord("q"):
#                 break

#         cv2.destroyAllWindows()

#         if len(self.pits) != 12:

#             raise RuntimeError(
#                 f"Expected 12 pits, "
#                 f"got {len(self.pits)}"
#             )

#         self.save_calibration()

#     # =====================================================
#     # PIT EXTRACTION
#     # =====================================================

#     def extract_pit(
#         self,
#         frame,
#         pit
#     ):

#         x = int(pit["x"])
#         y = int(pit["y"])
#         r = int(pit["r"])

#         return frame[
#             y-r:y+r,
#             x-r:x+r
#         ]

#     # =====================================================
#     # SEED COUNTING
#     # =====================================================

#     def count_seeds(
#         self,
#         pit_img
#     ):

#         gray = cv2.cvtColor(
#             pit_img,
#             cv2.COLOR_BGR2GRAY
#         )

#         blur = cv2.GaussianBlur(
#             gray,
#             (5, 5),
#             0
#         )

#         circles = cv2.HoughCircles(
#             blur,
#             cv2.HOUGH_GRADIENT,
#             dp=1.2,
#             minDist=10,
#             param1=50,
#             param2=12,
#             minRadius=3,
#             maxRadius=15
#         )

#         if circles is None:
#             return 0

#         return len(circles[0])

#     # =====================================================
#     # DETECT BOARD
#     # =====================================================

#     def detect_board(
#         self,
#         frame
#     ):

#         # print(
#         #     f"PITS LOADED: "
#         #     f"{len(self.pits)}"
#         # )

#         if len(self.pits) == 0:

#             raise RuntimeError(
#                 "No pits loaded. "
#                 "Run calibration first."
#             )

#         board = []

#         for i, pit in enumerate(
#             self.pits
#         ):

#             pit_img = self.extract_pit(
#                 frame,
#                 pit
#             )

#             count = self.count_seeds(
#                 pit_img
#             )

#             # print(
#             #     f"Pit {i}: {count}"
#             # )

#             board.append(count)

#         # print(
#         #     "BOARD STATE:",
#         #     board
#         # )

#         return board

#     # =====================================================
#     # DEBUG VIEW
#     # =====================================================

#     def debug_scan(self):

#         ret, frame = self.cap.read()

#         if not ret:
#             return

#         board = self.detect_board(
#             frame
#         )

#         for i, pit in enumerate(
#             self.pits
#         ):

#             x = int(pit["x"])
#             y = int(pit["y"])
#             r = int(pit["r"])

#             cv2.circle(
#                 frame,
#                 (x, y),
#                 r,
#                 (0, 255, 0),
#                 2
#             )

#             cv2.putText(
#                 frame,
#                 str(board[i]),
#                 (x - 20, y),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.7,
#                 (0, 0, 255),
#                 2
#             )

#         cv2.imshow(
#             "Oware Debug",
#             frame
#         )

#         cv2.waitKey(1)

#     # =====================================================
#     # CLEANUP
#     # =====================================================

#     def close(self):

#         if self.cap:
#             self.cap.release()

#         cv2.destroyAllWindows()


import cv2
import json
import os
import time


class OwareVision:

    CALIBRATION_FILE = "games/oware/pits.json"

    def __init__(self, camera_index=0):

        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)

        self.pits = []

        # =========================
        # DEBUG STORAGE
        # =========================
        self.debug_dir = "debug/oware"
        self.pit_dir = os.path.join(self.debug_dir, "pits")

        os.makedirs(self.debug_dir, exist_ok=True)
        os.makedirs(self.pit_dir, exist_ok=True)

        # =========================
        # LOAD CALIBRATION
        # =========================
        if os.path.exists(self.CALIBRATION_FILE):
            self.load_calibration()
            print(f"[OWARE] Loaded {len(self.pits)} pits")
        else:
            print("[OWARE] WARNING: No calibration file found")

    # =====================================================
    # CALIBRATION
    # =====================================================

    def save_calibration(self):

        with open(self.CALIBRATION_FILE, "w") as f:
            json.dump(self.pits, f, indent=4)

        print(f"[OWARE] Saved {len(self.pits)} pits")

    def load_calibration(self):

        with open(self.CALIBRATION_FILE, "r") as f:
            self.pits = json.load(f)

    def calibrate(self):

        ret, frame = self.cap.read()

        if not ret:
            raise RuntimeError("Camera not found")

        display = frame.copy()
        self.pits = []

        def click(event, x, y, flags, param):

            if event == cv2.EVENT_LBUTTONDOWN:

                self.pits.append({
                    "x": x,
                    "y": y,
                    "r": 45
                })

                cv2.circle(display, (x, y), 5, (0, 255, 0), -1)

                cv2.putText(
                    display,
                    str(len(self.pits) - 1),
                    (x + 10, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        cv2.namedWindow("Oware Calibration")
        cv2.setMouseCallback("Oware Calibration", click)

        print("[OWARE] Click all 12 pits, press Q when done")

        while True:

            cv2.imshow("Oware Calibration", display)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break

        cv2.destroyAllWindows()

        if len(self.pits) != 12:
            raise RuntimeError(f"Expected 12 pits, got {len(self.pits)}")

        self.save_calibration()

    # =====================================================
    # PIT EXTRACTION (WITH SAVING)
    # =====================================================

    def extract_pit(self, frame, pit, pit_id=None):

        x = int(pit["x"])
        y = int(pit["y"])
        r = int(pit["r"])

        pit_img = frame[y-r:y+r, x-r:x+r]

        # SAVE PIT IMAGE
        if pit_id is not None:
            pit_path = os.path.join(self.pit_dir, f"pit_{pit_id}.jpg")
            cv2.imwrite(pit_path, pit_img)

        return pit_img

    # =====================================================
    # SEED COUNTING
    # =====================================================

    def count_seeds(self, pit_img):

        gray = cv2.cvtColor(pit_img, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        circles = cv2.HoughCircles(
            blur,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=10,
            param1=50,
            param2=12,
            minRadius=3,
            maxRadius=15
        )

        if circles is None:
            return 0

        return len(circles[0])

    # =====================================================
    # BOARD DETECTION (WITH DEBUG SAVE)
    # =====================================================

    def detect_board(self, frame):

        if len(self.pits) == 0:
            raise RuntimeError("No pits loaded. Run calibration first.")

        board = []
        annotated = frame.copy()

        for i, pit in enumerate(self.pits):

            pit_img = self.extract_pit(frame, pit, pit_id=i)

            count = self.count_seeds(pit_img)

            board.append(count)

            x = int(pit["x"])
            y = int(pit["y"])

            cv2.circle(annotated, (x, y), 40, (0, 255, 0), 2)
            cv2.putText(
                annotated,
                str(count),
                (x - 10, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

        # SAVE DEBUG IMAGES
        timestamp = int(time.time() * 1000)

        cv2.imwrite(
            os.path.join(self.debug_dir, f"frame_{timestamp}.jpg"),
            frame
        )

        cv2.imwrite(
            os.path.join(self.debug_dir, f"annotated_{timestamp}.jpg"),
            annotated
        )

        return  board

    # =====================================================
    # DEBUG SCAN
    # =====================================================

    def debug_scan(self):

        ret, frame = self.cap.read()

        if not ret:
            return

        board = self.detect_board(frame)

        for i, pit in enumerate(self.pits):

            x = int(pit["x"])
            y = int(pit["y"])
            r = int(pit["r"])

            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)

            cv2.putText(
                frame,
                str(board[i]),
                (x - 20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        cv2.imshow("Oware Debug", frame)
        cv2.waitKey(1)

    # =====================================================
    # CLEANUP
    # =====================================================

    def close(self):

        if self.cap:
            self.cap.release()

        cv2.destroyAllWindows()