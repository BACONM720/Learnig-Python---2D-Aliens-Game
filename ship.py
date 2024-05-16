import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """class to manage our ship"""

    def __init__(self, ai_game):
        """initialise the ship and set a starting pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """draw the ship at its curr location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.speed

        self.rect.x = self.x
