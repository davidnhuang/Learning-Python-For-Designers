# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 12 2017
# ID 0239637

#todo - function should take two arguments, roots and n
#todo - function must loop recursively
#constraints - do not use ** operator

#GLOBAL VARIABLES
user_root = input ("Enter number: ")
user_power = input ("To what power: ")

#FUNCTIONS
def exponent(root, power):
    if int(power) == 1:
        return root
    if int(power) == 0:
        return 1
    else:
        return int(root) * int(exponent(root, int(power)-1))

#MAIN
print ('='*50)
print (user_root, "to the power of", user_power, "equals", exponent(user_root, user_power))
