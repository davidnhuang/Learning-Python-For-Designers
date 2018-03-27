# David Huang
# Learning Python for Designers
# CSGO Simulation V2
# March 2018

# IMPORTS
import random
import time

# CONSTANTS
# Team Data
# Dataset format: [team A name, team A side, team B name, team B side, team A score, team B score, team A alive player
# count, team B alive player count, team A ct elimination rate, team B ct elimination rate, team A bomb plant success
# rate, team B bomb plant success rate, team A bomb diffuse success rate, team B bomb deffuse success rate]
Team_Data = ['Team NiP', 'None', 'Team Fnatic', 'None', 0, 0, 5, 5, 48.2, 48.1, 55, 50, 33, 35]

# Game data
# Dataset format: [total rounds played, bomb planted, bomb defused, bomb detonated, game over]
Game_Data = [0, False, False, False, False, False]

# VARIABLES
# Game parameters
counter_terrorist_side = 'Counter Terrorists'
terrorist_side = 'Terrorists'

# FUNCTION
def team_A_t_assign(): # assign team B as terrorists
    Team_Data[1] = terrorist_side  # input terrorist label for team A
    Team_Data[3] = counter_terrorist_side  # input terrorist label for team B
    return Team_Data

def team_B_t_assign(): # assign team B as terrorists
    Team_Data[1] = counter_terrorist_side  # input Counter Terrorist label
    Team_Data[3] = terrorist_side  # input Terrorist label
    return Team_Data

# CLASSES
class game_mechanism():

    # initializes game mechanics and tournament mechanics
    def __init__(self, Game_Data, Team_Data): # imports data sets Game_Data and Team_Data
        self.Game_Data = Game_Data
        self.Team_Data = Team_Data

    # Tournament Rules
    def rolling_sides(self): # rolls for which team gets to go first as ct side
        if Game_Data[0] == 0: # rolls only happen at the beginning of the game
            teams_roll = [self.Team_Data[0], self.Team_Data[2]] # inputs team A side and team B side a roster
            ct_side = teams_roll.pop(random.randint(0,1)) # the way the roll works is by taking out one of the randomly
                                                          # selected teams in the list, which would be labeled as the ct
            t_side = teams_roll[0] # label the remaining team as the t
            sides_rolled = [ct_side, t_side] # arrange the selected sided into a list
            if sides_rolled[0] == self.Team_Data[0]: # if team A is selected as the ct
                team_B_t_assign()
            else: # if team B is rolled as ct
                team_A_t_assign()

    def switching_sides(self):
        if Game_Data[0] == 15: # switching team sides after half-time
            if self.Team_Data[1] == counter_terrorist_side: # if team A is ct side
                team_A_t_assign()
            else: # if team B is ct side
                team_B_t_assign()

    # Terminal Announcement
    def team_sides_announcement(self): # this function handles all announcement prompts
        print ('=' * 55) # decoration
        if Game_Data[0] == 15: # at half time
            print ('Half time, switching sides...') # print switching side prompt
        if Game_Data[0] == 0 or Game_Data[0] == 15: # either at half time or beginning of the game
            print (self.Team_Data[0], ' will play as ', self.Team_Data[1]) # announce sides
            print (self.Team_Data[2], ' will play as ', self.Team_Data[3])
        print ('=' * 55) # decoration

    # Game Finality
    def game_tie(self): # this method determines whether the game is a tie or not
        # A tie happens when the max amount of rounds (30) is played and both teams reach 15 round won
        if self.Team_Data[4] == 15 and self.Team_Data[5] == 15 and self.Game_Data[0] == 30:
            print ('Game Tie') # declare a tie

    def game_winner(self): # this method determines whether there is a victor in the game and print their victory prompt
        if self.Team_Data[4] == 16: # A team wins the game if they reach 16 rounds first
            print (self.Team_Data[0], 'clinched the game with 16 rounds won') # print team A win message
        elif self.Team_Data[5] == 16: # B team wins the game if they reach 16 rounds first
            print (self.Team_Data[2], 'clinched the game with 16 rounds won') # print team B win message

# MAIN
# initialize game
tournament = game_mechanism(Game_Data, Team_Data)

# first half
tournament.rolling_sides()
tournament.team_sides_announcement()

# game ending
tournament.game_tie() # declares a tie
tournament.game_winner() # declares a winner