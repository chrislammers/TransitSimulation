# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:21:40 2024

@author: chris
"""


def isInLine(p1, p2):
    # Check if p1 is in line with p2.
    
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True
    
    return False

List_Of_Stations = []

class Station:
    def __init__(self, name="0", location=[0,0], connections=[]):
        # Name of the station: String
        self.name = name
        # Location of the station: List [x (Integer),y (Integer)]
        # if the array is not integers, will need to round.
        self.location = location
        # List of other Stations to possibly connect to: List []
        # ONLY use connections in the constructor for custom, non 45 degree angle connections.
        self.connections = connections.copy()
            
        self.createConnections(List_Of_Stations)
        # This will need some sort of check to see if the
        
        List_Of_Stations.append(self)
    
    def getConnections(self):
        print("List of connections from " + self.name + ":")
        for conn in self.connections:
            print(conn.name)
            
    def connect(self, station):
        # Simply connect two stations together
        self.connections.append(station)
        
        # station.connections.append(self)
        
        
    
    def createConnections(self, stationList):
        # stationList is a list of existing stations.
        # for each station, add it to connections if the connection is on the 8 ordinal and cardinal directions
        # For now, Just N, E, S, W
        for station in stationList:
            # probably should have type safety
            print("Testing "+self.name+" and "+station.name)
            if isInLine(self.location, station.location):
                print("Connecting "+self.name+" at " +str(self.location)+" to "+station.name+" at "+str(station.location))
                self.connect(station)
                station.connect(self)
    
            
            
s1 = Station("station1", [1,1])
print(List_Of_Stations)
print("")
s2 = Station("station2", [1,3])
print(List_Of_Stations)
print("")
s3 = Station("station3", [2,2])
print(List_Of_Stations)
print("")
s4 = Station("station4", [4,10])
print(List_Of_Stations)
print("")
s5 = Station("station5", [2,1])
print(List_Of_Stations)
print("")
s6 = Station("station6", [8,8])
print(List_Of_Stations)
print("")

s1.getConnections()
s2.getConnections()
s3.getConnections()
s4.getConnections()
s5.getConnections()
s6.getConnections()

