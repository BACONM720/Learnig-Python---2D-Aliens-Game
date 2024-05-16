class GameStats:
    """track game statistics"""

    def __init__(self, ai_game):
        """initiLise stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """initialise stats that have changed"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
