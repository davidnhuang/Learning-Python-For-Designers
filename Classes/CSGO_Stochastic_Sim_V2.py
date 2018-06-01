# David Huang
# Learning Python for Designers
# CSGO Simulation V2

## IMPORTS
import random
import time

## TEST SWTICH
ON = False
OFF = True

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
team_A_t_elim_rate = 45.7
team_A_t_plant_rate = 55
team_A_ct_defuse_rate = 33
# Team B Stats
team_B_ID = 'Team Fnatic' # name
team_B_side = DEFAULT_TEAM_SIDE # what side currently playing as, ct or t
team_B_points = DEFAULT_TEAM_SCORE # team B score; starts at 0
team_B_players = DEFAULT_PLAYER_COUNT # players alive
team_B_ct_elim_rate = 48.1
team_B_t_elim_rate = 47.8
team_B_t_plant_rate = 53
team_B_ct_defuse_rate = 32
team_exchange_survival = 6 # chance of both teams surviving a gun exchange
detonation_chance = 5
## GAME ENVIRONMENT
bomb_planted = False # at the start of each round, bomb is always not planted
bomb_defused = False # at the start of each round, because bomb is not planted, bomb is not defused
bomb_plant_limit = False # terrorists only have one chance to plant and detonate bomb; they can't plant twice
rounds_played_tally = 0 # tallies the total number of rounds played and concluded
bomb_detonated = False

## Lists
# Teams
TEAM_A_STATS = [team_A_ID, team_A_ct_elim_rate, team_A_t_elim_rate, team_A_t_plant_rate, team_A_ct_defuse_rate, team_A_side, team_A_players, team_A_points]
TEAM_B_STATS = [team_B_ID, team_B_ct_elim_rate, team_B_t_elim_rate, team_B_t_plant_rate, team_B_ct_defuse_rate, team_B_side, team_B_players, team_B_points]
TEAM_ID = 0
TEAM_CT_KD = 1
TEAM_T_KD = 2
TEAM_PLANT_RATE = 3
TEAM_DEFUSE_RATE = 4
TEAM_SIDE = 5
PLAYER_COUNT = 6
POINTS = 7
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

PISTOL = ['Glock-18', 'P250', 'Tec-9', 'Desert Eagle', 'Dual Berettas', 'CZ75 Auto', 'R8 Revolver', 'P2000', 'USP-S']
RIFLE = ['MAC-10', 'PP-Bizon', 'UMP-45', 'Galil AR', 'AK-47', 'M4A4', 'M4A1-S', 'SSG-08', 'AWP']
glados_words = ['We hope your brief detention in the relaxation vault has been a pleasant one.',
          'Perfect. Please move quickly to the chamberlock, as the effects of prolonged exposure to the Button are not part of this test.',
          'The cake is a lie',
          'Please escort your Companion Cube to the Aperture Science Emergency Intelligence Incinerator.']

test_switch = ON

## GLOBAL COMPONENTS
def pause(sleep_time):
    if test_switch == OFF:
        time.sleep(sleep_time)
    elif test_switch == ON:
        time.sleep(0)

def no_exchange(team_ct_kd):
    return team_ct_kd[TEAM_CT_KD] + team_exchange_survival

def glados():
    quote_selection = random.randint(0,3)
    print(glados_words[quote_selection])

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
        elif msg_type_name == 'intro':
            print('Welcome to the Counter Strike Global Offensive game simulator')
            print('This will be a simulated game between', TEAM_A_STATS[TEAM_ID], 'and', TEAM_B_STATS[TEAM_ID])
        elif msg_type_name == 'sides':
            print(TEAM_A_STATS[TEAM_ID], 'will play as', TEAM_A_STATS[TEAM_SIDE])
            print(TEAM_B_STATS[TEAM_ID], 'will play as', TEAM_B_STATS[TEAM_SIDE])
        elif msg_type_name == 'rolling':
            print('Rolling sides...')
        elif msg_type_name == 'switching':
            print('Half time. Switching sides...')
        elif msg_type_name == 'scorekeeper':
            print(TEAM_A_STATS[TEAM_ID], ':', TEAM_A_STATS[POINTS], ' | ', TEAM_B_STATS[TEAM_ID], ':', TEAM_B_STATS[POINTS])
        elif msg_type_name == 'no kill':
            print('No one is killed yet.')
        elif msg_type_name == 'bomb plant':
            print('Bomb has been planted!')
        elif msg_type_name == 'defusing':
            print('Defusing...')
        elif msg_type_name == 'remaining':
            if TEAM_A_STATS[TEAM_SIDE] == CT_SIDE:
                print(CT_SIDE, TEAM_A_STATS[PLAYER_COUNT], 'vs.', T_SIDE, TEAM_B_STATS[PLAYER_COUNT])
            else:
                print(CT_SIDE, TEAM_B_STATS[PLAYER_COUNT], 'vs.', T_SIDE, TEAM_A_STATS[PLAYER_COUNT])
            print(TXT_SPACER)
        elif msg_type_name == 'defused':
            print('Bomb has been defused!')
        else:
            print('CALL ERROR: Not an available message type')
        print(TXT_SPACER)
        pause(1)

    def kill_log(self, killer, killed):
        print(killer, 'killed a player in', killed)

    def weapon_use(self):
        if GAME_STATES[CURRENT_ROUND] == 1 or GAME_STATES[CURRENT_ROUND] == HALFTIME_ROUND:
            return PISTOL[random.randint(0,len(PISTOL)-1)]
        else:
            return RIFLE[random.randint(0,len(RIFLE)-1)]

    def exchange_log(self, team, opposition):
        print(TXT_SPACER)
        print(team, 'killed a player on' ,opposition, 'with', self.weapon_use())
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

    def round_active(self):
        if TEAM_A_STATS[PLAYER_COUNT] > 0 and TEAM_B_STATS[PLAYER_COUNT] > 0:
            return True
        else:
            return False

    def bomb_has_been_planted(self):
        GAME_STATES[PLANT_STATE] = True
        GAME_STATES[PLANT_LIMIT] = True
        self.display('bomb plant')

    def probability_engine(self, team_a, team_b, type, kill_type):
        if type == 'kill':
            if random.randint(0,100) <= int(team_a[kill_type]):
                team_b[PLAYER_COUNT] -= 1
                self.kill_log(team_a[TEAM_ID], team_b[TEAM_ID])
            else:
                team_a[PLAYER_COUNT] -= 1
                self.kill_log(team_b[TEAM_ID], team_a[TEAM_ID])
        if type == 'plant':
            if random.randint(0,100) <= int(team_a[TEAM_PLANT_RATE]):
                self.bomb_has_been_planted()
            else:
                self.bomb_has_been_planted()
        if type == 'defuse':
            if random.randint(0,100) <= int(team_a[TEAM_DEFUSE_RATE]):
                return True
            else:
                return False

    def kill(self, team_a, team_b):
        if team_a[TEAM_SIDE] == CT_SIDE:
            self.probability_engine(team_a, team_b, 'kill', TEAM_CT_KD)
        else:
            self.probability_engine(team_b, team_a, 'kill', TEAM_CT_KD)

    def bomb_plant_confidence(self):
        if TEAM_A_STATS[TEAM_SIDE] == T_SIDE:
            if TEAM_A_STATS[PLAYER_COUNT] - TEAM_B_STATS[PLAYER_COUNT] >= 2 or TEAM_A_STATS[PLAYER_COUNT] >= 1 and TEAM_B_STATS[PLAYER_COUNT] == 1:
                return True
        else:
            if TEAM_B_STATS[PLAYER_COUNT] - TEAM_A_STATS[PLAYER_COUNT] >= 2 or TEAM_B_STATS[PLAYER_COUNT] >= 1 and TEAM_A_STATS[PLAYER_COUNT] == 1:
                return True

    def bomb_plant(self, team_a, team_b):
        if GAME_STATES[PLANT_LIMIT] == False and self.bomb_plant_confidence() == True:
            if team_a[TEAM_SIDE] == T_SIDE:
                self.probability_engine(team_a, team_b, 'plant', TEAM_CT_KD)
            else:
                self.probability_engine(team_b, team_a, 'plant', TEAM_CT_KD)

    def defuse(self, team_a, team_b):
        if GAME_STATES[PLANT_STATE] == True:
            if team_a[TEAM_SIDE] == CT_SIDE and team_a[PLAYER_COUNT] > 0 and team_b[PLAYER_COUNT] <= 3:
                self.display('defusing')
                if self.probability_engine(team_a, team_b, 'defuse', TEAM_CT_KD) == True:
                    GAME_STATES[DEFUSE_STATE] = True
                    self.display('defused')
            elif team_b[TEAM_SIDE] == CT_SIDE and team_b[PLAYER_COUNT] > 0 and team_a[PLAYER_COUNT] <= 3:
                self.display('defusing')
                if self.probability_engine(team_b, team_a, 'defuse', TEAM_CT_KD) == True:
                    GAME_STATES[DEFUSE_STATE] = True
                    self.display('defused')

    def round_reset(self):
        GAME_STATES[CURRENT_ROUND] += 1
        GAME_STATES[PLANT_STATE] = False
        GAME_STATES[DEFUSE_STATE] = False
        GAME_STATES[PLANT_LIMIT] = False
        GAME_STATES[DETONATED] = False
        TEAM_A_STATS[PLAYER_COUNT] = DEFAULT_PLAYER_COUNT
        TEAM_B_STATS[PLAYER_COUNT] = DEFAULT_PLAYER_COUNT

    def add_point(self,team):
        team[POINTS] += 1
        print(TXT_SPACER)
        print(team[TEAM_SIDE], 'win!')
        print(TXT_SPACER)

    def side_specific_point(self, side):
        if TEAM_A_STATS[TEAM_SIDE] == side:
            self.add_point(TEAM_A_STATS)
        elif TEAM_B_STATS[TEAM_SIDE] == side:
            self.add_point(TEAM_B_STATS)

    def round_winner(self):
        if TEAM_A_STATS[PLAYER_COUNT] == 0:
            self.add_point(TEAM_B_STATS)
        elif TEAM_B_STATS[PLAYER_COUNT] == 0:
            self.add_point(TEAM_A_STATS)
        elif GAME_STATES[DETONATED] == True:
            self.side_specific_point(T_SIDE)
        elif GAME_STATES[DEFUSE_STATE] == True:
            self.side_specific_point(CT_SIDE)

    def start(self):
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

    def main(self):
        self.kill(TEAM_A_STATS,TEAM_B_STATS)
        self.display('remaining')
        self.bomb_plant(TEAM_A_STATS, TEAM_B_STATS)
        self.defuse(TEAM_A_STATS, TEAM_B_STATS)

## TESTING
GAME = INIT_GAME(GAME_STATES)
GAME.display('intro')
STARTING_SIMULATION = input('Start simulation? (Y)es or (N)o : ')
if STARTING_SIMULATION == 'Y' or STARTING_SIMULATION == 'y':
    GAME.start()
    for HALVES in range (HALVES_AVAILABLE):
        if GAME_STATES[CURRENT_ROUND] == HALFTIME_ROUND:
            GAME.halftime()
        for rounds in range (HALFTIME_ROUND):
            GAME.display('call round')
            while GAME.round_active() == True:
                GAME.main()
            GAME.round_winner()
            GAME.round_reset()
            GAME.display('scorekeeper')
            if GAME.terminate() == True:
                break
elif STARTING_SIMULATION == 'N' or STARTING_SIMULATION == 'n':
    print('Exited.')
elif STARTING_SIMULATION == 'Glados':
    glados()
else:
    print('Exited.')