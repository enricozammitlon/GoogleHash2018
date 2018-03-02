from Read import *
from metric import *
from cab import cab

taxis = [cab() for i in range(firstline([2]))]
availableTaxis=[i for i in taxis]
nfl = Read('a_example.in')
jobs = nfl.getJobs()

jobs_by_length = sorted(jobs, key = lambda x : distance([x[0], x[1]], [x[2], x[3]]))


jobs_by_start = sorted(jobs, key = lambda x : x[4])

counter=0
while(i<=10):
    for (job in jobs_by_start):
        if(len(availableTaxis)!=0):
            availableTaxis[0].assign(job)
        updateAvailableCabs(availableTaxis)
    counter+=1

def updateAvailableCabs(availableTaxis):
    availableTaxis=[if(i.isAvailable()) i for i in taxis]
