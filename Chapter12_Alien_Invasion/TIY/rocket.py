import sys
import pygame

# Creating our rocket ship
class RocketShip:
    """A class to manage the rocket ship"""
    
    def __init__(self, tiy_game):
        """Initialization and set the starting position."""
        self.screen = tiy_game.screen
        self.screen_rect = tiy_game.screen.get_rect()

        # Load image and apply rect
        self.image = pygame.image.load('Chapter12_Alien_Invasion/TIY/rocket.png')
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.movement_right = False
        self.movement_left = False
        self.movement_up = False
        self.movement_down = False

    def movement_updates(self):
        """Update the ship's position based on the movement flag."""
        if self.movement_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.movement_left and self.rect.left > 0:
            self.x -= 1
        if self.movement_up and self.rect.top > 0:
            self.y -= 1
        if self.movement_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at defined location"""
        self.screen.blit(self.image, self.rect)

class RocketGame:
    """Class to manage all game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        # Creating a basic game window with title(caption)
        self.screen = pygame.display.set_mode((800,800))
        self.bg_color = (0,0,0)
        pygame.display.set_caption("Rocket Game")

        self.rocket = RocketShip(self)

    # Run game
    def run_game(self):
        """Main game loop"""
        while True:
            self._game_events()
            self._screen_update()
            # Dont forget that the screen needs to be updated with the rockets movements in order to actually move... 
            self.rocket.movement_updates()

    # Manage screen
    def _screen_update(self):
        """Update game screen"""
        self.screen.fill(self.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

    # Manage events
    def _game_events(self):
        """Respond to events on the game (keys & mouse)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        """Responds to pressed keys"""
        if event.key == pygame.K_RIGHT:
            self.rocket.movement_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.movement_left = True
        elif event.key == pygame.K_UP:
            self.rocket.movement_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.movement_down = True

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.movement_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.movement_left = False
        elif event.key == pygame.K_UP:
            self.rocket.movement_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.movement_down = False



# Dont forget you have to create an instance if you want to run your game. Building a class and functions will not do anything unless you actually use them... LOL
if __name__=="__main__":
    rocket = RocketGame()
    rocket.run_game()
