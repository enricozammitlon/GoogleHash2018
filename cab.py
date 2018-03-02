"""
Created on Thu Mar  1 18:58:41 2018

@authors: enrico (@rustychickenleg),toby (@tobyjamez)
"""
class cab:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.available = True
        self.stepsTaken=0
"""
    def moveUp(self):
        self.y +=1
        self.stepsTaken+=1

    def moveDown(self):
        self.y -=1
        self.stepsTaken+=1

    def moveRight(self):
        self.x +=1
        self.stepsTaken+=1

    def moveLeft(self):
        self.x -=1
        self.stepsTaken+=1
"""
    def getCurrentLoc(self):
        return [self.x,self.y]

    def assign(self,jobDetails):
        self.available=False
        

    def isAvailable(self):
        return self.available
