# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:41:59 2024

@author: chris
"""

# this will be used later when I add people movement.

class Vehicle:
    def __init__(self, capacity, riders=1):
        self.capacity = capacity
        self.riders = riders
    def __str__(self):
        return "Vehicle with " + str(self.riders) + " riders."
        
class Bus(Vehicle):
    def __init__(self, capacity, riders, route):
        super().__init__(capacity, riders)
        self.route = route
    def __str__(self):
        return "Bus " + str(self.route) + " with " + str(self.riders) + " riders."

bus = Bus(10, 5, 901)
print(bus)
v1 = Vehicle(5, 1)
print(v1)