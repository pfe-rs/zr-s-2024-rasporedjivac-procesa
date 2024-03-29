from cpu import CPU
from cpuScheduler import CPUScheduler
import time

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
        return self.numberOfProcesses + self.cpuScheduler.getNumberOfProcesses() > 0
    
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
    