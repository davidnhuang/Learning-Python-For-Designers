# David Huang
# Alexander Seropian
# Computer Science for Designers and Artists
# Version 1.1 - Alpha
# Nov 22 2017

# 'People are capable, at any time in their lives, of doing what they dream of.' - The Alchemist

# Imports
import pygame
import time

# INITIATIONS - DO NOT CHANGE
pygame.init() # initiates pygame module
pygame.font.init() # initiates pygame font
pygame.display.set_caption('OFFICE HOURS.exe') # sets the title for the window

# ---------- CONSTANTS ----------
# font family
GAME_FONT_FAMILY = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/uni0553-webfont.ttf'
TITLE_FONT_SIZE = 40 # largest font size 40 px for titles
SUBTITLE_FONT_SIZE = 20 # 20px for subtitles
INTERFACE_FONT_SIZE = 12 # smallest font size for ingame computer

# typography display
TITLE_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, TITLE_FONT_SIZE) # renders uni0553 at 40px
SUBTITLE_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, SUBTITLE_FONT_SIZE) # renders uni0553 at 20px
COMPUTER_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, INTERFACE_FONT_SIZE) # renders uni0553 at 12px

# game surface
SCREEN_SIZE = 800 # sets max screen size at 800 px
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) # defines GAME_DISPLAY as a surface
GAME_EXIT = False # did user exit the game? default at False

# game initial settings
GAME_START = False # did user start game? defaults at False, which spawns starting title screen
SCENE = 0 # which scene is user on? defaults at 0, which is outside of Jerry's office

# world initial settings
OFFICE_HOURS = True # when player needs to go into the office for work
YEARS_COUNT = 0 # counts how many years Jerry has been working at company
INDOOR = False # tests if user has entered a building or not; defaults at no
OPEN_COMPUTER = False # is user using a computer right now? defaults at no
JERRY_RESPONSE = 0 # did user respond to angry customers?
INDOOR_LOCATION = [None, 'OFFICE', 'BAR', 'APARTMENT', 'CAVE'] # which building interior is the player on?
INTERIOR_BG_RENDER = INDOOR_LOCATION[0] # which interior bg is rendered
SLEEP = False # did player sleep? can only occur if OFFICE_OURS == False
INVENTORY = False # did player open inventory? defaults at False, which is closed
GAME_FINALE = False # did player finish the game? defaults at False
TREASURE_ENDING = False # did player find the hidden treasure?
TREASURE_REQUIREMENT = False # did player meet requirements to enter the treasure cave?
BACKGROUND_NIGHT_DAY = 0 # this number determines which background URL to render; defaults at 0, which is day time
HOMELESS_GUY = False

# game prompt positions
BG_POSITION = (0,0) # background render position
PROMPT_POSITION = (500, SCREEN_SIZE * 0.9) # actions prompt position
EXIT_COMPUTER_POSITION = (100, SCREEN_SIZE * 0.7) # exit out of computer
BAG_PROMPT_POSITION = (50, SCREEN_SIZE * 0.9) # prompt to open player inventory

# ingame collectables
FLASHLIGHT = False # did player find the flashlight for the cave?
KEY = False # did player find the key to open the treasure chest?

# dialogues
CUSTOMER_NAME = ['JOE:', 'MARRY:', 'KATIE:', 'JOHN:', 'MAX:'] # name of all angry customers
UI_STARTING_MESSAGE = '1 CUSTOMER CONNECTED ON THE LINE - 20 IN QUEUE' # starting message for ingame computer
# all the dialogues from the angry customers
CUSTOMER_DIALOGUE_START = ["HI, MY INSURANCE RATE HAS SKY ROCKETED, WHAT'S GOING ON?",
                           "YO, WTF IS GOING ON WITH MY INSURANCE RATE, IT DOUBLED?!?!?!",
                           "HEY CROOKS, WHAT ARE YOU DOING WITH MY INSURANCE RATE?",
                           "HELLO, I WAS AT HOSPITAL AND THEY SAY IT'S FAKE??",
                           "WHY IS MY DOCTOR SAYING NO TO THIS INSURANCE?",
                           "MY RATE IS GOING CRAZY, WHAT'S GOING ON?"]
# all the ending dialogues from angry customers before they disconnect
CUSTOMER_END = ["I'M CALLING MY LAWYER", "I'M SUING YOU GUYS", "HOW DO YOU GUYS SLEEP AT NIGHT?", "**** YOU ALL", "YOU'RE NOT HELP AT ALL"]

# Jerry's response
JERRY_CHAT_RESPONSES = ["I'm very sorry to hear that.",
                        "Unfortunately, I cannot do anything about that right now,",
                        "but I can forward this complaint to my manage, is that ok?"]

# colors default
BLACK = (0,0,0)
WHITE = (255,255,255)
SKY_BLUE = (135,206,235)
NIGHT_BLACK = (19,24,98)
GREEN = (0,255,0)

# character settings
# Jerry Sprite facing right
JERRY_R = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/character/jerry_right-01.png'
# Jerry Sprite facing left
JERRY_L = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/character/jerry_left-01.png'
HOMELESS_GUY_PNG = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/character/homeless_guy-01.png'

# prompted messages
# action prompts
enter_prompt = SUBTITLE_DISPLAY.render('press SPACE to enter', False, (WHITE))
pickup_prompt = SUBTITLE_DISPLAY.render('press SPACE to answer', False, (WHITE))
exit_prompt = SUBTITLE_DISPLAY.render('press E to exit', False, (WHITE))
sleep_prompt = SUBTITLE_DISPLAY.render('press SPACE to sleep', False, (WHITE))
exit_computer_prompt = SUBTITLE_DISPLAY.render('press E to exit                    press R to continue', False, (GREEN))
inventory_prompt = SUBTITLE_DISPLAY.render('press B to open your bag', False, (WHITE))
note_prompt = SUBTITLE_DISPLAY.render('press SPACE to read', False, (WHITE))
continue_prompt = SUBTITLE_DISPLAY.render('press R to continue', False, (WHITE))

# day end messages
end_of_day_display = SUBTITLE_DISPLAY.render('6:00PM', False, (WHITE))
# year end messages
end_of_year_display = SUBTITLE_DISPLAY.render('8:30AM', False, (WHITE))

# computer messages
# lines that appear on the computer screen when Jerry is in his computer
computer_ui_display = COMPUTER_DISPLAY.render('connecting to customer...', False, (GREEN))
# computer login id
random_chat_id = COMPUTER_DISPLAY.render('LOGIN: 2918.2891', False, (GREEN))
# Jerry's opening lines (constant)
jerry_chat_name = COMPUTER_DISPLAY.render('Jerry', False, (GREEN))
jerry_auto_message_1 = COMPUTER_DISPLAY.render('Hi! This is Jerry From Great Credit Insurance', False, (GREEN))
jerry_auto_message_2 = COMPUTER_DISPLAY.render('How may I help you today?', False, (GREEN))
jerry_respond_message_1 = COMPUTER_DISPLAY.render(JERRY_CHAT_RESPONSES[0], False, (GREEN))
jerry_respond_message_2 = COMPUTER_DISPLAY.render(JERRY_CHAT_RESPONSES[1], False, (GREEN))
jerry_respond_message_3 = COMPUTER_DISPLAY.render(JERRY_CHAT_RESPONSES[2], False, (GREEN))

# customer
customer_chat_name = COMPUTER_DISPLAY.render(CUSTOMER_NAME[YEARS_COUNT], False, (GREEN))
customer_chat_messages = COMPUTER_DISPLAY.render(CUSTOMER_DIALOGUE_START[YEARS_COUNT], False, (GREEN))
customer_end_messages = COMPUTER_DISPLAY.render(CUSTOMER_END[YEARS_COUNT], False, (GREEN))
customer_disconnected_message = COMPUTER_DISPLAY.render('Customer has left the chatroom.', False, (GREEN))

# text locations
# ingame computer screen positions
USER_CONNECTED_POSITION = (350, SCREEN_SIZE * 0.12) # position for text 'user connected'
END_OF_DAY_POSITION = (100, SCREEN_SIZE*0.45) # position for text after user finished a day's work ingame

# x for the start of each chat bubble
CUSTOMER_CHAT_BUBBLE = 100
JERRY_CHAT_BUBBLE = CUSTOMER_CHAT_BUBBLE

# line coordinates on ingame computer screen
COMPUTER_LINE_0 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.13)
COMPUTER_LINE_1 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.2) # line 1 on computer screen
COMPUTER_LINE_2 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.22) # line 2 on computer screen
COMPUTER_LINE_3 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.26) # line 3 on computer screen
COMPUTER_LINE_4 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.28) # line 4 on computer screen
COMPUTER_LINE_5 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.32) # line 5 on computer screen
COMPUTER_LINE_6 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.34) # line 6 on computer screen
COMPUTER_LINE_7 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.36) # line 7 on computer screen
COMPUTER_LINE_8 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.38) # line 8 on computer screen
COMPUTER_LINE_9 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.42) # line 9 on computer screen
COMPUTER_LINE_10 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.44) # line 10 on computer screen
COMPUTER_LINE_11 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.60)

# backgrounds (EX = exterior, IN = interior, FO = foreground)
# outdoor background (office hours)

# outdoor background (after hours)
OFFICE_EX_BG = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Office_exterior.png'
BAR_EX_BG = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Bar_exterior.png'
APARTMENT_EX_BG = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Apartment_exterior.png'
FOREST_1 = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Forest_1.png'
FOREST_2 = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Forest_2.png'
CAVE_1 = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Cave_2.png'
TREASURE_END = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Cave_3.png'
CITY_END = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/End_of_city.png'
HIGHWAY_END = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Highway_end.png'

BUS_STOP_BG = ['/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Bus_stop.png',
               '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Bus_stop_a.png']

HIGHWAY_1 = ['/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Highway_1.png',
             '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Highway_1_a.png']

HIGHWAY_2 = ['/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Highway_2.png',
             '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Highway_2_a.png']


# indoor background (office hours)
OFFICE_INTERIOR_1 = '/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Inside_Office_1_A.png'
OFFICE_INTERIOR_2 = ['/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Inside_Office_2.png',
                     '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Inside_Office_2_A.png']
OFFICE_INTERIOR_3 = ['/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Inside_Office_3.png',
                     '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Inside_Office_3_A.png']
OFFICE_END = ['/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Office_End.png',
              '/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Office_End_a.png']
BAR_INTERIOR = ['/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Bar_interior.png',
                '/Users/David/PycharmProjects/Python_for_designers//Final_Project_aux/assets/scene bg/Bar_interior_afterwork.png']
APARATMENT_INTERIOR = ['/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Apartment_Interior.png',
                       '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Apartment_Interior_a.png']

# indoor background (afterhours)


# computer screen
COMPUTER_SCREEN = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Screen.png'

# foreground
FO_LAMPS = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/foreground_lamp-01.png'
FO_BUS_STOP = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Bus_stop_FO.png'
FO_CITY_END = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/City_end_FO.png'
FO_ROAD_END = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Road_End_FO.png'

# ending screens
GOOD_ENDING_SCREEN = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Good_Ending.png'
POOR_ENDING_SCREEN = '/Users/David/PycharmProjects/Python_for_designers/Final_Project_aux/assets/scene bg/Poor_Ending.png'

# character positioning
JERRY_X = SCREEN_SIZE * 0.3 # initial position of Jerry
JERRY_Y = SCREEN_SIZE * 0.5 # initial position of Jerry

JERRY_X_IN = 50 # initial position of Jerry Indoor
JERRY_Y_IN = SCREEN_SIZE * 0.4 # initial position of Jerry Indoor

CHARACTER_DIR = True # character facing right by default; True = right, False = left

HOMELESS_X = SCREEN_SIZE * 0.2
HOMELESS_Y = SCREEN_SIZE * 0.49

# screen limits to trigger scene change
# outdoor
SCREEN_MAX = SCREEN_SIZE - 40 # right bound that would trigger scene change
SCREEN_MIN = 10 # left bound that would trigger scene change

# indoor
SCREEN_MAX_IN = SCREEN_SIZE - 100 # right bound that would trigger scene change
SCREEN_MIN_IN = 10 # left bound that would trigger scene change

# ---------- FUNCTIONS ----------
# movement
dx = 0
dy = 0

# box range that would trigger collision
office_door_x = 300 # collision for office and bar
office_door_y = JERRY_Y_IN

door_range_min = office_door_x - 20
door_range_max = door_range_min + 100

# indoor
office_exit_min = JERRY_X_IN # indoor exit trigger box
office_exit_max = office_exit_min + 80 # indoor exit trigger box

computer_screen_x = 250 # indoor computer trigger
answer_computer_min = computer_screen_x - 20
computer_answer_max = computer_screen_x + 100

apartment_door_min = office_door_x - 50
apartment_door_max = apartment_door_min + 300

homeless_box_min = 0
homeless_box_max = 0

# ---------- FUNCTIONS ----------
# Background Functions
def skybox(): # fills the screen with sky blue, simulating sky
    if OFFICE_HOURS == True:
        GAME_DISPLAY.fill(SKY_BLUE)
    else:
        GAME_DISPLAY.fill(NIGHT_BLACK)

def bg_render(BG_NAME): # this function renders backgrounds based on PNG names
    png_img = pygame.image.load(BG_NAME)
    GAME_DISPLAY.blit(png_img, BG_POSITION)

def backdrop_change(): # this function changes the background based on which scene the player is in
    if INDOOR == False: # if the player is outdoors
        # within the city
        if SCENE == 0: # starting position of the game
            bg_render(OFFICE_EX_BG)
        elif SCENE == 1: # outside the bar
            bg_render(BAR_EX_BG)
        elif SCENE == 2: # outside Jerry's apartment
            bg_render(APARTMENT_EX_BG)
        elif SCENE == 3: # at the end of the city street
            bg_render(CITY_END)
        # outside the city
        elif SCENE == -1: # bus stop
            bg_render(BUS_STOP_BG[BACKGROUND_NIGHT_DAY])
        elif SCENE == -2: # first segment of the highway
            bg_render(HIGHWAY_1[BACKGROUND_NIGHT_DAY])
        elif SCENE == -3: # second segment of the highway
            bg_render(HIGHWAY_2[BACKGROUND_NIGHT_DAY])
        elif SCENE == -4: # end of the road
            bg_render(HIGHWAY_END)
        elif SCENE == -5: # start of the forest
            bg_render(FOREST_1)
        elif SCENE == -6: # second part of the forest
            bg_render(FOREST_2)
        elif SCENE == -7: # outside the cave
            bg_render(CAVE_1)
        elif SCENE == -8: # the treasure
            bg_render(TREASURE_END)
    else: # if the player is indoor
        if INTERIOR_BG_RENDER == 'OFFICE':
            if SCENE == 0:
                bg_render(OFFICE_INTERIOR_1)
            elif SCENE == 1:
                bg_render(OFFICE_INTERIOR_2[BACKGROUND_NIGHT_DAY])
            elif SCENE == 2:
                bg_render(OFFICE_INTERIOR_3[BACKGROUND_NIGHT_DAY])
            elif SCENE == 3:
                bg_render(OFFICE_END[BACKGROUND_NIGHT_DAY])
        elif INTERIOR_BG_RENDER == 'BAR':
            if SCENE == 1:
                bg_render(BAR_INTERIOR[BACKGROUND_NIGHT_DAY])
        elif INTERIOR_BG_RENDER == 'APARTMENT':
            if SCENE == 2:
                bg_render(APARATMENT_INTERIOR[BACKGROUND_NIGHT_DAY])

def collision(char_x, target_box_min, target_box_max): # detects collision between player and object
    if target_box_min <= char_x <= target_box_max: # if player enters the hit box of targeet object
        return True # collision has happened
    else:
        return False # no collision detected

def prompt(msg): # blits action prompt on the lower half of the screen
    GAME_DISPLAY.blit(msg, PROMPT_POSITION)

def blit_prompt(msg, position): # more flexible prompt function where user can define what message and where it is rendered
    GAME_DISPLAY.blit(msg, position)

def homeless_blit():
    if INDOOR == False and HOMELESS_GUY == False:
        if SCENE == 2:
            GAME_DISPLAY.blit(pygame.image.load(HOMELESS_GUY_PNG), (HOMELESS_X, HOMELESS_Y))

def prompt_display(): # blits a display at a specific location on the screen
    if INDOOR == False: # if player is outdoor
        if SCENE == 0 or SCENE == 1: # if he is outside the office or outside the bar
            door_prompt = collision(JERRY_X, door_range_min, door_range_max) # is there collision with the door?
            if door_prompt == True: # if yes
                prompt(enter_prompt) # print the prompt to enter on the lower right hand side
        elif SCENE == 2: # else if he is outside his apartment
            apartment_prompt = collision(JERRY_X, apartment_door_min, apartment_door_max) # is there collision?
            if apartment_prompt == True: # if yes
                prompt(enter_prompt) # print the prompt to enter on the lower right hand side
    else: # if player is indoor
        if INTERIOR_BG_RENDER == 'OFFICE': # if player is in the first office scene
            if SCENE == 0:
                if answer_computer_min <= JERRY_X_IN <= computer_answer_max and OFFICE_HOURS == True: # if he is in range of answering his computer
                    prompt(pickup_prompt) # print answer prompt
                elif office_exit_min <= JERRY_X_IN <= office_exit_max: # else if he is near the exit
                    prompt(exit_prompt) # print exit prompt
            elif SCENE == 3:
                if SCREEN_MAX > JERRY_X_IN > SCREEN_MAX - 250:
                    prompt(note_prompt)
        elif SCENE == 1 and INTERIOR_BG_RENDER == 'BAR': # if player is in the bar interior
            if office_exit_min <= JERRY_X_IN <= office_exit_max: # if player is within exit range
                prompt(exit_prompt) # print exit prompt
        elif SCENE == 2 and INTERIOR_BG_RENDER == 'APARTMENT': # if player is in the apartment
            if office_exit_min <= JERRY_X_IN <= office_exit_max: # if he is within exit range
                prompt(exit_prompt) # print exit prompt
            elif SCREEN_SIZE > JERRY_X_IN > SCREEN_SIZE - 500 and OFFICE_HOURS == False:
                prompt(sleep_prompt)

def open_computer_interface(): # translates screen to computer interface
    if OPEN_COMPUTER == True: # if computer is turned on
        bg_render(COMPUTER_SCREEN) # blit computer UI onto screen
        blit_prompt(random_chat_id, COMPUTER_LINE_0)
        GAME_DISPLAY.blit(exit_computer_prompt, EXIT_COMPUTER_POSITION)# render computer screen UI

def chat_bubbles():
    if JERRY_RESPONSE >= 0:
        blit_prompt(jerry_auto_message_1, COMPUTER_LINE_1)
        blit_prompt(jerry_auto_message_2, COMPUTER_LINE_2)
    if JERRY_RESPONSE >= 1:
        blit_prompt(customer_chat_name, COMPUTER_LINE_3)
        blit_prompt(customer_chat_messages, COMPUTER_LINE_4)
    if JERRY_RESPONSE >= 2:
        blit_prompt(jerry_chat_name, COMPUTER_LINE_5)
        blit_prompt(jerry_respond_message_1, COMPUTER_LINE_6)
        blit_prompt(jerry_respond_message_2, COMPUTER_LINE_7)
        blit_prompt(jerry_respond_message_3, COMPUTER_LINE_8)
    if JERRY_RESPONSE >= 3:
        blit_prompt(customer_chat_name, COMPUTER_LINE_9)
        blit_prompt(customer_end_messages, COMPUTER_LINE_10)
        blit_prompt(customer_disconnected_message, COMPUTER_LINE_11)


def foreground(): # renders foreground elements
    if INDOOR == False: # if player is outdoor
        if SCENE == 0 or SCENE == 1 or SCENE == 2: # renders lamps on the street
            bg_render(FO_LAMPS)
        elif SCENE == 3:  # renders the stop sign
            bg_render(FO_CITY_END)
        elif SCENE == -1: # renders the bus bench
            bg_render(FO_BUS_STOP)
            bg_render(FO_LAMPS)
        elif SCENE == -4: # renders the road end sign
            bg_render(FO_ROAD_END)

def char_render(x, y, in_x, in_y): # renders player character
    if INDOOR == False: # if player is outdoors
        if CHARACTER_DIR == True: # if player is facing the right
            char_png = pygame.image.load(JERRY_R) # render Jerry facing right
            GAME_DISPLAY.blit(char_png, (x,y)) # blit at x,y
        else: # if player is facing the left
            char_png = pygame.image.load(JERRY_L) # render Jerry facing left
            GAME_DISPLAY.blit(char_png, (x,y)) # blit at x,y
    else: # if player is indoor
        if CHARACTER_DIR == True: # if player is facing the right
            char_png = pygame.image.load(JERRY_R) # load Jerry facing right
            enlarge_char_png = pygame.transform.scale(char_png, (250,250)) # enlarge png model
            GAME_DISPLAY.blit(enlarge_char_png, (in_x,in_y)) # blit enlarged png to x,y
        else: # if player is facing the left
            char_png = pygame.image.load(JERRY_L) # load Jerry facing left
            enlarge_char_png = pygame.transform.scale(char_png, (250,250)) # enlarge png model
            GAME_DISPLAY.blit(enlarge_char_png, (in_x,in_y)) # blit enlarge png to x,y

def day_over_message():
    GAME_DISPLAY.fill(BLACK)
    blit_prompt(end_of_day_display, END_OF_DAY_POSITION)
    prompt(continue_prompt)

def year_over_message():
    GAME_DISPLAY.fill(BLACK)
    blit_prompt(end_of_year_display, END_OF_DAY_POSITION)
    prompt(continue_prompt)

def treasure_requirements():
    if KEY == True and FLASHLIGHT == True:
        TREASURE_REQUIREMENT = True
        return TREASURE_REQUIREMENT

def game_finished():
    if YEARS_COUNT == 5:
        GAME_FINALE = True
        bg_render(POOR_ENDING_SCREEN)
        return GAME_FINALE
    elif TREASURE_END == True:
        GAME_FINALE = True
        skybox()
        bg_render(GOOD_ENDING_SCREEN)
        return GAME_FINALE


# ---------- MAIN LOOP ----------
while not GAME_EXIT:

    for event in pygame.event.get():
        # ----- KEYBOARD COMMANDS -----
        # WINDOW CLOSE
        if event.type == pygame.QUIT:
            GAME_EXIT = True # quit out the game
        # KEY PRESS
        if event.type == pygame.KEYDOWN: # detects whether there has been a key press input
            # LEFT ARROW
            if event.key == pygame.K_LEFT: # if it is the left arrow key
                CHARACTER_DIR = False # turn the character to the left
                dx = -10
            # RIGHT ARROW
            elif event.key == pygame.K_RIGHT: # if it is the right arrow key
                CHARACTER_DIR = True # turn the character to the right
                dx = 10  # move x to the right by 10 pixels per input
            # S KEY
            elif event.key == pygame.K_s: # if it is the space key
                GAME_START = True # means user has started the game
            # SPACE KEY
            elif event.key == pygame.K_SPACE:
                door_collided = collision(JERRY_X,door_range_min,door_range_max)
                if door_collided == True:
                    INDOOR = True
                    if SCENE == 0:
                        INTERIOR_BG_RENDER = INDOOR_LOCATION[1]
                    elif SCENE == 1:
                        INTERIOR_BG_RENDER = INDOOR_LOCATION[2]
                apartment_collided = collision(JERRY_X,apartment_door_min, apartment_door_max)
                if apartment_collided == True:
                    INDOOR = True
                    if SCENE == 2:
                        INTERIOR_BG_RENDER = INDOOR_LOCATION[3]
                    elif INTERIOR_BG_RENDER == 'APARTMENT':
                        bed_collided = collision(JERRY_X_IN, SCREEN_SIZE - 500, SCREEN_SIZE)
                        if OFFICE_HOURS == False:
                            SLEEP = True
                computer_collided = collision(JERRY_X_IN,answer_computer_min,computer_answer_max)
                if computer_collided == True and OFFICE_HOURS == True:
                    OPEN_COMPUTER = True
                bed_collided = collision(JERRY_X_IN, answer_computer_min, computer_answer_max)
                if computer_collided == True and OFFICE_HOURS == False:
                    SLEEP = True
            # E KEY
            elif event.key == pygame.K_e:
                if INDOOR == True:
                    if INTERIOR_BG_RENDER == 'OFFICE':
                        if SCENE == 0 and office_exit_min <= JERRY_X_IN <= office_exit_max:
                            INDOOR = False
                    elif INTERIOR_BG_RENDER == 'BAR':
                        if SCENE == 1 and office_exit_min <= JERRY_X_IN <= office_exit_max:
                            INDOOR = False
                    elif INTERIOR_BG_RENDER == 'APARTMENT':
                        if SCENE == 2 and office_exit_min <= JERRY_X_IN <= office_exit_max:
                            INDOOR = False
                if OPEN_COMPUTER == True:
                    OPEN_COMPUTER = False
            # R KEY
            elif event.key == pygame.K_r:
                if OPEN_COMPUTER == True:
                    JERRY_RESPONSE += 1
        # KEY RELEASE
        if event.type == pygame.KEYUP: # detects if the user has released a keypress
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # whenever an arrow key is released
                dx = 0 # stop the x changes of the character; prevent the character from moving indefinitely
                dy = 0 # stop the y changes in the character; prevent the character from moving indefinitely

    if INDOOR == False: # if the player is outdoor
        if JERRY_X >= SCREEN_MAX: # if Jerry comes to 40px from the right side of the screen
            JERRY_X = 15 # reset Jerry to the left at 10px
            SCENE += 1 # change scene background
        elif JERRY_X < SCREEN_MIN:  # if Jerry comes to 10px from the left side of the screen
            JERRY_X = SCREEN_SIZE * 0.95 # reset Jerry to the right of the screen
            SCENE -= 1 # change scene background
    else: # if the player is indoor
        if JERRY_X_IN >= SCREEN_MAX_IN:
            JERRY_X_IN = 20
            SCENE += 1
        elif JERRY_X_IN < SCREEN_MIN_IN:
            JERRY_X_IN = SCREEN_SIZE * 0.7
            SCENE -= 1
    # ---------- MAIN SURFACE ----------
    # BACKGROUND LAYERS#
    skybox()
    backdrop_change()
    # Layer 5 (characters)
    if INDOOR == False:
        JERRY_X += dx
    else:
        JERRY_X_IN += dx * 2
    homeless_blit()
    char_render(JERRY_X,JERRY_Y,JERRY_X_IN,JERRY_Y_IN)
    # Layer 4
    foreground()
    # Layer 3
    prompt_display()
    # Layer 2
    blit_prompt(inventory_prompt, BAG_PROMPT_POSITION)
    # Layer 1
    open_computer_interface()
    if OPEN_COMPUTER == True:
        chat_bubbles()
    #SLEEP
    if OFFICE_HOURS == False and SLEEP == True:
        year_over_message()
    # TOP Layer
    # ---------- MAIN SURFACE END ----------
    # game update function
    pygame.display.flip()
    # GAME BOUNDARIES
    if INDOOR == True: # if player is indoor
        if INTERIOR_BG_RENDER == 'OFFICE': # if player is in office
            if SCENE == 0: # if player is in the first segment of the office
                if SCREEN_MIN + 50 > JERRY_X_IN > SCREEN_MIN:
                    dx = 0
            elif SCENE == 3: # if player is at the last segment of the office
                if SCREEN_MAX > JERRY_X_IN > SCREEN_MAX - 250:
                    dx = 0
        elif INTERIOR_BG_RENDER == 'BAR': # if player is in the bar
            if SCENE == 1:
                if SCREEN_MIN + 50 > JERRY_X_IN > SCREEN_MIN:
                    dx = 0
                elif SCREEN_SIZE > JERRY_X_IN > SCREEN_SIZE - 350:
                    dx = 0
        elif INTERIOR_BG_RENDER == 'APARTMENT': # if player is inside his apartment
            if SCENE == 2:
                if SCREEN_MIN + 30 > JERRY_X_IN > SCREEN_MIN:
                    dx = 0
                elif SCREEN_SIZE > JERRY_X_IN > SCREEN_SIZE - 500:
                    dx = 0
    else: # if player is outdoor
        if SCENE == 3: # if player reached end of city street
            if SCREEN_SIZE > JERRY_X > SCREEN_MAX - 300:
                dx = 0
        elif SCENE == -4: # if player reached end of highway
            if SCREEN_MIN + 500 > JERRY_X > SCREEN_MIN:
                dx = 0