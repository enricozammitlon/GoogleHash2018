from Read import *
from metric import *
from cab import cab

taxis = [cab() for i in range(firstline([2]))]

jobs = rest()

jobs_by_length = sorted(jobs, key = lambda x : distance([x[0], x[1]], [x[2], x[3]]))


jobs_by_start = sorted(jobs, key = lambda x : x[4])

