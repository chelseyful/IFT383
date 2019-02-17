#!/usr/bin/python
class Computer(object):

    # Data fields
    memory=2048
    cores=4
    wireless=False
    power=False

    # methods
    def powerOn(self):
        self.power=True

    def __init__(self, newMemory=None, newCores=None):
        if type(newMemory) is int:
            self.memory = newMemory
        if type(newCores) is int:
            self.cores = newCores
        self.power=False

    def powerOn(self):
        self.power=True