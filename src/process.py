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





os = OS()

process1 = Process(5, 10, 1)
os.createProcess(process1)
process2 = Process(3, 20, 2)
os.createProcess(process2)
process3 = Process(2, 15, 3)
os.createProcess(process3)

cpu = os.cpu
cpu.run()

