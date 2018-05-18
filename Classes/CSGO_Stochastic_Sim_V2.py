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
TEAM_A_DATA = [team_A_ID, team_A_ct_elim_rate, team_A_t_plant_rate, team_A_ct_defuse_rate, team_A_side, team_A_players]
TEAM_B_DATA = [team_B_ID, team_B_ct_elim_rate, team_B_t_plant_rate, team_B_ct_defuse_rate, team_B_side, team_B_players]

GAME_DATA = [rounds_played_tally,
             team_A_points, team_B_points,
             bomb_planted, # if bomb is planted by t side, return true
             bomb_defused, # if bomb is planted and defused, return true
             bomb_plant_limit,
             bomb_detonated] # if bomb has been planted once, it cannot be planted again

## TEXT DECORATION
TXT_SPACER = ' '
TXT_RULE_LONG = '-'*50
TXT_RULE_SHORT = '-'*25
## DATA TAGS
# Sides
TEAM_A = 0
TEAM_B = 1

# Types
TEAM_NAME = 0
TEAM_CT_KD = 1
TEAM_PLANT_RATE = 2
TEAM_DEFUSE_RATE = 3
TEAM_SIDE = 4
PLAYER_COUNT = 5

## CLASSES
class GAME_INIT:

    def __init__(self, GAME_DATA):
        self.GAME_DATA = GAME_DATA

    def importing_data(self):
        if GAME_DATA[0] == STARTING_ROUND or GAME_DATA[0] == HALFTIME_ROUND:
            rolling_teams = [TEAM_A_DATA[TEAM_NAME],TEAM_B_DATA[TEAM_NAME]]
            rolled_ct_team = rolling_teams.pop(random.randint(0,1))
            rolled_t_team = rolling_teams[0]
            team_decided_roles = [rolled_ct_team, rolled_t_team]
            if team_decided_roles[0] == TEAM_A_DATA[TEAM_NAME]:
                TEAM_A_DATA[TEAM_SIDE] = CT_SIDE
                TEAM_B_DATA[TEAM_SIDE] = T_SIDE
                DATA_FORMATION = [TEAM_A_DATA, TEAM_B_DATA]
                return DATA_FORMATION
            else:
                TEAM_A_DATA[TEAM_SIDE] = T_SIDE
                TEAM_B_DATA[TEAM_SIDE] = CT_SIDE
                DATA_FORMATION = [TEAM_B_DATA, TEAM_A_DATA]
                return DATA_FORMATION

    def round_over(self):
        # if ct is eliminated or t is eliminated
        if self.importing_data()[TEAM_A][PLAYER_COUNT] == 0 or self.importing_data()[TEAM_B][PLAYER_COUNT] == 0 or self.GAME_DATA[4] == True or self.GAME_DATA[6] == True:
            return True

    def game_over(self):
        if GAME_DATA[0] < ROUNDS_AVAILABLE and GAME_DATA[3] == WINNING_ROUND or GAME_DATA[4] == WINNING_ROUND:
                return True
        elif GAME_DATA[3] == HALFTIME_ROUND and GAME_DATA[4] == HALFTIME_ROUND:
            return True
        else:
            return False

    def message_display(self, decorator_1, msg_type_name, decorator_2):
        print(TXT_SPACER)
        print(decorator_1)
        if msg_type_name == 'call round':
            print (GAME_DATA[0], ' / ', ROUNDS_AVAILABLE)
        else:
            print ('CALL ERROR: Not an available message')
        print(decorator_2)
        print(TXT_SPACER)

## TESTING
# Testing Initialization
foo = GAME_INIT(GAME_DATA)
foo.message_display(TXT_RULE_LONG, 'call round', TXT_RULE_LONG)

# Testing Loop
while foo.game_over() == True:
    foo.importing_data()
    foo.round_over()