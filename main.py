import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

#initialise pygame
pygame.init()

#sets the game display name at window top
pygame.display.set_caption("Super Star Quest")

#set window size,colour,fps and speed of user movement
BG_COLOUR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

#EVENT LOOP
def main(window):
    clock = pygame.time.Clock()
#event loop while loop, ensures FPS
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()


#ONLY CALLING THIS FUNCTION IF CALLED, NOT RUN WHEN BEING CALLED FROM OTHER FILES/FUNCTIONS
if __name__=="__main__":
    main(window)