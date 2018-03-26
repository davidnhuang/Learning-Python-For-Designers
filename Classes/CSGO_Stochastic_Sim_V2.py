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

# CLASSES
class game_mechanism():

    # initializes game mechanics and tournament mechanics
    def __init__(self, Game_Data, Team_Data): # imports data sets Game_Data and Team_Data
        self.Game_Data = Game_Data
        self.Team_Data = Team_Data

    # Tournament Rules
    def rolling_sides(self): # this function rolls for which team gets to go first as ct side
        teams_roll = [self.Team_Data[0], self.Team_Data[2]] # inputs team A side and team B side a roster
        ct_side = teams_roll.pop(random.randint(0,1)) # the way the roll works is by taking out one of the randomly
                                                      # selected teams in the list, which would be labeled as the ct
        t_side = teams_roll[0] # label the remaining team as the t
        sides_rolled = [ct_side, t_side] # arrange the selected sided into a list
        if sides_rolled[0] == self.Team_Data[0]: # if team A is selected as the ct
            self.Team_Data[1] = 'Counter Terrorists' # input Counter Terrorist label
            self.Team_Data[3] = 'Terrorists' # input Terrorist label
            return self.Team_Data
        else: # if team B is rolled as ct
            self.Team_Data[1] = 'Terrorists' # input terrorist label for team A
            self.Team_Data[3] = 'Counter Terrorists' # input terrorist label for team B
            return self.Team_Data

    # Terminal Announcement
    def team_sides_announcement(self):
        print ('=' * 55)
        print (self.Team_Data[0], ' will play as ', self.Team_Data[1])
        print (self.Team_Data[2], ' will play as ', self.Team_Data[3])
        print ('=' * 55)

    # Match mechanics

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