# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 11 2017
# ID 0239637

#todo - takes the list of every US president’s age (in years only) when elected and computes the average


# Global Variables
pres_age = [42, 43, 46, 46, 47, 47, 48, 49, 49, 50, 51, 51, 51, 51, 51, 52, 52, 54, 54, 54, 54, 54, 55, 55, 55, 55, 56,
            56, 56, 57, 57, 57, 57, 58, 60, 61, 61, 61, 62, 64, 64, 65, 68, 69, 70]

def age_average(age_list):
    age_sum = 0 # Empty variable; used to store all the age values summed together
    for age in range(0, len(age_list)-1): # take index from first age at 0 to last
        age_sum += age_list[age] # add the age value to the age sum variable
    return age_sum / len(age_list) # take the sum and divide it by the length of the list to get the average

# Output
print (age_average(pres_age))
