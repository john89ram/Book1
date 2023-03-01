# 12-5 Keys
    # Make a simple pygame file that creates an empty screen.
    # Have a while loop to keep the screen open
    # Also have the program print the event.key attribute whenever a pygame.KEYDOWN event is detected.
        # Run the program and press various keys to see how Pygame responds.

import sys
import pygame

class Keydown:
    """Simple class to show that the down key has been pressed"""

    def __init__(self):
        pygame.init()

        pygame.display.set_mode((200,200))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                print(event.key)

            pygame.display.flip()

    

if __name__=="__main__":
    game = Keydown()
    game.run()