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
servers = []
enableDebugTests = True
timeSlots = 10

# resources consumed correspod to VM #
# ie = vm[0] = 0.5, etc
vm = [0.5, 0.25, 0.125]

# Server object
class Server:
    def __init__(self, id):
        self.id = id
        self.list = []
        self.cpu = 1;
    
    def getVms(self):
        return self.list
    
    def addVm(self, vmId):
        self.list.append(vmId)
        self.cpu = self.cpu - vm[vmId]
        
    def getRemainingCPU(self):
        return self.cpu
        
    def tick(self):
        departures()
        
    def departures(self):
        return false
        
    def depart(self):
        return false
    
    def toString(self):
        return "Server " + str(self.id) + ": " + str(self.getVms()) + " : " + str(self.getRemainingCPU()) +" CPU remaining"

def createNewServer(id):
    #print("created server " + str(id))
    servers.append(Server(id))


def firstFit(vmId):
    # Checking the servers        
    for i in range(0,len(servers)+1):
        
        # If we checked all servers and no room, make new server
        if (i == len(servers)):
            createNewServer(i)
            servers[i].addVm(vmId)
            break
        
        # If space found on a server, put vm in
        if servers[i].getRemainingCPU() >= vm[vmId]:
            servers[i].addVm(vmId)
            #print("found space in server " + str(i))
            break
        
# Print the contents of all servers
def printServers():
    for i in range(0, len(servers)):
        print(servers[i].toString())

# Need one server to start
createNewServer(0);

#  
for i in range(0,timeSlots):
    #print("----- slot "+str(i) + " --------")
    firstFit(random.randint(0,len(vm)-1))
    
printServers()
