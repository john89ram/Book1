import pygame
from pygame.sprite import Sprite

class Plane:
    """A class to manage the player's plane"""

    def __init__(self, tp_game):
        """Initialization of the plane and its starting point"""
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()
        self.settings = tp_game.settings

        self.image = pygame.image.load('Chapter14_Scoring/Target_Practice/images/plane.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y) 

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed

        self.rect.y = self.y

    def center_pos(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

class Bullets(Sprite):
    """A class to manage the bullets of the plane"""

    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = tp_game.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_w,
                                self.settings.bullet_h)
        self.rect.midright = tp_game.player.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
