from datetime import datetime


class GameSession:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_game = None
        self.board_state = None
        self.last_move = None
        self.status = "idle"

        self.robot_busy = False
        self.game_over = False

        self.winner = None

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_timestamp(self):
        self.updated_at = datetime.now()

    def set_game(self, game_name):
        self.current_game = game_name
        self.update_timestamp()

    def set_board(self, board):
        self.board_state = board
        self.update_timestamp()

    def set_move(self, move):
        self.last_move = move
        self.update_timestamp()

    def set_status(self, status):
        self.status = status
        self.update_timestamp()

    def set_robot_busy(self, busy):
        self.robot_busy = busy
        self.update_timestamp()

    def set_game_over(self, winner=None):
        self.game_over = True
        self.winner = winner
        self.status = "game_over"
        self.update_timestamp()

    def to_dict(self):
        return {
            "current_game": self.current_game,
            "board_state": self.board_state,
            "last_move": self.last_move,
            "status": self.status,
            "robot_busy": self.robot_busy,
            "game_over": self.game_over,
            "winner": self.winner,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


# Global session instance
game_session = GameSession()