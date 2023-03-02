

class Settings:
    """A class to store all settings for Raindrops"""

    def __init__(self):
        """Initialize the settings."""

        # Game window settings
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (44,65,94)

        # Rain default settings
        self.rain_speed = 2

        # Cloud default settings
        self.cloud_speed = .5
        self.cloud_direction = 1