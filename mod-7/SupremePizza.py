#!/usr/bin/python
class SupremePizza(object):
    slices=16
    temperature=75.0

    def __init__(self, slices=16, temperature=75.0):
        self.slices = slices
        self.temperature = temperature

    def makeSupreme(self):
        self.meats = 'all'
        self.veggies = 'all'
        
    def hasSlices(self):
        if self.slices > 0:
            return True
        else:
            return False

    def eat(self, slices=1):
        if self.slices >= slices:
            self.slices -= slices
            return True
        else:
            return False

if __name__ == "__main__":
    myPizza = Pizza(8)
    while myPizza.hasSlices():
        print("Eating pizza...")
        myPizza.eat()