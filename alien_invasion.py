import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets & behaviour"""

    def __init__(self):
        """Initialise game and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start main game loop"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            # make most recent screen visible
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

            # Get rid of bullets of the screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _check_events(self):
        """respond to key presses and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):

        self.bullets.update()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
        """create a new bullet and add it to the group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        """update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """create a fleet of aliens"""
        # create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        num_aliens_x = available_space_x // (2 * alien_width)

        # determine number of rows that can fit
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
        num_rows = available_space_y // (2 * alien_height)

        # create full fleet
        for row_number in range(num_rows):
            for alien_number in range(num_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond if any aliens reach edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """update images on screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        self.aliens.draw(self.screen)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
