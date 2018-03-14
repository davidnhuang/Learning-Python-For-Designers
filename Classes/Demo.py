# March 8th, 2018
# Learning Python: Class and Object Oriented Programs
# Tutorial URL:https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

# FUNCTIONS AND CLASSES
class Customer(object): # class that defines a customer
    # a customer of ABC Bank with a checking account. Customers have the following attributes:
    # 1. Customers have a name: a string representing the customer's name
    # 2. Customers have a balance: a float tracking the current balance of the customer's account

    def __init__(self, name, balance=0.0): # initializing the Customer class
        # describing the customer
        # for self, it's like saying "here's how you withdraw money from a Customer object, which is the name of the
        # object itself."
        self.name = name # creates the name for the customer
        self.balance = balance # creates the `balance` for the customer

    def withdraw(self, amount):
        # returning a balance remaining after withdrawing `amount` dollars.
        if amount > self.balance: # if the parameter `amount` is greater than balance from init
            raise RuntimeError ("Amount greater than available balance.") # print insufficient balance message
        self.balance -= amount # else remove `amount` from balance
        return self.balance # return the value

    def deposit(self, amount):
        # returning a balance after `amount` is added
        self.balance += amount
        return self.balance

class Car(object): # here we've created the class Cars
    wheels = 4 # cars have 4 wheels
    def __init__(self, make, model): # here we are describing the car
        self.make = make # here we are describing the make
        self.model = model # here we are describing the model of the car

    @staticmethod # a static method removes methods need to have the self declaration
    def car_gas_sound():
        print ('Vroom!')

    @classmethod
    def motorcycle_wheel(cls):
        return cls.wheels == 2

mustang = Car('Ford', 'Mustang') # a Mustant is a Ford vehicle under the Mustang model

#INHERITANCE
#MAIN
print (mustang.wheels)
print (Car.wheels)
print (mustang.car_gas_sound())
