# NAME: David Huang
# DATE: 10 / 4 / 2017
# ID Number: 0239637
# Change log: 1.1

# MAIN
# user input sentence
input_message = input("enter sentence: ")

# determine how many letters are in the sentence, including spaces and commas
letter_place = len(input_message) # - 1 because 0 is the first index

# telling the computer to refer to the range of the user input
def cipher_func(x): #  cipher function is replacing one letter for another; one at a time
    while x <= letter_place: # keep looping until the end of the sentence
        if ord(input_message[x]) == 32 or ord(input_message[x]) == 44: # testing if it is a ',' or a ' '
            return chr(ord(input_message[x])) # if it is, skip and don't change
        # since the difference between 'x' becoming an 'a' is ASCII decrease of 23, the desired outcome can be achieved -
        # by simply -23 for anything within ord(120 ~ 122) and ord(88 ~ 90)
        if 122 >= ord(input_message[x]) >= 120 or 90 >= ord(input_message[x]) >= 88:
            return chr(ord(input_message[x]) - 23)
        else:
            return chr(ord(input_message[x]) + 3) # if it does not fall under any of the above categories, shift over by 3

# parsing the string back together with ciphered values
print ("ciphered sentence: ", end=' ')
for c in range (0, letter_place): # replacing every letter with cipher_func,  repeating this function until the last letter
    print (cipher_func(c), end='') # parse the replaced letters into a sentence format
