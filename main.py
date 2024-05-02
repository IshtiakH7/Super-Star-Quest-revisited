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

#set window size,fps and speed of user movement
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites ]

#load every file in directory
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width()//width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i*width, 0, width, height)
            surface.blit(sprite_sheet, (0,0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "")+ "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

class Player(pygame.sprite.Sprite):
    COLOUR = (255, 0, 0)
    GRAVITY = 1

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.falling_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.falling_count/fps)* self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.falling_count += 1


    def draw(self, win):
        pygame.draw.rect(win, self.COLOUR, self.rect)


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(join("Background", "Green.png"))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)


#EVENT LOOP
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Green.png")

    player = Player(100, 100, 50, 50)

#event loop while loop, ensures FPS
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)
    pygame.quit()
    quit()


#ONLY CALLING THIS FUNCTION IF CALLED, NOT RUN WHEN BEING CALLED FROM OTHER FILES/FUNCTIONS
if __name__=="__main__":
    main(window)