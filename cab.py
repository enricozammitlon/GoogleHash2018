"""
Created on Thu Mar  1 18:58:41 2018

@authors: enrico (@rustychickenleg),toby (@tobyjamez)
"""
class cab:
    def __init__(self, start_loc, end_loc, steps_left):
        self.x = start_loc[0]
        self.y = start_loc[1]
        self.available = True
        self.end_loc = end_loc
        self.steps_left = steps_left

    def moveTo(self, end_loc):
        self.x = end_loc[0]
        self.y = end_loc[1]:

    def getCurrentLoc(self):
        return [self.x,self.y]

    def assign(self,jobDetails)
