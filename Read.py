class Read:


    def __init__(self,filename):
        readFile = open(filename,'r');
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
        self.firstline=""
        self.jobs=[[]]

        for line in readFile:
            splitUp = line.split();
            if processTheLine:
                self.jobs.append([int(splitUp[0]),int(splitUp[1]),int(splitUp[2]),int(splitUp[3]),int(splitUp[4]),int(splitUp[5])])
            else:
                firstline=line
                rows = int(splitUp[0])
                columns = int(splitUp[1])
                vehicles = int(splitUp[2])
                rides = int(splitUp[3])
                bonus = int(splitUp[4])
                steps = int(splitUp[5])
                processTheLine = 1;
        readFile.close();


    def getFirstLine(self):
        return self.firstline

    def getJobs(self):
        return self.jobs
