class Read:
    def __init__(self,filename):
        readFile = open(filename,'r');
        processTheLine= 0
        self.firstline=""
        self.jobs=[[]]

        for line in readFile:
            splitUp = line.split();
            if processTheLine:
                self.jobs.append([int(splitUp[0]),int(splitUp[1]),int(splitUp[2]),int(splitUp[3]),int(splitUp[4]),int(splitUp[5])])
            else:
                firstline=line
                processTheLine = 1;
        readFile.close();


    def getFirstLine(self):
        return self.firstline

    def getJobs(self):
        return self.jobs
