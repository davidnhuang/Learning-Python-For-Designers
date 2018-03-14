# David Huang
# Computer Programming for Designers and Artists
# Week 5 - Oct 11 2017
# ID 0239637

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print (rainbow[2:5]) # This prints yellow (index 2) to blue (index 5)

numbers = [i*10 for i in range(10)]
print (numbers[3]) # returns 30, as 3 in the range of 10 is called and multiplied with 10

jumble = rainbow
jumble.extend(numbers) # number is added to jumble as a list, along with rainbow as a list
jumble.remove("indigo") # indigo is removed from the list
print (jumble[10]) # returns 40, as 40 is the 10th value in the jumble list

planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
sad_planet = planets.pop()
print (planets[-6], sad_planet) # returns earth, since earth is the 6th string from the last string after pluto has been
                                # removed, pluto is returned as sad_planet
