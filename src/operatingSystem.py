from cpuScheduler import CPUScheduler
import time

class OS:
    _instance = None

    def __new__(cls, cpu, pAlgorithm):
        if not cls._instance:
            cls._instance = super().__new__(cls)
    
        cls.blockedProcesses = []
        cls.numberOfProcesses = 0
        cls.cpu = cpu
        cls.cpuScheduler = CPUScheduler(pAlgorithm)
        
        return cls._instance

    def createProcess(self, proc):
        print("Process [", proc.id, "] is created.", sep='')
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
        print("Process [", proc.id, "] is finished.", sep='')
        pass
    