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
# Glados
because_we_can = ['We hope your brief detention in the relaxation vault has been a pleasant one.',
          'Perfect. Please move quickly to the chamberlock, as the effects of prolonged exposure to the Button are not part of this test.',
          'The cake is a lie',
          'Please escort your Companion Cube to the Aperture Science Emergency Intelligence Incinerator.']

## GLOBAL COMPONENTS
def pause(sleep_time):
    time.sleep(sleep_time)

def we_do_what_we_must():
    quote_selection = random.randint(0,3)
    print(because_we_can[quote_selection])

## CLASSES
class INIT_GAME:

    def __init__(self, GAME_STATES):
        self.GAME_STATES = GAME_STATES

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
            print('Welcome to the Counter Strike Global Offensive game simulator')
            print('This will be a simulated game between', TEAM_A_STATS[TEAM_ID], 'and', TEAM_B_STATS[TEAM_ID])
        elif msg_type_name == 'planted':
            print('Bomb has been planted!')
        elif msg_type_name == 'sides':
            print(TEAM_A_STATS[TEAM_ID], 'will play as', TEAM_A_STATS[TEAM_SIDE])
            print(TEAM_B_STATS[TEAM_ID], 'will play as', TEAM_B_STATS[TEAM_SIDE])
        elif msg_type_name == 'rolling':
            print('Rolling sides...')
        elif msg_type_name == 'switching':
            print('Half time. Switching sides...')
        elif msg_type_name == 'scorekeeper':
            print(TEAM_A_STATS[TEAM_ID], ':', TEAM_A_STATS[POINTS], ' | ', TEAM_B_STATS[TEAM_ID], ':', TEAM_B_STATS[POINTS])
        else:
            print('CALL ERROR: Not an available message type')
        print(TXT_SPACER)

    def assign_ct_b(self):
        TEAM_A_STATS[TEAM_SIDE] = T_SIDE
        TEAM_B_STATS[TEAM_SIDE] = CT_SIDE

    def assign_ct_a(self):
        TEAM_A_STATS[TEAM_SIDE] = CT_SIDE
        TEAM_B_STATS[TEAM_SIDE] = T_SIDE

    def rolling_sides(self):
        if GAME_STATES[CURRENT_ROUND] == STARTING_ROUND:
            self.display('rolling')
            rolling_teams = [TEAM_A_STATS[TEAM_ID],TEAM_B_STATS[TEAM_ID]]
            rolled_ct_team = rolling_teams.pop(random.randint(0,1))
            rolled_t_team = rolling_teams[0]
            decided_side = [rolled_ct_team, rolled_t_team]
            return decided_side

    def assigning_team(self):
        if TEAM_A_STATS[TEAM_SIDE] == CT_SIDE:
            self.assign_ct_a()
        else:
            self.assign_ct_b()

    def switching_sides(self):
        self.display('switching')
        if TEAM_A_STATS[TEAM_ID] == CT_SIDE:
            self.assign_ct_b()
        else:
            self.assign_ct_a()

    def round_reset(self):
        GAME_STATES[CURRENT_ROUND] += 1
        GAME_STATES[PLANT_STATE] = False
        GAME_STATES[DEFUSE_STATE] = False
        GAME_STATES[PLANT_LIMIT] = 0
        GAME_STATES[DETONATED] = False
        TEAM_A_STATS[PLAYER_COUNT] = DEFAULT_PLAYER_COUNT
        TEAM_B_STATS[PLAYER_COUNT] = DEFAULT_PLAYER_COUNT

    def starting_simulation(self):
        self.rolling_sides()
        self.assigning_team()
        self.display('sides')

    def halftime(self):
        self.switching_sides()
        self.display('sides')

    def terminate(self):
        if TEAM_A_STATS[POINTS] == WINNING_ROUND and GAME_STATES[CURRENT_ROUND] < ROUNDS_AVAILABLE or \
        TEAM_B_STATS[POINTS] == WINNING_ROUND and GAME_STATES[CURRENT_ROUND] < ROUNDS_AVAILABLE or \
        TEAM_A_STATS[POINTS] == HALFTIME_ROUND and TEAM_B_STATS[POINTS] == HALFTIME_ROUND and GAME_STATES[0] == ROUNDS_AVAILABLE:
            return True

    def round_winner(self, winner_team):
        winner_team[POINTS] += 1

    def team_elimination(self):
        if TEAM_A_STATS[PLAYER_COUNT] == 0:
            self.round_winner(TEAM_B_STATS)
        elif TEAM_B_STATS[PLAYER_COUNT] == 0:
            self.round_winner(TEAM_A_STATS)

    def ct_win(self):
        if GAME_STATES[DEFUSE_STATE] == True:
            if TEAM_A_STATS[TEAM_SIDE] == CT_SIDE:
                self.round_winner(TEAM_A_STATS)
            else:
                self.round_winner(TEAM_B_STATS)

    def t_win(self):
        if GAME_STATES[DETONATED] == True:
            if TEAM_A_STATS[TEAM_SIDE] == T_SIDE:
                self.round_winner(TEAM_A_STATS)
            else:
                self.round_winner(TEAM_B_STATS)

    def round_over(self):
        self.team_elimination()
        self.ct_win()
        self.t_win()
        self.round_reset()

    def player_encounter(self):
        if TEAM_A_STATS[TEAM_SIDE] == CT_SIDE:
            if random.randint(0,100) <= int()

#    def game_round(self):
#        while TEAM_A_STATS[PLAYER_COUNT] > 0 and TEAM_B_STATS[PLAYER_COUNT] > 0:

## TESTING
GAME = INIT_GAME(GAME_STATES)
GAME.display('intro')
STARTING_SIMULATION = input('Start simulation? (Y)es or (N)o : ')
if STARTING_SIMULATION == 'Y' or STARTING_SIMULATION == 'y':
    GAME.starting_simulation()
    for GAME_HALVES in range (HALVES_AVAILABLE):
        if GAME_STATES[CURRENT_ROUND] == HALFTIME_ROUND:
            GAME.halftime()
        for rounds in range (HALFTIME_ROUND):
            GAME.display('call round')
            GAME.display('scorekeeper')
            GAME.round_over()
            if GAME.terminate() == True:
                break
elif STARTING_SIMULATION == 'N' or STARTING_SIMULATION == 'n':
    print('Exited.')
else:
    we_do_what_we_must()