from Read import *
from metric import *
from cab import cab

taxis = [cab() for i in range(firstline([2]))]

jobs = rest()

jobs = sorted(jobs, key = lambda x : distance([x[0], x[1]], [x[2], x[3]]))


