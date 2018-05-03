# David Huang
# Learning Python for Designers
# CSGO Simulation V2
# March 2018

# Good Rule of Thumb - Before you write more code, test to see if it works first in the main loop

## CONSTANT
ROUNDS_AVAILABLE = 30 # there are only 30 rounds in one game to play
HALFTIME_ROUND = int(ROUNDS_AVAILABLE/2) # halftime is the round at the midpoint of the game
WINNING_ROUND = HALFTIME_ROUND+1 # team who wins 1 more than half the available round first wins the game
DEFAULT_PLAYER_COUNT = 5 # determines how many players are alive at the start of each round
DEFAULT_TEAM_SCORE = 0 # determines score teams start with
DEFAULT_TEAM_SIDE = None # starting sides for teams in the beginning

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

## DATA FORMATTING
# TODO - Data Reformatting - create flexible and manageable data sets for the game
TEAM_DATA = [team_A_name, team_B_name, # ID for teams
             team_A_side, team_B_side, # Sides for teams
             team_A_points, team_B_points, # points tally for both teams
             team_A_players, team_B_players, # number of players alive on both teams
             team_A_ct_elim_rate, team_B_ct_elim_rate, # elimination rates for both teams
             team_A_t_plant_rate, team_B_t_plant_rate, # bomb planted rates for both teams
             team_A_ct_defuse_rate, team_B_ct_defuse_rate, # bomb defused rates for both teams
             team_exchange_survival
             ]

GAME_DATA = []


## VARIABLES

## FUNCTIONS

## CLASSES

## MAIN

## TEST
# print test
print (Team_Data[4], Team_Data[5])