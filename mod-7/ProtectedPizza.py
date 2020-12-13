#!/usr/bin/python3
class ProtectedPizza(object):
    __slices=16
    __temperature=75.0

    def __init__(self, slices=16, temperature=75.0):
        self._slices = slices
        self._temperature = temperature

    def hasSlices(self):
        if self._slices > 0:
            return True
        else:
            return False

    def getSlices(self):
        return self._slices

    def setSlices(self, newVal):
        if type(newVal) is int:
            self._slices = newVal
            return True
        else:
            return False
    def eat(self, slices=1):
        if self._slices >= slices:
            self._slices -= slices
            return True
        else:
            return False

if __name__ == "__main__":
    myPizza = ProtectedPizza(8)
    while myPizza.hasSlices():
        print("Eating pizza...")
        myPizza.eat()
