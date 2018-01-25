# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 11 2017
# ID 0239637

# Takes a list as argument and prints out any element that appears more than once in the list.

# CONSTANTS
num_list = [60, 83, 90, 60, 19, 20, 21, 21, 20, 84, 83, 90, 60, 21, 60]
duplicate_list = [] # This empty list is used to store index all the duplicate number
final_list = [] # This output is used to remove duplicates within the duplicate_list

# Variables

# Main
def print_duplicates(list):
    for num in range (len(list)): # Take index of all the characters in the range
        for next_num in range (num + 1, len(list)):# Take index of all the characters next to the index
            if list[num] == list[next_num]:# checks if the current index equates to the next index
                duplicate_list.append(list[next_num]) # add all the duplicates into duplicate_list

    # **below is another loop that organizes the duplicate_list - Purely for readability **
    for duplicate_num in duplicate_list: # Take index of all the characters in duplicate_list
        if duplicate_num not in final_list: # If the duplicate number is not in final list, meaning if it is unique
            final_list.append(duplicate_num) # Add unique value into new list final_list

    print ("From your number range, all duplicate values are as follow: ", end=' ')
    for i in range (len(final_list)): # Takes all the value from final_list and outputs them as individual values
        print (str(final_list[i]) + ', ', end=' ')

#Output
print(print_duplicates(num_list)) # Final Output
