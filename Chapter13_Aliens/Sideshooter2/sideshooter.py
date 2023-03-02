# 13-6 Game over
    # In Sideshooter, keep track of the number of times the player is hit
        # and number of time the enemy is hit by the player.
    # Decide on an appropriate condition for ending the game, and stop the game when this event occurs.     
# Main game file

import sys
import pygame

from settings import Settings
from cowboy import Cowboy
from bullet import Bullets

class SideShooter:
    """Overall class to manage main game assets and behaviors"""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w,
                                               self.settings.screen_h))
        self.screen_rect = self.screen.get_rect()
        
        pygame.display.set_caption("Side Shooter!")

        self.cowboy = Cowboy(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            self.cowboy.update()
            self._update_bullets()
            self._update_screen()
            print(len(self.bullets))

    def _check_events(self):
        """Responds to key and mouse activity"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        """Checks for keys pressed"""
        if event.key == pygame.K_UP:
            self.cowboy.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.cowboy.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _keyup_events(self, event):
        """Check for keys released"""
        if event.key == pygame.K_UP:
            self.cowboy.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.cowboy.moving_down = False

    def _fire_bullet(self):
        """Creating and adding bullets to group"""
        if len(self.bullets) < self.settings.bullet_count:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update image on the screen, flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.cowboy.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    ss = SideShooter()
    ss.run_game()