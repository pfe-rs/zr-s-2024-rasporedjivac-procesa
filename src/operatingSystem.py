from cpuScheduler import CPUScheduler
import time

class OS:
    _instance = None

    def __new__(cls, pAlgorithm):
        if not cls._instance:
            cls._instance = super().__new__(cls)
    
        cls.blockedProcesses = []
        cls.numberOfProcesses = 0
        cls.cpuScheduler = CPUScheduler(pAlgorithm)
        
        return cls._instance

    def createProcess(self, proc):
        self.getSys().mutex.acquire()
        print("Process [", proc.id, "] is created.", sep='')
        self.cpuScheduler.putProcess(proc)
        self.getSys().mutex.release()

    def hasProcesses(self):
        return self.numberOfProcesses + self.cpuScheduler.getNumberOfProcesses() > 0
    
    def updateProcesses(self):
        self.getSystem().mutex.acquire()
        for process in self.blockedProcesses:
            if process.wakeTime <= time.time():
                self.blockedProcesses.remove(process)
                self.numberOfProcesses -= 1
                self.cpuScheduler.putProcess(process)
        self.getSystem().mutex.release()
    
    def getProcess(self):
        self.updateProcesses()
        
        self.getSystem().mutex.acquire()
        proc = self.cpuScheduler.getProcess()
        self.getSystem().mutex.release()
        return proc
    
    def sleep(self, proc):
        self.getSystem().mutex.acquire()
        self.blockedProcesses.append(proc)
        self.numberOfProcesses += 1
        proc.wakeTime = time.time() + proc.sleepInterval
        self.getSystem().mutex.release()

    def finishProcess(self, proc):
        print("Process [", proc.id, "] is finished.", sep='')

    def getSystem(sys):
        return sys
    