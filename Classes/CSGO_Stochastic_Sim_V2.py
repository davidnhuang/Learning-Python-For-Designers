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
class Finality(): # this class handles all the possible endings for the game, which are ties, team A win, team B win

    def __init__(self, Game_Data, Team_Data): # using Game_Data dataset to handle finalities
        self.Game_Data = Game_Data
        self.Team_Data = Team_Data

    def game_tie(self): # this method determines whether the game is a tie or not
        # A tie happens when the max amount of rounds (30) is played and both teams reach 15 round won
        if self.Team_Data[4] == 15 and self.Team_Data[5] == 15 and self.Game_Data[0] == 30:
            print ('Game Tie') # declare a tie


# FUNCTIONS

# MAIN
game_finality = Finality(Game_Data, Team_Data)

Game_Data[0] = 30
Team_Data[4] = 15
Team_Data[5] = 15

game_finality.game_tie()