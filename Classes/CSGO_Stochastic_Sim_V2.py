# David Huang
# Learning Python for Designers
# CSGO Simulation V2

# Rule of thumb
    # Don't write useless code
        # This includes variables and constants
    # Don't repeat yourself
    # Before you write more code, test to see if it works first in the main loop

## IMPORTS
import random
import time

## CONSTANT
ROUNDS_AVAILABLE = 30 # there are only 30 rounds in one game to play
HALFTIME_ROUND = int(ROUNDS_AVAILABLE/2) # halftime is the round at the midpoint of the game
WINNING_ROUND = HALFTIME_ROUND+1 # team who wins 1 more than half the available round first wins the game
DEFAULT_PLAYER_COUNT = 5 # determines how many players are alive at the start of each round
DEFAULT_TEAM_SCORE = 0 # determines score teams start with
DEFAULT_TEAM_SIDE = None # starting sides for teams in the beginning
STARTING_ROUND = 0
CT_SIDE = 'Counter Terrorists'
T_SIDE = 'Terrorists'
HALVES_AVAILABLE = int(ROUNDS_AVAILABLE / HALFTIME_ROUND)

## INITIALIZING DATA
# Team A Basic Data
team_A_ID = 'Team NiP' # name for Team A
team_A_side = DEFAULT_TEAM_SIDE # what side team A is currently playing as, ct or t
# Team A Default State
team_A_points = DEFAULT_TEAM_SCORE # team B score; defaults at 0
team_A_players = DEFAULT_PLAYER_COUNT # number of players team A starts with
# Team A Statistics
team_A_ct_elim_rate = 48.2
team_A_t_plant_rate = 55
team_A_ct_defuse_rate = 33
# Team B
# Team B Basic Data
team_B_ID = 'Team Fnatic' # name for Team B
team_B_side = DEFAULT_TEAM_SIDE # what side team B is currently playing as, ct or t
# Team B Default State
team_B_points = DEFAULT_TEAM_SCORE # team B score; starts at 0
team_B_players = DEFAULT_PLAYER_COUNT # number of players team B starts with
# Team B Statistics
team_B_ct_elim_rate = 48.1
team_B_t_plant_rate = 53
team_B_ct_defuse_rate = 32
# Team Exchange Survival
team_exchange_survival = 6 # percentage chance of both teams surviving a gun exchange
# Game Progression Data
bomb_planted = False # at the start of each round, bomb is always not planted
bomb_defused = False # at the start of each round, because bomb is not planted, bomb is not defused
bomb_plant_limit = False # terrorists only have one chance to plant and detonate bomb; they can't plant twice
rounds_played_tally = 0 # tallies the total number of rounds played and concluded
winner_team = None
bomb_detonated = False

## DATA SET
TEAM_A_DATA = [team_A_ID, team_A_ct_elim_rate,
               team_A_t_plant_rate, team_A_ct_defuse_rate,
               team_A_side, team_A_players]
TEAM_B_DATA = [team_B_ID, team_B_ct_elim_rate,
               team_B_t_plant_rate, team_B_ct_defuse_rate,
               team_B_side, team_B_players]
GAME_DATA = [rounds_played_tally,
             team_A_points, team_B_points,
             bomb_planted,
             bomb_defused,
             bomb_plant_limit,
             bomb_detonated,
             ]

## TEXT DECORATION
TXT_SPACER = ' '
TXT_RULE_LONG = '-'*50
TXT_RULE_SHORT = '-'*25
TXT_DOUBLE_RULE_LONG = '='*50
TXT_DOUBLE_RULE_SHORT = '='*25

## DATA TAGS
# Sides
TEAM_A = 0
TEAM_B = 1

# Team Data Types
TEAM_NAME = 0
TEAM_CT_KD = 1
TEAM_PLANT_RATE = 2
TEAM_DEFUSE_RATE = 3
TEAM_SIDE = 4
PLAYER_COUNT = 5

# Game Data Types
ID_ROUNDS_PLAYED = 0
ID_TEAM_A_SCORE = 1
ID_TEAM_B_SCORE = 2
ID_BOMB_PLANT = 3
ID_BOMB_DEFUSE = 4
ID_BOMB_LMT = 5
ID_BOMB_DETON = 6

## GLOBAL COMPONENTS
def sleep(sleep_time):
    time.sleep(sleep_time)

## CLASSES
class GAME_INIT:

    def __init__(self, GAME_DATA):
        self.GAME_DATA = GAME_DATA

    def round_environment_reset(self):
        GAME_DATA[ID_ROUNDS_PLAYED] += 1
        GAME_DATA[3] = False
        GAME_DATA[4] = False
        GAME_DATA[5] = 0
        GAME_DATA[6] = False
        return GAME_DATA

    def team_reset(self, imported_data):
        imported_data[TEAM_A][PLAYER_COUNT] = DEFAULT_PLAYER_COUNT
        imported_data[TEAM_B][PLAYER_COUNT] = DEFAULT_PLAYER_COUNT
        return imported_data

    def user_input(self, msg_type_name):
        if msg_type_name == 'start':
            displayed_input = input('Begin match? (Y)es or (N)o : ')
            return displayed_input

    def static_msg(self, msg_type_name):
        print(TXT_SPACER)
        if msg_type_name == 'call round':
            print(TXT_RULE_LONG)
            print('Round ' , GAME_DATA[ID_ROUNDS_PLAYED] + 1, ' / ' , ROUNDS_AVAILABLE)
            print(TXT_RULE_LONG)
        elif msg_type_name == 'call round winner':
            print(TXT_RULE_LONG)
            print('Team Winner')
            print(TXT_RULE_LONG)
        elif msg_type_name == 'spacer':
            return None
        elif msg_type_name == 'intro':
            print('Welcome to the championship match of ESL Tournament')
            print('This will be a game between', TEAM_A_DATA[TEAM_NAME], 'and', TEAM_B_DATA[TEAM_NAME])
            sleep(1)
        else:
            print ('CALL ERROR: Not an available message type')
        print(TXT_SPACER)

    def sorting_data(self, first_half_teams):
        if first_half_teams[TEAM_A] == TEAM_A_DATA[TEAM_NAME]:
            TEAM_A_DATA[TEAM_SIDE] = CT_SIDE
            TEAM_B_DATA[TEAM_SIDE] = T_SIDE
            DATA_FORMATION = [TEAM_A_DATA, TEAM_B_DATA]
            return DATA_FORMATION
        else:
            TEAM_A_DATA[TEAM_SIDE] = T_SIDE
            TEAM_B_DATA[TEAM_SIDE] = CT_SIDE
            DATA_FORMATION = [TEAM_B_DATA, TEAM_A_DATA]
            return DATA_FORMATION

    def rolling_sides(self):
        if GAME_DATA[ID_ROUNDS_PLAYED] == STARTING_ROUND:
            print ('Rolling sides...')
            rolling_teams = [TEAM_A_DATA[TEAM_NAME],TEAM_B_DATA[TEAM_NAME]]
            rolled_ct_team = rolling_teams.pop(random.randint(0,1))
            rolled_t_team = rolling_teams[0]
            team_decided_roles = [rolled_ct_team, rolled_t_team]
            staging_data = self.sorting_data(team_decided_roles)
            return staging_data

    def switching_sides(self, first_half_teams):
        team_b = first_half_teams[1][0]
        team_a = first_half_teams[0][0]
        first_half_teams[0][0] = team_b
        first_half_teams[1][0] = team_a
        return first_half_teams

    def importing_data(self, first_half_teams):
        if GAME_DATA[ID_ROUNDS_PLAYED] == STARTING_ROUND:
            team_half_data = self.sorting_data(first_half_teams)
            return team_half_data
        elif GAME_DATA[ID_ROUNDS_PLAYED] == HALFTIME_ROUND:
            team_half_data = self.switching_sides()
            return team_half_data

    def dynamic_msg(self, msg_type_name, live_sorted_data):
        print (TXT_SPACER)
        if GAME_DATA[ID_ROUNDS_PLAYED] == STARTING_ROUND or GAME_DATA[ID_ROUNDS_PLAYED] == HALFTIME_ROUND:
            if msg_type_name == 'call sides':
                print(TXT_DOUBLE_RULE_LONG)
                print(live_sorted_data[TEAM_A][TEAM_NAME],'will play as',live_sorted_data[TEAM_A][TEAM_SIDE])
                print(live_sorted_data[TEAM_B][TEAM_NAME],'will play as',live_sorted_data[TEAM_B][TEAM_SIDE])
                print(TXT_DOUBLE_RULE_LONG)
        print (TXT_SPACER)

## TESTING
# Testing Initialization
GAME = GAME_INIT(GAME_DATA)
GAME.static_msg('intro')
first_half_teams = GAME.rolling_sides()
team_data_import = GAME.sorting_data(first_half_teams)
for GAME_HALF in range (HALVES_AVAILABLE):
    GAME.dynamic_msg('call sides', team_data_import)
    for rounds in range (HALFTIME_ROUND):
        GAME.static_msg('call round')
        GAME_DATA[ID_ROUNDS_PLAYED] += 1
        print (team_data_import)