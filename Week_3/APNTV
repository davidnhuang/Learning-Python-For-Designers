#----------------------------------------------------------------------------
# APNTV System
# Alien Prime Number Test Verification
# Sep 13, 2017
#
# To keep humanity safe, this program is designed to confirm the presence of
# PRIME numbers in our dealing with extraterrestrials!
# Authorized use only.
#
# CONFIDENTIAL - This document requires prior authorization for use
# All authors & contributors must add credentials below:
#
# NAME: David Huang
# DATE: 10 / 4 / 2017
# ID Number: 0239637
# Change log: 1.20
#
#
##
###
#####
#######
###########



#-- is_prime function
# Hey you! HSCI-234 Student! Here is where you have a job to do. Remember this is for humanity so make sure it works right!
# This is a function definition. We'll learn all about functions next week. For now, scroll down a few lines to where the comments tell you to work
# You are going to add code to test if a given number is PRIME and return the value True if so and False if not.

def is_prime(num):

        # OKAY! remember our definition of a prime number!
        #  a) it is greater than 1
        #  b) it is a whole number
        #  c) it is only divisible by 1 and itself

		# use your new found knowledge of if statements, looping and operators to get a True or False answer
		# put that answer in the variable test_result - it will get returned at the end of the function

        # -------------------- start code here
        division_count = 0 # counts how many times the number can be divided as a whole

        # determines if whether the number can be divided by anything other than 1 and itself
        for i in range (1, int(num) + 1, 1): # dividing it by the range of 1 and itself
            if (int(num)/i) % 1 == 0:
                division_count += 1 # this counts how many times the input can be fully divisible; prime can ONLY be divisible by 2 numbers
        # tests whether the number is 1) greater than 1, 2) whole, 3) divisible only by 1 and itself
        if int(num) > 1 and int(num) % 1 == 0 and division_count == 2:
            test_result = True
        else:
            test_result = False
        # -------------------- end code here (you can add as many lines above as you need)
        return test_result

#-- code body
# requests candidate number from user and prints the result of the verification test
print ('=' * 23 + '-[APNTV]-' + '=' * 23)
print ("Welcome to APNTV\nRestricted access...\n")
number_to_test = input("Enter candidate number: ")

# text parsed together with values returned from code
text_result = "IS" if is_prime(number_to_test) == True else "IS NOT"
print ("\nThe number you entered was " + str(number_to_test) + "\nIt " + text_result + " prime.")
