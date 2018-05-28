# David Huang
# Learning Python for Designers
# CSGO Simulation V2

## IMPORTS
import random
import time

## CONSTANT
ROUNDS_AVAILABLE = 30
HALFTIME_ROUND = int(ROUNDS_AVAILABLE/2)
WINNING_ROUND = HALFTIME_ROUND+1
DEFAULT_PLAYER_COUNT = 5
DEFAULT_TEAM_SCORE = 0
DEFAULT_TEAM_SIDE = None
STARTING_ROUND = 0
CT_SIDE = 'Counter Terrorists'
T_SIDE = 'Terrorists'
HALVES_AVAILABLE = int(ROUNDS_AVAILABLE / HALFTIME_ROUND)

## TEAM INFO
# Team A Stats
team_A_ID = 'Team NiP' # name
team_A_side = DEFAULT_TEAM_SIDE # what side currently playing as, ct or t
team_A_points = DEFAULT_TEAM_SCORE # score
team_A_players = DEFAULT_PLAYER_COUNT # players alive
team_A_ct_elim_rate = 48.2
team_A_t_plant_rate = 55
team_A_ct_defuse_rate = 33
# Team B Stats
team_B_ID = 'Team Fnatic' # name
team_B_side = DEFAULT_TEAM_SIDE # what side currently playing as, ct or t
team_B_points = DEFAULT_TEAM_SCORE # team B score; starts at 0
team_B_players = DEFAULT_PLAYER_COUNT # players alive
team_B_ct_elim_rate = 48.1
team_B_t_plant_rate = 53
team_B_ct_defuse_rate = 32
team_exchange_survival = 6 # chance of both teams surviving a gun exchange
## GAME ENVIRONMENT
bomb_planted = False # at the start of each round, bomb is always not planted
bomb_defused = False # at the start of each round, because bomb is not planted, bomb is not defused
bomb_plant_limit = False # terrorists only have one chance to plant and detonate bomb; they can't plant twice
rounds_played_tally = 0 # tallies the total number of rounds played and concluded
bomb_detonated = False

## Lists
# Teams
TEAM_A_STATS = [team_A_ID, team_A_ct_elim_rate, team_A_t_plant_rate, team_A_ct_defuse_rate, team_A_side, team_A_players, team_A_points]
TEAM_B_STATS = [team_B_ID, team_B_ct_elim_rate, team_B_t_plant_rate, team_B_ct_defuse_rate, team_B_side, team_B_players, team_B_points]
TEAM_A = 0
TEAM_B = 1
TEAM_ID = 0
TEAM_CT_KD = 1
TEAM_PLANT_RATE = 2
TEAM_DEFUSE_RATE = 3
TEAM_SIDE = 4
PLAYER_COUNT = 5
POINTS = 6
# Game
GAME_STATES = [rounds_played_tally, bomb_planted, bomb_defused, bomb_plant_limit, bomb_detonated,]
CURRENT_ROUND = 0
PLANT_STATE = 1
DEFUSE_STATE = 2
PLANT_LIMIT = 3
DETONATED = 4

## TEXT DECORATION
TXT_SPACER = ' '
TXT_RULE_LONG = '-'*50
TXT_RULE_SHORT = '-'*25
TXT_DOUBLE_RULE_LONG = '='*50
TXT_DOUBLE_RULE_SHORT = '='*25

## GLOBAL COMPONENTS
def pause(sleep_time):
    time.sleep(sleep_time)

## CLASSES
class INIT_GAME:

    def __init__(self, GAME_STATES):
        self.GAME_STATES = GAME_STATES

    def input(self, msg_type_name):
        if msg_type_name == 'start':
            input('Start simulation? (Y)es or (N)o')

    def display(self, msg_type_name):
        print(TXT_SPACER)
        if msg_type_name == 'call round':
            print(TXT_RULE_LONG)
            print('Round ', GAME_STATES[0] + 1, ' / ', ROUNDS_AVAILABLE)
            print(TXT_RULE_LONG)
        elif msg_type_name == 'call round winner':
            print(TXT_RULE_LONG)
            print('Team Winner')
            print(TXT_RULE_LONG)
        elif msg_type_name == 'spacer':
            return None
        elif msg_type_name == 'intro':
            print('Welcome to the championship match of ESL Tournament')
            print('This will be a game between', TEAM_A_STATS[TEAM_ID], 'and', TEAM_B_STATS[TEAM_ID])
        elif msg_type_name == 'planted':
            print('Bomb has been planted!')
        elif msg_type_name == 'sides':
            if GAME_STATES[0] == STARTING_ROUND or GAME_STATES[0] == HALFTIME_ROUND+1:
                print(TEAM_A_STATS[TEAM_ID], 'will play as', TEAM_A_STATS[TEAM_SIDE])
                print(TEAM_B_STATS[TEAM_ID], 'will play as', TEAM_B_STATS[TEAM_SIDE])
        elif msg_type_name == 'rolling':
            print('Rolling sides...')
            pause(3)
        elif msg_type_name == 'switching':
            print('Switching sides...')
            pause(3)
        elif msg_type_name == 'scorekeeper':
            print(TEAM_A_STATS[TEAM_ID], ':', TEAM_A_STATS[POINTS], ' | ', TEAM_B_STATS[TEAM_ID], ':', TEAM_B_STATS[POINTS])
        elif msg_type_name == 'start':
            if self.input('start') == 'Y' or self.input('start') == 'y':
                print('Starting...')
                pause(3)
            elif self.input('start') == 'N' or self.input('start') == 'n':
                print('Simulation canceled')
        else:
            print('CALL ERROR: Not an available message type')
        print(TXT_SPACER)

    def rolling_sides(self):
        if GAME_STATES[0] == STARTING_ROUND:
            self.display('rolling')
            rolling_teams = [TEAM_A_STATS[TEAM_ID],TEAM_B_STATS[TEAM_ID]]
            rolled_ct_team = rolling_teams.pop(random.randint(0,1))
            rolled_t_team = rolling_teams[0]
            decided_side = [rolled_ct_team, rolled_t_team]
            return decided_side

    def switching_sides(self, first_half_teams):
        self.display('switching')
        if first_half_teams[TEAM_A][TEAM_ID] == TEAM_A_STATS[TEAM_ID]:
            flipped_teams = [TEAM_B_STATS[TEAM_ID], TEAM_A_STATS[TEAM_ID]]
            return flipped_teams
        else:
            flipped_teams = [TEAM_A_STATS[TEAM_ID], TEAM_B_STATS[TEAM_ID]]
            return flipped_teams

    def assigning_stats(self, decided_side):
        if decided_side[TEAM_A] == TEAM_A_STATS[TEAM_ID]:
            TEAM_A_STATS[TEAM_SIDE] = CT_SIDE
            TEAM_B_STATS[TEAM_SIDE] = T_SIDE
            DATA_FORMATION = [TEAM_A_STATS, TEAM_B_STATS]
            return DATA_FORMATION
        else:
            TEAM_A_STATS[TEAM_SIDE] = T_SIDE
            TEAM_B_STATS[TEAM_SIDE] = CT_SIDE
            DATA_FORMATION = [TEAM_B_STATS, TEAM_A_STATS]
            return DATA_FORMATION

    def round_reset(self):
        GAME_STATES[0] += 1
        GAME_STATES[1] = False
        GAME_STATES[2] = False
        GAME_STATES[3] = 0
        GAME_STATES[4] = False
        TEAM_A_STATS[PLAYER_COUNT] = DEFAULT_PLAYER_COUNT
        TEAM_B_STATS[PLAYER_COUNT] = DEFAULT_PLAYER_COUNT

    def terminate(self):
        if TEAM_A_STATS[POINTS] == WINNING_ROUND and GAME_STATES[0] < ROUNDS_AVAILABLE or \
        TEAM_B_STATS[POINTS] == WINNING_ROUND and GAME_STATES[0] < ROUNDS_AVAILABLE or \
        TEAM_A_STATS[POINTS] == HALFTIME_ROUND and TEAM_B_STATS[POINTS] == HALFTIME_ROUND and GAME_STATES[0] == ROUNDS_AVAILABLE:
            return True

## TESTING
GAME = INIT_GAME(GAME_STATES)

GAME.display('intro')
GAME.input('start')

TEAMS_DECIDED = GAME.assigning_stats(GAME.rolling_sides())
for GAME_HALVES in range (HALVES_AVAILABLE):
    if GAME_STATES[0] == HALFTIME_ROUND:
        TEAMS_DECIDED = GAME.assigning_stats(GAME.switching_sides(TEAMS_DECIDED))
    for rounds in range (HALFTIME_ROUND):
        GAME.display('sides')
        GAME.display('call round')
        GAME.display('scorekeeper')
        GAME.round_reset()
        if GAME.terminate() == True:
            break