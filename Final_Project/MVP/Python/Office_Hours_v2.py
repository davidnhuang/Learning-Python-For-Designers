# David Huang
# Alexander Seropian
# Computer Science for Designers and Artists
# Version 1.1 - Alpha
# Dec 6 2017

# 'People are capable, at any time in their lives, of doing what they dream of.' - The Alchemist

# INDEX #
# 1.0 imports
# 2.0 initialization
# 3.0 constants
    # 3.1 screen sets
    # 3.2 game starts
    # 3.3 font sets
# 4.0 settings
    # 4.1 game settings
    # 4.2 font sizing settings
    # 4.3 world intial settings (critical)
        # 4.3.1 game time
        # 4.3.2 game background
        # 4.3.3 game item states
        # 4.3.4 game screen display
        # 4.3.5 game character setting
        # 4.3.6 game requirements
        # 4.3.7 game finale settings
# 5.0 rendering
    # 5.1 font rendering
# 6.0 functions

#----- 1.0 IMPORTS -----#
import pygame

#----- 2.0 INITIALIZATION -----#
pygame.init() # initiates pygame module
pygame.font.init() # initiates pygame font
pygame.display.set_caption('OFFICE HOURS - the Game') # sets the title for the window

#----- 3.0 CONSTANT -----#
# 3.1 screen sets
SCREEN_SIZE = 800 # sets max screen size at 800 px
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) # defines GAME_DISPLAY as a surface

# 3.2 game starts
GAME_EXIT = False # did user exit the game? default at False

# 3.3 font sets
GAME_FONT_FAMILY = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/uni0553-webfont.ttf'

#----- 4.0 SETTINGS -----#
# 4.1 game setting
GAME_START = False # did user start game? defaults at False, which spawns starting title screen
SCENE = 0 # which scene is user on? defaults at 0, which is outside of Jerry's office

# 4.2 font sizing settings
TITLE_SIZE = 40 # largest font size 40 px for titles
SUBTITLE_SIZE = 20 # 20px for subtitles
PARAGRAPH_SIZE = 12 # smallest font size for in-game computer

# 4.3 world initial settings (crucial)
# 4.3.1 game time
OFFICE_HOURS = True # when player needs to go into the office for work
YEARS_COUNT = 0 # counts how many years Jerry has been working at company
DAY_OR_NIGHT = 0 # this number determines which background URL to render; defaults at 0, which is day time

# 4.3.2 game background
INDOOR = False # tests if user has entered a building or not; defaults at no
INDOOR_LOCATION = [None, 'OFFICE', 'BAR', 'APARTMENT', 'CAVE'] # which building interior is the player on?
INDOOR_BACKGROUND = INDOOR_LOCATION[0] # which interior bg is rendered

# 4.3.3 game item states
NOTE = False # is Jerry reading a note?
FIRST_PAGE_FOUND = False # did Jerry bump into the first not of the lost journal?
SECOND_PAGE_FOUND = False # did Jerry find the second page of the lost journal?

# 4.3.4 game screen display
COMPUTER_SCREEN = False # is user using a computer right now? defaults at no
STARTING_SCREEN = True # starting screen for the game
INTRO_SCREEN = True # introduction screen for Jerry
END_OF_DAY_MESSAGE = False # message at the end of the day
SLEEP_WINDOW = False

# 4.3.5 game character states
COMPUTER_RESPONSE = 0 # did user respond to angry customers?
SLEEP = False # did player sleep? can only occur if OFFICE_OURS == False
HOMELESS_GUY = False

# 4.3.6 game requirements
TREASURE_REQUIREMENT_MET = False # did player meet requirements to enter the treasure cave?

# 4.3.7 game finale states
TREASURE_ENDING = False # did player find the hidden treasure?

#----- 5.0 RENDERING -----#
# 5.1 font rendering
TITLE_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, TITLE_SIZE) # renders uni0553 at 40px
SUBTITLE_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, SUBTITLE_SIZE) # renders uni0553 at 20px
COMPUTER_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, PARAGRAPH_SIZE) # renders uni0553 at 12px

# 5.2 game asset positions
# 5.2.1 background image position
BG_POSITION = (0,0) # background render position

#----- 6.0 FUNCTIONS -----#

# ========================== GAME START ========================== #

# =========================== GAME END ========================== #
