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

# CLASSES
class game_mechanism():

    def __init__(self, Game_Data, Team_Data):
        self.Game_Data = Game_Data
        self.Team_Data = Team_Data

    def roll_side(self):

class game_outcome(): # this class handles all the possible endings for the game, which are ties, team A win, team B win

    def __init__(self, Game_Data, Team_Data): # using Game_Data dataset to handle game outcomes
        self.Game_Data = Game_Data # this allows the class to import the datasets from Game Data
        self.Team_Data = Team_Data # this allows the class to import the datasets from Team Data

    def game_tie(self): # this method determines whether the game is a tie or not
        # A tie happens when the max amount of rounds (30) is played and both teams reach 15 round won
        if self.Team_Data[4] == 15 and self.Team_Data[5] == 15 and self.Game_Data[0] == 30:
            print ('Game Tie') # declare a tie

    def game_winner(self): # this method determines whether there is a victor in the game and print their victory prompt
        if self.Team_Data[4] == 16: # A team wins the game if they reach 16 rounds won
            print (self.Team_Data[0], 'clinched the game with 16 rounds won')
        elif self.Team_Data[5] == 16:
            print (self.Team_Data[2], 'clinched the game with 16 rounds won')


# FUNCTIONS

# MAIN
outcome = game_outcome(Game_Data, Team_Data)

Team_Data[4] = 16
Team_Data[5] = 10

outcome.game_tie() # declares a tie
outcome.game_winner() # declares a winner