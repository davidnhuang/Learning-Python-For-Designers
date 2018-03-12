# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 11 2017
# ID 0239637

# todo - takes a list of words as an argument and returns the longest word in the list.
# todo - compare the length of all the strings in the list
# todo - return the word with the longest via index
# hint - int(len(list)) will return the length as an integer so you can start comparing

# Variable
string_list = ["apples", "bananas", "strawberry", "cantaloupes"]

# Main
def longest_word(list):
    for index in range (0, len(list)): # takes index of every string in the list
        longest_word = list[0] # set longest_word as the first string within the list
        for words in list: # for all teh lengths from the range
            if len(words) > len(longest_word): # if the length of the next word is greater than the first
                longest_word = words # pass the word as the longest
    return longest_word

# Output
print ("The longest word in your list is: " + longest_word(string_list))
