# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 11 2017
# ID 0239637

import random

#Variables
brady_bunch = ["Mike", "Carol", "Greg", "Jan", "Marsha", "Bobby", "Peter", "Cindy"]
plots = ["was late", "was sick", "got in trouble", "won a contest", "sang a song", "had a date"]

# generate plot lines

# In order for code to work, the range must be the len(list)-1 since we are taking the indices.
character = random.randint(0,len(brady_bunch)-1)
# Same goes for this line, in which the range must be len(list)-1
plot = random.randint(0,len(plots)-1)
print (brady_bunch[character],plots[plot])
