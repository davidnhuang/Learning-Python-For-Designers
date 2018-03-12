# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 11 2017
# ID 0239637

import random

# CONSTANTS
NUM_DICE = 5
SIDES_PER_DIE = 6
NUM_TURNS = 3

# VARIABLES
state = 0
playing = True
the_dice = [0] * NUM_DICE
round_number = 0
jackpot_list = []  # empty list for storing all the generated rolls


# ROLL ------------ Function
# rolls and returns the die value
def roll(num_sides):
    return random.randint(1, num_sides)


# MAIN ------------ code begins here
print("""
------------------------------------------------------
                Welcome to Text Dice!
------------------------------------------------------
""")

# game loop - increments game state after each roll
# todo - add scoring of a roll
# todo - add persistent score across rolls
# todo - add a computer player to play against
# todo - add multiple human players

while (playing):
    if state == 0: # sets the round at 0, or start
        round_number += 1 # adds a round to start, so user starts at round 1
        print('-' * 23 + " Round " + str(round_number) + " " + '-' * 23) # graphic print with round number
        cmd = input("(R)oll or (Q)uit> ") # user input to roll or quit out
        if cmd.lower() == "r": # did the user type r?
            for i in range(NUM_DICE): # for all 5 dice, roll based on random from 1 to six
                the_dice[i] = roll(SIDES_PER_DIE)
                state = 1 # now, the program is not longer in start state

    elif state > 0: # if the round is not the first round of the first set
        cmd = input("Enter dice# to re-roll> ") # print this
        # todo - error reporting for bad inputs
        for i in range(NUM_DICE):
            if str(i + 1) in cmd: # ?? This is a weird input for a re roll - if user enters any number from 1 to NUM_ROUNDS
                the_dice[i] = roll(SIDES_PER_DIE) # executes the roll function
                state += 1

    if cmd == "q" or cmd == "Quit": # quits out of the program
        playing = False

    print("Your dice Roll #" + str(state) + ": ", flush=True)

    for i in range(NUM_DICE):
        print("[" + str(the_dice[i]) + "] ", end=' ', flush=True)  # printing out the rolls
        print ("")
        jackpot_list.append(the_dice[i]) # Instead of printing, put the dice into the jackpot_list

    def is_jackpot(list):
        count = 0
        for i in range(0, len(list)-1):# comparing numbers from first to last
            if list[i] == list[i+1]:# comparing a pair of numbers from i to the next; checking if they are the same
                count += 1 # if the pair are the same, count 1
        if count == NUM_DICE - 1: # since the function measures in pairs, there can be only max-1 pairs in a set
            return True # return True if all number pairs are the same

    def jackpot_msg(f): # print this message if it is a jackpot
        if f == True:
            print ("!" * 10 + " JACKPOT " + "!" * 10)

    print (jackpot_msg(is_jackpot(jackpot_list))) # Jackpot Message Print

    if state == NUM_TURNS:
        print("Turn has finished.")
        state = 0

    jackpot_list = []  # Reset the jackpot list for the next roll

print("Goodbye...")
