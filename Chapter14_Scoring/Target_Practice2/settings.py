import pygame.font
import pygame

class Settings:
    """A class to store all game settings for Target Practice"""
    
    def __init__(self):
        """Initialize the game's settings"""
        self.clock = pygame.time.Clock()

        # Game window settings
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (135,206,235)

        # Player settings
        self.player_speed = 5
        self.player_lives = 2

        # Bullet settings
        self.bullet_speed = 6
        self.bullet_w = 15
        self.bullet_h = 3
        self.bullet_color = (60,60,60)
        self.bullet_count = 3

        # Enemy settings
        self.enemy_speed = 1
        self.enemy_direction = 1
        self.lvl_up_speed = 1.1

    def initialize_dynamic_settings(self):

        self.player_speed = 5
        self.bullet_speed = 6
        self.enemy_speed = 1

    def lvl_up(self):

        self.player_speed *= self.lvl_up_speed
        self.bullet_speed *= self.lvl_up_speed
        self.enemy_speed  *= self.lvl_up_speed

class Button:
    
    def __init__(self, tp_game, msg):
        """Initialize button attributes"""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg,True, self.text_color,
                                          self. button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """ Draw black button and then draw msg"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class GameStats:
    """A class to start and stop main game (Game Over), and restarts game"""

    def __init__(self, tp_game):
        self.settings = tp_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.lives_left = self.settings.player_lives
