# 13-3 Raindrops: 
    # Program to handle all assets and places them on scene and main loop
        # A row of raindrops needs to be created and at the top of the screen
        # Once on screen they need to drop.
        # End program
import sys
import pygame
from settings import Settings

class Raindrops:
    """OVerall class to manage scene assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        
        # Include sprite group for rain here

    def run_scene(self):
        """Main animation loop"""
        while True:
            self._update_events()

            self._update_screen()

    def _update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)



        pygame.display.flip()


if __name__=="__main__":
    rd = Raindrops()
    rd.run_scene()