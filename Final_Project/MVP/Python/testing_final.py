# David Huang
# Computer Science for Designers and Artists
# Week 11
# Alex Seropian
# Version: testing v1
# Nov 15 2017

# ----- Imports -----
import pygame

pygame.init()

# ----- CONSTANTS -----
# game settings
SCREEN_SIZE = 800 # screen pixel pygame will render
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
GAME_EXIT = False
BLOCK_SIZE = 20

# game colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# game bg assets
city_bg = '/Users/David/Documents/GitHub/Final_Project/assets/city_bg_2.png'
city_street = '/Users/David/Documents/GitHub/Final_Project/assets/city_street.png'
jerry_char = '/Users/David/Documents/GitHub/Final_Project/assets/jerry.png'

# ----- Variables -----
# game window caption
pygame.display.set_caption('Testing 1')
block_position = [SCREEN_SIZE/2, SCREEN_SIZE/2]

# ----- Functions -----
def game_ground():
    pygame.draw.rect(GAME_DISPLAY, RED, [0, 468, SCREEN_SIZE, 200])

def bg_render(GAME_DISPLAY, url):
    png_image = pygame.image.load(url)
    GAME_DISPLAY.blit(png_image, (0, 0))

def char_movement(dx, dy):
    # resetting old block location
    pygame.draw.rect(GAME_DISPLAY, (0,0,0),(block_position[0], block_position[1], BLOCK_SIZE, BLOCK_SIZE))
    block_position[0] += dx
    block_position[1] += dy

    pygame.draw.rect(GAME_DISPLAY, (255,0,0), block_position[0], block_position[1], BLOCK_SIZE, BLOCK_SIZE)

def jerry(GAME_DISPLAY, url):
    character_png = pygame.image.load(url)
    GAME_DISPLAY.blit(character_png, (20, 570))


# ----- Main Loop -----

char_movement(0, 0)

while not GAME_EXIT: # while the user has not closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the user clicks quit / red x, close the window
            GAME_EXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                polling = False
            if event.key == pygame.K_UP:
                char_movement(0, -BLOCK_SIZE)
            if event.key == pygame.K_DOWN:
                char_movement(0, BLOCK_SIZE)
            if event.key == pygame.K_LEFT:
                char_movement(-BLOCK_SIZE, 0)
            if event.key == pygame.K_RIGHT:
                char_movement(BLOCK_SIZE, 0)
    bg_render(GAME_DISPLAY, city_bg) # layer 1 - bg
    bg_render(GAME_DISPLAY, city_street) # layer 2 - city street bg
    jerry(GAME_DISPLAY, jerry_char) # spawning main character
    pygame.display.update() # update the game