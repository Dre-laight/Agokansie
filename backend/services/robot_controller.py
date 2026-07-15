



import serial
import time
import threading


class RobotController:

    def __init__(self, port="COM6", baudrate=115200):

        self.port = port
        self.baudrate = baudrate
        self.serial = None

        self.safe_z = -180
        self.pick_z = -105


    # =========================================================
    # CONNECT
    # =========================================================
    def connect(self):

        if self.serial and self.serial.is_open:
            return

        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)
            print(f"[OK] Connected to {self.port}")

        except serial.SerialException as e:
            print(f"[SERIAL ERROR] {e}")
            self.serial = None

    # =========================================================
    # GCODE SENDER
    # =========================================================
    # def send_gcode(self, cmd):

    #     self.connect()

    #     if not self.serial:
    #         print("[ERROR] Serial not connected")
    #         return

    #     print(">>", cmd)
    #     self.serial.write((cmd + "\n").encode())

    #     while True:
    #         response = self.serial.readline().decode().strip()

    #         if response:
    #             print("<<", response)

    #         if "ok" in response.lower():
    #             break
    #         if "error" in response.lower():
    #             print("[FLUIDNC ERROR]", response)
    #             return False
    
    def send_gcode(self, cmd):

        self.connect()

        if not self.serial:
            print("[ERROR] Serial not connected")
            return False

        print(">>", cmd)
        self.serial.write((cmd + "\n").encode())

        while True:

            response_bytes = self.serial.readline()

            # Debug: see exactly what the controller sent  
            print("RAW:", response_bytes)

            try:
                response = response_bytes.decode("utf-8").strip()
            except UnicodeDecodeError:
                print("[WARNING] Invalid UTF-8 data received")
                continue

            if response:
                print("<<", response)

            if "ok" in response.lower():
                return True

            if "error" in response.lower():
                print("[FLUIDNC ERROR]", response)
                return False
    
    
    
    def send_gcode_block(self, commands):

        self.connect()

        if not self.serial:
            return False

        for i, cmd in enumerate(commands):
            print(f"{i}: {cmd}")

        program = "\n".join(commands) + "\n"

        self.serial.write(program.encode())

        ok_count = 0

        while ok_count < len(commands):

            response = self.serial.readline().decode(
                "utf-8",
                errors="ignore"
            ).strip()

            if response:
                print("<<", response)

            if response.lower() == "ok":
                ok_count += 1

            elif "error" in response.lower():
                print(f"[ERROR after command {ok_count}]")
                print("Command was:", commands[ok_count])
                return False

        return True
    # =========================================================
    # MOTION
    # =========================================================
    def home(self):
        self.send_gcode("$H")

    def move(self, x, y, z=None, feed=12000):

        if z is None:
            cmd = f"G0 X{x} Y{y}"
        else:
            cmd = f"G1 X{x} Y{y} Z{z} F{feed}"
            # cmd = f"G1 X{x} Y{y} Z{z}"

        self.send_gcode(cmd)

    def pick(self):
        self.send_gcode("M3 S1000")

    def drop(self):
        self.send_gcode("M5")

    # =========================================================
    # 🚀 NEW UNIFIED EXECUTION SYSTEM
    # =========================================================
    def execute_action(self, game, action_packet):

        print("\nEXECUTING ACTION:", action_packet)

        action = action_packet["action"]
        data = action_packet["data"]

        # =====================================================
        # DAME / ACHI: MOVE PIECES
        # =====================================================
        if action == "move":

            start = game.map_to_coordinates(data["from"])
            end = game.map_to_coordinates(data["to"])

            sx, sy = start
            ex, ey = end

            # self.home()

            self.move(sx, sy, self.safe_z)
            self.move(sx, sy, self.pick_z)

            self.pick()

            self.move(sx, sy, self.safe_z)

            self.move(ex, ey, self.safe_z)
            self.move(ex, ey, self.pick_z)

            self.drop()

            self.move(ex, ey, self.safe_z)

            # self.home()

        # =====================================================
        # OWARE: SOWING ACTION
        # =====================================================
        elif action == "sow":

            moves = data["moves"]

            for move_data in moves:

                # =====================================
                # SOW ONE BEAD
                # =====================================
                if move_data["type"] == "sow":

                    source = move_data["from"]
                    target = move_data["to"]

                    sx, sy = game.map_to_coordinates(source)
                    tx, ty = game.map_to_coordinates(target)

                    # Pick ONE bead from source pit
                    # self.move(sx, sy, self.safe_z)
                    self.move(sx, sy, self.pick_z)

                    self.pick()

                    self.move(sx, sy, self.safe_z)

                    # Move to destination pit
                    self.move(tx, ty, self.safe_z)
                    self.move(tx, ty, self.pick_z)

                    self.drop()

                    self.move(tx, ty, self.safe_z)

                # =====================================
                # CAPTURE ONE BEAD
                # =====================================
                elif move_data["type"] == "capture":

                    source = move_data["from"]
                    owner = move_data["owner"]

                    sx, sy = game.map_to_coordinates(source)

                    # Choose the correct capture container
                    if owner == 1:
                        cx, cy = 70, 80
                    else:
                        cx, cy = 70, 200

                    # Pick one captured bead
                    self.move(sx, sy, self.safe_z)
                    self.move(sx, sy, self.pick_z)

                    self.pick()

                    self.move(sx, sy, self.safe_z)

                    # Move to capture container
                    self.move(cx, cy, self.safe_z)
                    self.move(cx, cy, self.pick_z)

                    self.drop()

                    self.move(cx, cy, self.safe_z)

            self.home()
        else:
            print("[ERROR] Unknown action:", action)
    def game_over_dispenser(self):
        self.send_gcode("""G28
                        G0 A-100""")
        # time.sleep(1)
        # self.send_gcode("G0 A0")
        # # self.send_gcode("G4 P1000")
        # time.sleep(2)
        # self.send_gcode("G0 A-360")
        # # self.send_gcode("G4 P1000")
        # time.sleep(1)
        # self.send_gcode("G0 A-100")

    # def start_dispenser(self):
    #     threading.Thread(
    #         target=self.game_over_dispenser,
    #         daemon=True
    #     ).start()    



    # def execute_action(self, game, action_packet):

    #     print("\nEXECUTING ACTION:", action_packet)

    #     action = action_packet["action"]
    #     data = action_packet["data"]

    #     commands = []

    #     # =====================================================
    #     # DAME / ACHI
    #     # =====================================================
    #     if action == "move":

    #         sx, sy = game.map_to_coordinates(data["from"])
    #         ex, ey = game.map_to_coordinates(data["to"])

    #         commands.extend([
    #             "G28",

    #             f"G1 X{sx} Y{sy} Z{self.safe_z} F10000",
    #             f"G1 X{sx} Y{sy} Z{self.pick_z} F10000",

    #             "M3 S1000",

    #             f"G1 X{sx} Y{sy} Z{self.safe_z} F10000",

    #             f"G1 X{ex} Y{ey} Z{self.safe_z} F10000",
    #             f"G1 X{ex} Y{ey} Z{self.pick_z} F10000",

    #             "M5",

    #             f"G1 X{ex} Y{ey} Z{self.safe_z} F10000",

    #             "G28"
    #         ])

    #     # =====================================================
    #     # OWARE
    #     # =====================================================
    #     elif action == "sow":

    #         for move_data in data["moves"]:

    #             if move_data["type"] == "sow":

    #                 sx, sy = game.map_to_coordinates(move_data["from"])
    #                 tx, ty = game.map_to_coordinates(move_data["to"])

    #                 commands.extend([
    #                     f"G1 X{sx} Y{sy} Z{self.pick_z} F10000",
    #                     "M3 S1000",
    #                     f"G1 X{sx} Y{sy} Z{self.safe_z} F10000",

    #                     f"G1 X{tx} Y{ty} Z{self.safe_z} F10000",
    #                     f"G1 X{tx} Y{ty} Z{self.pick_z} F10000",
    #                     "M5",
    #                     f"G1 X{tx} Y{ty} Z{self.safe_z} F10000"
    #                 ])

    #             elif move_data["type"] == "capture":

    #                 sx, sy = game.map_to_coordinates(move_data["from"])

    #                 if move_data["owner"] == 1:
    #                     cx, cy = 70, 80
    #                 else:
    #                     cx, cy = 70, 200

    #                 commands.extend([
    #                     f"G1 X{sx} Y{sy} Z{self.safe_z} F10000",
    #                     f"G1 X{sx} Y{sy} Z{self.pick_z} F10000",
    #                     "M3 S1000",
    #                     f"G1 X{sx} Y{sy} Z{self.safe_z} F10000",

    #                     f"G1 X{cx} Y{cy} Z{self.safe_z} F10000",
    #                     f"G1 X{cx} Y{cy} Z{self.pick_z} F10000",
    #                     "M5",
    #                     f"G1 X{cx} Y{cy} Z{self.safe_z} F10000"
    #                 ])

    #         # commands.append("G28")

    #     else:
    #         print("[ERROR] Unknown action:", action)
    #         return

    #     self.send_gcode_block(commands)
    # =========================================================
    # CLEANUP
    # =========================================================
    def close(self):

        if self.serial and self.serial.is_open:
            self.serial.close()
# robot = RobotController()

# robot.connect()
# # robot.start_dispenser()
# robot.game_over_dispenser()