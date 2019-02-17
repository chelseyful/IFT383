#!/usr/bin/python
class Cake(object):
    _calories = 0
    def __init__(self, calories=5000):
        self._calories = calories

    def getCalories(self):
        return self._calories

    def __str__(self):
        return "I am a delicous cake consisting of %d calories!" % (self._calories)

    def __eq__(self, other):
        return self._calories == other._calories

    def __add__(self, other):
        return Cake(self._calories + other._calories)

class SheetCake(Cake):
    length=0
    width=0
    def __init__(self, calories=5000, length=24, width=12):
        self._calories = calories
        self.length = length
        self.width = width

class CheeseCake(Cake):
    radius=0