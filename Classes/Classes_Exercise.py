# Author: David Huang
# Learning Python for Designers
# Reverse String with Classes
# 3 - 16 - 2018

# Create a class that describes a dog

class dog(): # creates the class dog, which produces a dog with the attribute color and name
    def __init__(self, color, name): # initializing
        self.color = color # describes that a dog has a distinct color
        self.name = name # describes that a dog has a distinct name

    def dog_attribute(self): # method that prints the attributes assigned to the dog
        print (self.color) # prints the color
        print (self.name) # prints the name

    def bark(self): # method that gets the dog to bark
        print ('Woof!') # Woof!

    def howl(self): # method that gets the dog to howl
        print ('Aoooo!') # Howling

tony_the_bulldog = dog('black', 'Tony') # here, we are declaring Tony the Bulldog as a dog with the name Tony and is Black

tony_the_bulldog.dog_attribute() # since before, we assigned tony_the_bulldog to dog class, here, we see tony_the_bulldog
                                 # being passed into the self position. Therefore, the attribute black and Tony are also
                                 # being passed and called as well
tony_the_bulldog.bark() # barks
tony_the_bulldog.howl() # howls

# A clear distinction is that a class is NOT a function; it is a series of methods that help define an object.
# A dog has four legs, a color, and can bark and howl. This means that the methods within the class would define those.
# Think of class as the object or thing, and the method as parts of the thing or characteristics of that thing

# Create a class that describes a mammal - define a cow, a dog, and a lion
class mammal():

    def __init__(self, animal_name, food, wild, animal_type):
        self.animal_name = animal_name
        self.food = food
        self.wild = wild
        self.animal_type = animal_type

    def description(self):
        print(self.animal_name, 'eats', self.food, 'and is', self.wild, 'and', self.animal_type, 'a hunter')

    def cow_noise(self):
        if self.animal_name == 'cow':
            print ('mooo')
        else:
            print ('dunno')

cow = mammal('cow','grass', 'domestic', 'is not')

cow.description()
cow.cow_noise()

class life():

    def __init__(self, name, photosynthetic, predatory, sexual_reproduction):
        self.name = name
        self.photosynthetic = photosynthetic