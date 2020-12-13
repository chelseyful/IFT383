#!/usr/bin/python3

# The Cake class defines the properties and behaviors shared by all types of
# cakes. or example; all implimentations of Cake will have calories
class Cake(object):
    _calories = 0
    def __init__(self, calories=5000):
        self._calories = calories

    def getCalories(self):
        return self._calories

    def __str__(self):
        return f"I am a delicous cake consisting of {self._calories} calories!"

    def __eq__(self, other):
        return self._calories == other._calories

    def __add__(self, other):
        return Cake(self._calories + other._calories)


# SheetCake is a type of Cake, and inherits the properties and behaviors
# from its parent class Cake. Additionally, SheetCake also has a length and
# width property that defines the dimensions of the SheetCake.
class SheetCake(Cake):
    length=0
    width=0
    def __init__(self, calories=5000, length=24, width=12):
        self._calories = calories
        self.length = length
        self.width = width


# CheeseCake also inherits all properties and behaviors from Cake.
# In addition, it has a property for radius. This implimentation
# differs from SheetCake, as CheeseCake is round, If this was a
class CheeseCake(Cake):
    radius=0
