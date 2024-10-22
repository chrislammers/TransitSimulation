# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:41:59 2024

@author: chris
"""

# this will be used later when I add people movement.
import time

class Vehicle:
    def __init__(self, capacity, riders=1, stopTime=0):
        self.capacity = capacity
        self.riders = riders
        self.stopTime = stopTime
        
    # this can be used to add AND subtract, using negatives
    def add_rider(self, num_riders):
        self.riders += num_riders
        if self.riders > self.capacity:
            overflow = self.capacity - self.riders
            print("The bus is full! " + str(overflow) + " people left behind")
            self.riders = self.capacity
        
        
        
    def __str__(self):
        return "Vehicle with " + str(self.riders) + "/" + str(self.capacity) + " riders."
        
class Bus(Vehicle):
    def __init__(self, capacity, riders, two_floor=False):
        super().__init__(capacity, riders)
        # print(type(two_floor)) 
        if type(two_floor) is not type(False):
            two_floor = False
            print("two_floor needs to be a boolean. Defaulting to single floor")
        self.two_floor = two_floor
    
    def __str__(self):
        if self.two_floor:
            floors = "Double-Decker Bus"
        else:
            floors = "Bus"
        
        return floors + " with " + str(self.riders) + "/" + str(self.capacity) + " riders." 
    
class Rail(Vehicle):
    def __init__(self, capacity, riders, length=1):
        super().__init__(capacity, riders)
        # length of vehicle (number of carriages)
        self.length = length

# bus = Bus(10, 5)
# print(bus)
# v1 = Vehicle(5, 1)
# print(v1)