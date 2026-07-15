from games.oware.game import OwareGame
from games.achi.game import AchiGame
from games.dame.game import DameGame


class GameManager:

    # def __init__(self):
    #     self.current_game_name = None
    #     self.current_game = None

    #     self.available_games = {
    #         "oware": OwareGame,
    #         "achi": AchiGame,
    #         "dame": DameGame
    #     }
    def __init__(self):
        self.current_game_name = None
        self.current_game = None

        self.available_games = {
            "oware": OwareGame,
            "achi": AchiGame,
            "dame": DameGame
        }

        self.loaded_games = {}

    # def select_game(self, game_name):

    #     game_name = game_name.lower()

    #     if game_name not in self.available_games:
    #         raise ValueError(
    #             f"Unsupported game: {game_name}"
    #         )

    #     self.current_game_name = game_name

    #     game_class = self.available_games[game_name]

    #     self.current_game = game_class()
    #     print(self.current_game)

    #     return self.current_game
    
    def select_game(self, game_name):

        game_name = game_name.lower()

        if game_name not in self.available_games:
            raise ValueError(f"Unsupported game: {game_name}")

        self.current_game_name = game_name

        if game_name not in self.loaded_games:
            game_class = self.available_games[game_name]
            self.loaded_games[game_name] = game_class()

        self.current_game = self.loaded_games[game_name]

        return self.current_game

    def get_current_game(self):
        return self.current_game

    def get_current_game_name(self):
        return self.current_game_name

    def has_game_selected(self):
        return self.current_game is not None

    # def reset_game(self):

    #     if self.current_game_name is None:
    #         return

    #     game_class = self.available_games[
    #         self.current_game_name
    #     ]

    #     self.current_game = game_class()
    def reset_game(self):

        if self.current_game_name is None:
            return

        game_class = self.available_games[
            self.current_game_name
        ]

        # Replace the old instance with a fresh one
        self.loaded_games[
            self.current_game_name
        ] = game_class()

        self.current_game = self.loaded_games[
            self.current_game_name
        ]

    def clear_game(self):

        self.current_game = None
        self.current_game_name = None

    def get_available_games(self):

        return list(
            self.available_games.keys()
        )

    def get_status(self):

        return {
            "current_game": self.current_game_name,
            "game_loaded": self.current_game is not None,
            "available_games":
                self.get_available_games()
        }


game_manager = GameManager()