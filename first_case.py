# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:05:18 2024

@author: chris
"""

from Objects.station import Station
from Objects.route import Route

print("Creating Stations:")         
s1 = Station("station1", [1,1])
print("")
s2 = Station("station2", [1,3])
print("")

print("Listing Connections:")
s1.getConnections()
s2.getConnections()

print("")
print("Creating and travelling route:")
route = Route("Test Route", [s1, s2], 0)

route.move()
route.move()
route.move()


