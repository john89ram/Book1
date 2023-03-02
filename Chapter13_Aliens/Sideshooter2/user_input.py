# user_input.py
import pygame
import sys

class UserInput:
    """Class to manage user input"""

    def __init__(self, cowboy, ss_game):
        """Initialize user input"""
        self.cowboy = cowboy
        self.ss_game = ss_game

    def check_events(self):
        """Responds to key and mouse activity"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)

    def keydown_events(self, event):
        """Checks for keys pressed"""
        if event.key == pygame.K_UP:
            self.cowboy.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.cowboy.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self.ss_game._fire_bullet()

    def keyup_events(self, event):
        """Check for keys released"""
        if event.key == pygame.K_UP:
            self.cowboy.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.cowboy.moving_down = False
