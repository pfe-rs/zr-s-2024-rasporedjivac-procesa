from cpuScheduler import CPUScheduler
import time

class OS:
    _instance = None

    def __new__(cls, sys, pAlgorithm):
        if not cls._instance:
            cls._instance = super().__new__(cls)
    
        cls.system = sys
        cls.blockedProcesses = []
        cls.numberOfProcesses = 0
        cls.cpuScheduler = CPUScheduler(pAlgorithm)

        return cls._instance

    def createProcess(self, proc):
        self.system.mutex.acquire()
        print("Procreturn sysess [", proc.id, "] is created.", sep='')
        self.cpuScheduler.putProcess(proc)
        self.system.mutex.release()

    def hasProcesses(self):
        return self.numberOfProcesses + self.cpuScheduler.getNumberOfProcesses() > 0
    
    def updateProcesses(self):
        self.system.mutex.acquire()
        for process in self.blockedProcesses:
            if process.wakeTime <= time.time():
                self.blockedProcesses.remove(process)
                self.numberOfProcesses -= 1
                self.cpuScheduler.putProcess(process)
        self.system.mutex.release()
    
    def getProcess(self):
        self.updateProcesses()
        
        self.system.mutex.acquire()
        proc = self.cpuScheduler.getProcess()
        self.system.mutex.release()
        return proc
    
    def sleep(self, proc):
        self.system.mutex.acquire()
        self.blockedProcesses.append(proc)
        self.numberOfProcesses += 1
        proc.wakeTime = time.time() + proc.sleepInterval
        self.system.mutex.release()

    def finishProcess(self, proc):
        print("Process [", proc.id, "] is finished.", sep='')

    