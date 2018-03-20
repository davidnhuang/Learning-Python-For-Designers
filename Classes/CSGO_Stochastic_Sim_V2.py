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
Team_Dataset = ['Team NiP', 'None', 'Team Fnatic', 'None', 0, 0, 5, 5, 48.2, 48.1, 55, 50, 33, 35]

# Game data
# Dataset format: [total rounds played, bomb planted, bomb defused, bomb detonated]
Game_Data = [0, False, False, False]

# VARIABLES


# CLASSES
class Team():

    def __init__(self, Team_Data):
        self.Team_Data = Team_Data

class Game():

    def __init__(self, Game_Data):
        self.Game_Data = Game_Data

    def ct_win_msg(self):
        
# FUNCTIONS

# MAIN