class Settings:

    def __init__(self):
        """initialise game settings"""
        # screen settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.speed = 0.5

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # if fleet of 1 represents right; -1 represents left
        self.fleet_direction = 1



