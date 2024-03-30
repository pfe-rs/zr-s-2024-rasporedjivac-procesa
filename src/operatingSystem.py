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
    
    def getProcess(self):
        self.sys.mutex.aquire()
        for proceess in self.blockedProcesses:
            if proceess.wakeTime <= time.time():
                self.blockedProcesses.remove(proceess)
                self.numberOfProcesses -= 1
                self.cpuScheduler.putProcess(proceess)
        
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
    