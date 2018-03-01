"""
Created on Thu Mar  1 18:58:41 2018

@authors: enrico (@rustychickenleg),toby (@tobyjamez)
"""
class cab:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.available = True

    def moveTo(self, end_loc):
        self.x = end_loc[0]
        self.y = end_loc[1]:

    def getCurrentLoc(self):
        return [self.x,self.y]

    def assign(self,jobDetails)
