# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:23:38 2024

@author: chris
"""

import Objects.vehicle as vh
# from station import Station


# At a basic level, this is linear, no branches
class Route:
    def __init__(self, stops, vehicle):
        # list of stops the route takes in order: List<Station>
        self.stops = stops.copy()
        self.vehicle = vh.Bus(1, 1)
    
    def addStation(self, station, atStart=False):
        if not atStart:
            # last station in self.stops must have the new station as a connection
            self.stops.append(station)
        else:
            # first station in self.stops must have the new station as a connection
            self.stops.insert(0, station)
            
    
        
        
        
