# 14-3 Challenging Target Practice
    # Use everything form 14-2
    # Let make the target move faster with each hit and back to normal when restarting the game

import sys
import pygame
from settings import Settings, GameStats, Button
from player import Plane, Bullets
from enemy import Enemy
from user_inputs import UserInput
#---------------------------------------------------------------------------------------------------
class TargetPractice:
    """Simple game task to practice what the book has already explained."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_w,
                                               self.settings.screen_h))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption("Target Practice")
#---------------------------------------------------------------------------------------------------
        # Initialize child classes for main game use
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")

        self.player = Plane(self)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.user_input = UserInput(self)

        self._create_target()
#---------------------------------------------------------------------------------------------------
    def run_game(self):
        """Start of the main loop for the game."""
        while True:
            self.settings.clock.tick(120)
            self.user_input.check_events()
            if self.stats.game_active:
                self.player.update()
                self._update_bullets()
                self._update_target()
            self._update_screen()
            print(self.settings.bullet_count, self.stats.lives_left, self.settings.enemy_speed)
#---------------------------------------------------------------------------------------------------
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_count:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self._missed_shots()
        self._check_target_hit()

    def _check_target_hit(self):
        collision = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if collision:
            self.settings.bullet_count = 3

        if not self.enemies:
            self.bullets.empty()
            self._create_target()
            self.settings.lvl_up()

    def _missed_shots(self):
        if self.stats.lives_left > 0:
            self.stats.lives_left -= 1

            self.enemies.empty()
            self._create_target()
        
        else:
            self.stats.game_active = False
#---------------------------------------------------------------------------------------------------
    def _create_target(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)
    
    def _update_target(self):
        self.enemies.update()
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_direction()
                break

    def _change_direction(self):
        self.settings.enemy_direction *= -1

#---------------------------------------------------------------------------------------------------
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets
            self.enemies.empty()
            self.bullets.empty()

            # Create a new fleet and center ship
            self._create_target()
            self.settings.initialize_dynamic_settings()

            # Hide the mouse during active game
            pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
#---------------------------------------------------------------------------------------------------
if __name__=='__main__':
    tp_game = TargetPractice()
    tp_game.run_game()