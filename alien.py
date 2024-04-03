import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class to manage our ship"""

    def __init__(self, ai_game):
        """initialize the alien and set position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        """load alien image ans set rect"""
        self.image = pygame.image.load('images/AlienShip.bmp')
        self.rect = self.image.get_rect()

        """start each alien near top left of screen"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """store the aliens postion"""
        self.x = float(self.rect.x)

    def update(self):
        """move alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """return true if alien reaches edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
