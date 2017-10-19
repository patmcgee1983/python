# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:30:33 2017

@author: Reese / Pat
"""

import matplotlib.pyplot as plt
import queue
import numpy 
import random

# Define Constants & Variables
numberOfServers = 5
Servers = []

# Server object
class Server:
    def __init__(self, id):
        self.id = id
        self.list = []
    
    def getVms(self):
        return self.list
    
    def addVm(self, vmId):
        self.list.append(vmId)

# Load servers into server array
for i in range(0,numberOfServers):
    Servers.append(Server(i))


# Load servers with test data 
def testServers():
    for i in range(0,numberOfServers):
        for j in range(0,5):
            x = random.randint(0,44)
            Servers[i].addVm(x)

# Print the contents of all servers
def printServers():
    for i in range(0, numberOfServers):
        print(str(Servers[i].getVms()))

testServers()
printServers()
