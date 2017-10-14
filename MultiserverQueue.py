# Simulates multiserver queue and plots distribution of delay times on Histogram
# matplot works on Linux only

import matplotlib.pyplot as plt
import queue
import numpy

# Each job is an object that has properties
class Job:

    def __init__(self,k):
        self.arrivalTime = k

# Each server is an object
class Server:

    def __init__(self, id):
        self.id = id
        self.q = queue.Queue(100000)

    def getJobs(self):
        return self.q.qsize()

    def addJob(self, job):
        self.q.put(job)
        # print("Added a job to Server " + str(self.id))

    def completeJob(self):
        return self.q.get()


# Define variables
numberOfTests = 1000000

a = arrivalRate = 0.55
d = departureRate = 0.5
N = numberOfServers = 5

# Servers array contains server objects
Servers = [] * N

# Create N Servers and load them into the array Servers[]
for i in range(0,N):
    newServer = Server(i)
    Servers.append(newServer)

# Initializing Arrays, t=time, x & y coordinates
t = [] * numberOfTests
x = []
y = []

# Each counter[i] keeps track of number of servers that experience a delay of i
counter = [] * numberOfTests
for i in range(0,numberOfTests):
    counter.append(0)

# Set up pyplot
plt.ylabel("Fraction of Jobs thats Experience x delay");
plt.xlabel("Delay D");
plt.title("λ = " + str(arrivalRate) + " /  µ = " + str(departureRate) + " With " + str(numberOfTests) + " tests and " + str(N) + " Servers")

# Get the number of arrivals or departures based on number of servers n and probability p
def getBinomial(p, n):

    return numpy.random.binomial(n, p, size=None)

# Initializing time (k) and queue length (q)
k=0
q=0

while k < numberOfTests:

    # get number of arrivals & departures for timeslot k
    arrivals = getBinomial(arrivalRate, N)
    departures = getBinomial(departureRate, N)

    if (departures > (arrivals + q)):
        departures = arrivals + q

    q = q + (arrivals-departures)

    # For each arrival, add to server with shortest queue
    for i in range(0,arrivals):

        shortestQueue = 0

        # Get server with shortest queue
        for currentServer in range(1, N):

            if (Servers[currentServer].getJobs() < Servers[currentServer - 1].getJobs()):
                shortestQueue = currentServer

        # add the job to the shortest queue
        Servers[shortestQueue].addJob(k)

    # For each departure we will remove the next job from servers queue
    for i in range(0,departures):

        longestQueue = 0

        # Get server with longest queue
        for j in range(1, N):

            if (Servers[j].getJobs() > Servers[j - 1].getJobs()):
                longestQueue = j

        # We find out when the job was placed in q
        timeStarted = Servers[longestQueue].completeJob()

        # calculate how long that job has been in server for
        delay = k - timeStarted
        x.append(delay)

    k += 1


plt.hist(x, bins=max(x), range=None, facecolor='r')  # arguments are passed to np.histogram
plt.show()
