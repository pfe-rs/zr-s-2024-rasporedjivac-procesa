import time
import algorithmPlanner

class Process:
    _idCounter = 0
    def __init__(self, remainingIterations, size, sleepInterval):
        self.remainingIterations = remainingIterations
        self.sleepInterval = sleepInterval
        self.size = size
        self.id = _idCounter
        _idCounter += 1

class CPU:
    _instance = None

    def __new__(cnt):
        if not cnt._instance:
            cnt._instance = super().__new__(cnt)
            cnt._instance.os = OS()
        return cnt._instance

    def run(self):
        while self.os.hasProcesses():
            proc = self.os.getProcess()
            if not proc:
                time.sleep()
            else:
                if proc.remainingIterations > 0:
                    print("Process ", proc.id, " is running")

                    for i in range(proc.size):
                        continue
                
                    proc.remainingIterations -= 1
                    if proc.sleepInterval > 0: #ako je sleepInterval is 0, no need to sleep
                        self.os.sleep(proc.sleepTime, proc)
                else:
                    self.os.finishProcess(proc)

class CPUScheduler:
    def __init__(self):
        self.algorithmPlanner = algorithmPlanner.AlgorithmPlanner()
        self.prioritizedAlgorithm = None

    def setPrioritizedAlgorithm(self, algorithm):
        self.prioritizedAlgorithm = algorithm

    def getNumberOfProcesses(self):
        return self.algorithmPlanner.numberOfProcesses

    def getProcess(self):
        self.prioritizedAlgorithm.NumberOfProcesses -= 1 #ne radi

        return None

    def putProcess(self, proc):
        self.processes.append(proc)
        self.numberOfProcesses += 1

class OS:
    _instance = None

    def __new__(cnt):
        if not cnt._instance:
            cnt._instance = super().__new__(cnt)
            cnt._instance.cpu = CPU()
        return cnt._instance

    def __init__(self):
        self.blockedProcesses = []
        self.numberOfProcesses = 0
        self.cpuScheduler = CPUScheduler()

    def createProcess(self, proc):
        self.cpuScheduler.putProcess(proc)

    def hasProcesses(self):
        return self.numberOfProcesses + self.cpuScheduler.> 0
    
    def getProcess(self):
        for proceess in self.blockedProcesses:
            if proceess.wakeTime <= time.time():
                self.blockedProcesses.remove(proceess)
                self.numberOfProcesses -= 1
                self.cpuScheduler.putProcess(proceess)
        return self.cpuScheduler.getProcess()
    
    def sleep(self, proc):
        self.blockedProcesses.append(proc)
        self.numberOfProcesses += 1
        proc.wakeTime = time.time() + proc.sleepInterval

    def finishProcess(self, proc):
        pass
    


os = OS()

process1 = Process(5, 10, 1)
os.createProcess(process1)
process2 = Process(3, 20, 2)
os.createProcess(process2)
process3 = Process(2, 15, 3)
os.createProcess(process3)

cpu = os.cpu
cpu.run()

