class CPUScheduler:
    def __init__(self, prioritizedAlgorithm):
        self.prioritizedAlgorithm = prioritizedAlgorithm

    def setPrioritizedAlgorithm(self, algorithm):
        self.prioritizedAlgorithm = algorithm

    def getNumberOfProcesses(self):
        return self.prioritizedAlgorithm.getNumberOfProcesses()

    def getProcess(self):
        return self.prioritizedAlgorithm.getProcess()

    def putProcess(self, proc):
        self.prioritizedAlgorithm.putProcess(proc)
    
