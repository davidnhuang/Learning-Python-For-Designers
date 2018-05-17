# Daviarea=None Learning Python for Designers
# CSGO Simulation V2
# March 2018

# Don't write useless code
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

## DATA SET
TEAM_A_DATA = [team_A_ID, team_A_ct_elim_rate, team_A_t_plant_rate, team_A_ct_defuse_rate, team_A_side]
TEAM_B_DATA = [team_B_ID, team_B_ct_elim_rate, team_B_t_plant_rate, team_B_ct_defuse_rate, team_B_side]

GAME_METADATA = [rounds_played_tally,
                 team_A_players, team_B_players,
                 team_A_points, team_B_points,
                 bomb_planted, # if bomb is planted by t side, return true
                 bomb_defused, # if bomb is planted and defused, return true
                 bomb_plant_limit] # if bomb has been planted once, it cannot be planted again

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

## CLASSES
class SETUP:

    def __init__(self, TEAM_A_DATA, TEAM_B_DATA, GAME_METADATA):
        self.TEAM_A_DATA = TEAM_A_DATA
        self.TEAM_B_DATA = TEAM_B_DATA
        self.GAME_DATA = GAME_METADATA

    def call_data(self, SORTED_LIST, TEAM_SIDE, CALLED_DATA_TYPE):
        called_data = SORTED_LIST[TEAM_SIDE][CALLED_DATA_TYPE]
        print (called_data)

    def rolling_sides(self):
        if GAME_METADATA[0] == 0 or GAME_METADATA[0] == HALFTIME_ROUND:
            # rolling for which team plays as ct first
            rolling_teams = [TEAM_A_DATA[TEAM_NAME],TEAM_B_DATA[TEAM_NAME]]
            rolled_ct_team = rolling_teams.pop(random.randint(0,1))
            rolled_t_team = rolling_teams[0]
            team_decided_roles = [rolled_ct_team, rolled_t_team]
            # importing data based on deciding
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

    def game_over(self, GAME_METADATA):
        if GAME_METADATA[0] <= ROUNDS_AVAILABLE:
            if GAME_METADATA[3] == WINNING_ROUND or GAME_METADATA[4] == WINNING_ROUND:
                return True
            elif GAME_METADATA[3] == HALFTIME_ROUND and GAME_METADATA[4] == HALFTIME_ROUND:
                return True
        else:
            return False

## TEST
class TESTING:

    def __init__(self, SORTED_TEAM_DATA, GAME_METADATA):
        self.SORTED_TEAM_DATA = SORTED_TEAM_DATA
        self.GAME_METADATA = GAME_METADATA

    def basic_count(self, search_term, search_area):
        search_count = 0
        if search_area == search_term:
            search_count += 1
        print (search_count)

# print test
TEMP_NAME = SETUP(TEAM_A_DATA, TEAM_B_DATA, GAME_METADATA)
TESTING = TESTING(TEMP_NAME, GAME_METADATA)

## MAIN
if TEMP_NAME.game_over(GAME_METADATA) == True:
    GAME_METADATA[0]+= 1
    print ('game happening')
else:
    print ('game over')
    print (GAME_METADATA[0])
