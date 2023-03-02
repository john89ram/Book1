# 13-3 Raindrops:
    # Find an image of a raindrop and create a grid of raindrops.
    # Make the raindrops fall toward the bottom of the screen until they disappear

import sys
import pygame
from settings import Settings
from cloud import Cloud

class Raindrop:
    """Small animation for a rainstorm"""

    def __init__(self):
        """Initialize the scene, and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w,
                                                self.settings.screen_h))
        
        pygame.display.set_caption("Rainy Storm")

    def run(self):
        """Main animation loop and resources"""
        while True:
            self._check_events()
#            self._update_clouds()
#            self._update_rain()
            self._update_screen()

    def _check_events(self):
        """Responds to mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """Update images on the screen, flip to new screen"""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()


if __name__=='__main__':
    rd = Raindrop()
    rd.run()