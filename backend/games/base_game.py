# games/base_game.py

from abc import ABC, abstractmethod


class BaseGame(ABC):

    def __init__(self, name):

        self.name = name

        self.board_state = None

        self.game_over = False

        self.winner = None

    # =====================================================
    # BOARD STATE
    # =====================================================

    def set_board_state(self, board_state):

        self.board_state = board_state

    def get_board_state(self):

        return self.board_state

    # =====================================================
    # WINNER
    # =====================================================

    def set_winner(self, winner):

        self.winner = winner

    def get_winner(self):

        return self.winner

    # =====================================================
    # GAME STATUS
    # =====================================================

    def end_game(self, winner=None):

        self.game_over = True

        self.winner = winner

    def reset(self):

        self.board_state = None

        self.game_over = False

        self.winner = None

    # =====================================================
    # REQUIRED METHODS
    # =====================================================

    @abstractmethod
    def scan_board(self):
        pass

    @abstractmethod
    def get_best_move(self, board_state):
        pass

    @abstractmethod
    def validate_move(self, move):
        pass

    @abstractmethod
    def apply_move(self, move):
        pass

    @abstractmethod
    def is_game_over(self):
        pass

    @abstractmethod
    def map_to_coordinates(self, location):
        pass

    # =====================================================
    # JSON RESPONSE
    # =====================================================

    def get_state(self):

        return {
            "game": self.name,
            "board_state": self.board_state,
            "game_over": self.game_over,
            "winner": self.winner
        }