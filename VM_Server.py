# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:30:33 2017

@author: Reese / Pat
"""

import matplotlib.pyplot as plt
import numpy 
import random

# Define Constants & Variables
servers = []
enableDebugTests = True
timeSlots = 1000000
arrivalRate = 0.9
x = []
yBest = []
yFirst = []
# N = max number of servers that will arrive at each timeslot, will iterate each N
N = [2, 4, 8, 16, 32]


# resources consumed correspod to VM #
# ie = vm[0] = 0.5, etc
vm = [0.5, 0.25, 0.125]
geometricMean = [10, 8, 30]
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
        i=0
        while i < len(self.list):
            # The probability of a vm vacating a server in any timeslot is 1 /  its geometric mean
            if (random.random() <= (1 / geometricMean[self.list[i]])):
                self.depart(self.list[i])
                i-=1

            i += 1
                
    def depart(self,i):
        self.list.remove(i)
        self.cpu = self.cpu + vm[i]
            
                
    
    def toString(self):
        return "Server " + str(self.id) + ": " + str(self.getVms()) + " : " + str(self.getRemainingCPU()) +" CPU remaining"

def createNewServer(id):
    #print("created server " + str(id))
    servers.append(Server(id))


def firstFit(numberOfVmsCreated):
    
    # Checking the servers
    for numberOfVms in range(0,numberOfVmsCreated):
        
        # Generate a new VM id
        vmId = numpy.random.randint(0,len(vm))
         
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

def bestFit(numberOfVmsCreated):
    
    for numberOfVms in range(0,numberOfVmsCreated):
        vmId = numpy.random.randint(0,len(vm))
        bestFitPlace(vmId)
        

def bestFitPlace(vmId): #vmID is a single value between 0 and 2 (inclusive) representing a VM type
    bestVal = 10
    bestServer = -1
    i = 0
    while(i < len(servers)+1):
        # If we checked all servers and no room, make new server
        if ((i == len(servers)) and (bestServer == -1)):
            createNewServer(i)
            servers[i].addVm(vmId)
            return True
        # If space found on a server, check for exact match, add
        if (i < len(servers)):
            if (servers[i].getRemainingCPU() == vm[vmId]):
                servers[i].addVm(vmId)
                return True

            if((servers[i].getRemainingCPU() - vm[vmId] > 0) and (servers[i].getRemainingCPU() - vm[vmId] < bestVal)):
                bestVal = servers[i].getRemainingCPU() - vm[vmId]
                bestServer = i
        i += 1
    if(bestServer != -1):
        servers[bestServer].addVm(vmId)


# Print the contents of all servers
def printServers():
    for i in range(0, len(servers)):
        print(servers[i].toString())


for iterations in range(0,len(N)):
    serverSum = 0
    #  
    for k in range(0,timeSlots):
        
        # The number of vms arriving is a binomial with parameters N,lambda
        vmsArrived = numpy.random.binomial(N[iterations],arrivalRate)
        
        #firstFit with the number of arrivals
        firstFit(vmsArrived)
        
        # BestFit(numberOfArrivals)
        # Best fit method call will go here
        
        i=0
        
        while i < len(servers):
            servers[i].tick()
            if (servers[i].getRemainingCPU() == 1):
                servers.pop(i)
                i -= 1
            
            i += 1
                
        serverSum = serverSum + len(servers)
    
    avgServers = serverSum / k
    yFirst.append(avgServers)
    #yBest.append(avgServers)
    print("----------" + str(N[iterations]) + " : " + str(yFirst[iterations]) + "-----------")


servers.clear()



for iterations in range(0,len(N)):
    serverSum = 0
    #  
    for k in range(0,timeSlots):
        
        # The number of vms arriving is a binomial with parameters N,lambda
        vmsArrived = numpy.random.binomial(N[iterations],arrivalRate)
        
        #firstFit with the number of arrivals
        bestFit(vmsArrived)
        
        # BestFit(numberOfArrivals)
        # Best fit method call will go here
        
        i=0
        
        while i < len(servers):
            servers[i].tick()
            if (servers[i].getRemainingCPU() == 1):
                servers.pop(i)
                i -= 1
            
            i += 1
                
        serverSum = serverSum + len(servers)
    
    avgServers = serverSum / k
    yBest.append(avgServers)
    print("----------" + str(N[iterations]) + " : " + str(yBest[iterations]) + "-----------")


plt.plot(N,yFirst,'b-', label='First Fit')
plt.plot(N,yBest,'r-', label='Best Fit')
plt.ylabel('Avg Number of Servers')
plt.xlabel('N')
plt.title('Best fit vs First Fit Avg Number of Servers for N jobs')
plt.show()
#printServers()
