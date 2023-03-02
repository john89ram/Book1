import pygame
import sys

from settings import Settings
from cowboy import Cowboy
from bullet import Bullets
from user_input import UserInput

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
        self.user_input = UserInput(self.cowboy, self)

    def run_game(self):
        """Main game loop"""
        while True:
            self.user_input.check_events()
            self.cowboy.update()
            self._update_bullets()
            self._update_screen()

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
