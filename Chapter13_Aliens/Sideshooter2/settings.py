# settings.py
# File to modify all settings in SideShooter
from random import randint

class Settings:
    """A class to store all the settings for SideShooter"""

    def __init__(self):
        """Initialize game"""

        # Game window settings
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (161,95,59)

        # Cowboy's movement speeds
        self.cowboy_s = 1.5
        self.lives_limit = 3

        # Bullet settings
        self.bullet_s = 3
        self.bullet_w = 15
        self.bullet_h = 3
        self.bullet_color = (60,60,60)
        self.bullet_count = 4

        # Snake settings
        self.snake_speed = 0.5