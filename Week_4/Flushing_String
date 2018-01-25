# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 12 2017
# ID 0239637

#todo - measure the string length
#todo - constain str.len to 50 characters
#todo - for string that exceed 50, return to next line

#GLOBAL VARIABLES
display_text = input("Enter text: ")
indent_length = input("How many characters per line: ")
text_length = len(display_text)

#FUNCTIONS
def right_justify(display_text):
    for i in range(0, text_length):
        if i % int(indent_length) == 0 and i != 0:
            print ("\n")
        print (display_text[i], end='')


#MAIN
print (" ")
print ("="*int(indent_length))
print (" ")
print (right_justify(display_text))

