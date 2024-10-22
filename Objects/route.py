# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:23:38 2024

@author: chris
"""

import Objects.vehicle as vh
# from station import Station


# At a basic level, this is linear, no branches
class Route:
    def __init__(self, name, stops, vehicle):
        # list of stops the route takes in order: List<Station>
        self.name = name
        self.stops = stops.copy()
        self.vehicle = vh.Bus(1, 1)
        # this info is here for now, though move() and this could be moved elsewhere in the future
        self.direction = 1
        self.current_location = 0
        
        
    
    def addStation(self, station, atStart=False):
        if not atStart:
            # last station in self.stops must have the new station as a connection
            self.stops.append(station)
        else:
            # first station in self.stops must have the new station as a connection
            self.stops.insert(0, station)
            
    def move(self):
        if len(self.stops) < 2:
            print("Add more stations before you move. (minimum 2)")
            return
        
        print("Moving from "+self.stops[self.current_location].name+" to "+self.stops[self.current_location+self.direction].name)
        self.current_location+=self.direction
        # print(str(self.current_location+1)+">="+str(len(self.stops)))
        # print("")
        
        if self.current_location+1>=len(self.stops):
            self.direction = -1
            print("You've reached the end of the line")
            return
        if self.current_location-1 <= -1:
            self.direction = +1
            print("You've reached the start of the line")
            return
        
        