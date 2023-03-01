import sys
import pygame
from settings import Settings
from star import Star

class StarryNight:
    """it says it up there"""

    def __init__(self):
        """a;lskdjf"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        
        self.star = pygame.sprite.Group()
        self._create_grid()


    def run(self):
        """a;lsdkfja;lskdjfajng"""
        while True:
            self._events()
            self._update_screen()

    def _events(self):
        """asd;lfkja;dslkvnapruiohv;afdnv"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
        """yeah yeah yeah"""
        star = Star(self)
        star_width, star_height = star.rect.size
        
        available_x = self.settings.screen_width
        number_stars_x = available_x//(star_width)
        
        available_y = self.settings.screen_height
        number_rows = available_y // star_height

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """almost there!!!"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height * row_number
        self.star.add(star)

    def _update_screen(self):
        """OMG this is not fun doing it fast"""
        self.screen.fill(self.settings.bg_color)
        self.star.draw(self.screen)

        pygame.display.flip()


if __name__=="__main__":
    sn = StarryNight()
    sn.run()