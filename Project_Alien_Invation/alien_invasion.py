import sys
import pygame
from settings import Settings
from ship import Ship

#------------------------------------------------------------------------------------------------------

### Creating a pygame window and responding to user input ###

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_height))
        pygame.display.set_caption(" Alien Invasion")

        # Draw ship to the screen
        self.ship = Ship(self)

    def run_game(self):
        """Start the mail loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Respond to keypress and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()