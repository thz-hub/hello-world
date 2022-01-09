class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        try:
            with open('fen.txt', 'r') as fenr:
                fenrr = fenr.read()
                self.high_score = float(str(fenrr))
        except FileNotFoundError:
            self.high_score = 0
        self.level = 1

