class Process:
    def __init__(self, remainingIterations, sleepInterval, size):
        self.remainingIterations = remainingIterations
        self.sleepInterval = sleepInterval
        self.size = size

class CPU:
    def __init__(self):
        self.os = OS(self)

    def run(self):
        while os.hasProcesses(): #postoje procesi koji se izvrsavaju (ready ili blocked) total processes > 0
        proc = os.getProcess() # scheduler.getProcess()
        if not proc:
            time.sleep()
        else:
            if proc.remainingIterations > 0:
                dowork(proc.workAmout) #for i in range(proc.workAmount) dummy work

                proc.remainingIterations -= 1
                os.sleep(proc.sleepTime, proc)
            else:
                os.exit(proc) #totall processes--


class OS:
    def __init__(self, cpu):
        self.processes = []
        self.totalProcesses = 0
        self.cpu = CPU(cpu)

    def createProcess(self, proc):
        self.processes.append(proc)
        self.totalProcesses += 1

    def hasProcesses(self):
        return self.totalProcesses > 0
    
    def getProcess(self):
        if self.totalProcesses > 0:
            return self.processes.pop(0)
        return None
    