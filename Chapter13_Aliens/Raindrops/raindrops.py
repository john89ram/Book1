# 13-3 Raindrops: 
    # Program to handle all assets and places them on scene and main loop
        # A row of raindrops needs to be created and at the top of the screen
        # Once on screen they need to drop.
        # End program
import sys
import pygame
from settings import Settings
from drop import Drop

class Raindrops:
    """OVerall class to manage scene assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        
        self.drop = pygame.sprite.Group()
        self._create_rain()

    def run_scene(self):
        """Main animation loop"""
        while True:
            self._update_events()
            self._update_drops()
            self._update_screen()

    def _update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_rain(self):
        drop = Drop(self)
        drop_w, drop_h = drop.rect.size

        available_x = self.settings.screen_width
        num_drops_x = available_x//drop_w

        for drop_num in range(num_drops_x):
            self._create_drop(drop_num)

    def _create_drop(self, drop_num):
        drop = Drop(self)
        drop_w, drop_h = drop.rect.size
        drop.x = drop_w*drop_num
        drop.rect.x = drop.x
        self.drop.add(drop)

    def _update_drops(self):
        self.drop.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drop.draw(self.screen)


        pygame.display.flip()


if __name__=="__main__":
    rd = Raindrops()
    rd.run_scene()