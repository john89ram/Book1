import pygame
import sys

class UserInput:

    def __init__(self, tp_game):
        # Initialize instance to controllable inputs in game
        self.tp_game = tp_game
        self.player = tp_game.player
        self.stats = tp_game.stats
        self._check_play_button = tp_game._check_play_button

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)
            
    def keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_p:
            self.stats.game_active = True

        elif event.key == pygame.K_SPACE:
            self.tp_game._fire_bullet()

    def keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

