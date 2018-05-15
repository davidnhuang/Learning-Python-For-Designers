# David Huang
# Learning Python for Designers
# CSGO Simulation V2
# March 2018

# Good Rule of Thumb - Before you write more code, test to see if it works first in the main loop

## IMPORTS
import random

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
team_A_name = 'Team NiP' # name for Team A
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
team_B_name = 'Team Fnatic' # name for Team B
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
TEAM_DATA = [team_A_name, team_B_name, # ID for teams
             team_A_side, team_B_side, # Sides for teams
             team_A_points, team_B_points, # points tally for both teams
             team_A_players, team_B_players, # number of players alive on both teams
             team_A_ct_elim_rate, team_B_ct_elim_rate, # elimination rates for both teams
             team_A_t_plant_rate, team_B_t_plant_rate, # bomb planted rates for both teams
             team_A_ct_defuse_rate, team_B_ct_defuse_rate, # bomb defused rates for both teams
             ]

GAME_DATA = [rounds_played_tally, # stores total number of rounds played by both sides
             bomb_planted, # if bomb is planted by t side, return true
             bomb_defused, # if bomb is planted and defused, return true
             bomb_plant_limit] # if bomb has been planted once, it cannot be planted again

TEMP_CT_DATA = [] # temporary memory to import data for CT based on selected CT side
TEMP_T_DATA = [] # temporary memory to import data for T based on selected T side

## MESSAGES
msg_bomb_plant = 'Bomb has been planted!'
msg_ct_victory = 'Counter terrorists win!'
msg_t_victory = 'Terrorists win!'

## CLASSES
class SETUP:

    def __init__(self, TEAM_DATA, GAME_DATA):
        self.TEAM_DATA = TEAM_DATA
        self.GAME_DATA = GAME_DATA

    def deciding_sides(self):
        rolling_teams = [TEAM_DATA[0],TEAM_DATA[1]]
        ct_team_decided = rolling_teams.pop(random.randint(0,1))
        t_team_decided = rolling_teams[0]
        team_decided_roles = [ct_team_decided, t_team_decided]
        return team_decided_roles


class MECHANICS:

    def __init__(self, TEAM_DATA, GAME_DATA):
        self.TEAM_DATA = TEAM_DATA
        self.GAME_DATA = GAME_DATA

## MAIN

## TEST
# print test
foo = SETUP(TEAM_DATA, GAME_DATA)
foo.deciding_sides()
print (foo.deciding_sides()[0])