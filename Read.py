import numpy as np

readFile = open('Test.txt','r');
startx = []
endx = []
starty = []
endy = []
rides = None
vehicles = None
bonus = None
steps = []
rows = None
columns = None
estart = []
efinish = []
steps = None
processTheLine = 0;

for line in readFile:
   splitUp = line.split();
   if processTheLine:
   
        
    startx.append(int(splitUp[0]))
    starty.append(int(splitUp[1]))
    endx.append(int(splitUp[2]))
    endy.append(int(splitUp[3]))
    estart.append(int(splitUp[4]))
    efinish.append(int(splitUp[5]))
    
    
   else:
    rows = int(splitUp[0])
    columns = int(splitUp[1])
    vehicles = int(splitUp[2])
    rides = int(splitUp[3])
    bonus = int(splitUp[4])
    steps = int(splitUp[5])
  
   processTheLine = 1;



readFile.close();
start = np.column_stack((startx, starty))
end = np.column_stack((endx, endy))
print(steps)