# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 12 2017
# ID 0239637

#FUNCTION
def reverse_order(num):
    if len(num) <= 1: # tests if the length of the string has more than 1 number
        return num # if it only has one number, skip and reprint

    # Below is a recursion return, in that the string will be sliced after the first digit, and then add on the first of
    # the resulted string. Once when the function reaches a point when the length is = 1, it would simply return the value
    # as shown above
    return reverse_order(num[1:]) + num[0]

#MAIN
print (reverse_order("123"))
