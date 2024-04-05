class GameStats:
    """track game statistics"""

    def __init__(self,ai_game):
        """initiLISe stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """initialise stats that have changed"""
        self.ship_left = self.settings.ship_limit
