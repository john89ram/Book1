import pygame
import sys

from time import sleep
from settings import Settings
from game_stats import GameStats
from random import randint
from cowboy import Cowboy
from bullet import Bullets
from snake import Snake
from user_input import UserInput

class SideShooter:
    """Overall class to manage main game assets and behaviors"""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w,
                                               self.settings.screen_h))
        self.screen_rect = self.screen.get_rect()
        
        pygame.display.set_caption("Side Shooter!")

        self.stats = GameStats(self)

        self.cowboy = Cowboy(self)
        self.bullets = pygame.sprite.Group()
        self.snakes = pygame.sprite.Group()
        self.user_input = UserInput(self.cowboy, self)

        self._create_swarm()

    def run_game(self):
        """Main game loop"""
        while True:
            self.clock.tick(240)
            self.user_input.check_events()
            if self.stats.game_active:
                self.cowboy.update()
                self._update_bullets()
                self._update_snakes()
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
        self._check_bullet_swarm_collisions()

    def _check_bullet_swarm_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.snakes, True, True)

        if not self.snakes:
            self.bullets.empty()
            self._create_swarm()

    def _create_swarm(self):
        """Create a swarm of snakes"""
        for i in range(randint(1,5)):
            snake = Snake(self)
            self.snakes.add(snake)

    def _update_snakes(self):
        self.snakes.update()
        for snake in self.snakes.copy():
            if snake.rect.right <= 0:
                self.snakes.remove(snake)
        if pygame.sprite.spritecollideany(self.cowboy, self.snakes):
            self._snake_bite()

    def _snake_bite(self):
        if self.stats.lives_left > 0:
            self.stats.lives_left -= 1

            self.snakes.empty()
            self.bullets.empty()

            self._create_swarm()
            self.cowboy.center_pos()
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update image on the screen, flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.cowboy.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.snakes.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    ss = SideShooter()
    ss.run_game()
