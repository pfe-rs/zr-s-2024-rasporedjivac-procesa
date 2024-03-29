class Process:
    _idCounter = 0
    def __init__(self, iterationNumber, size, sleepInterval, breakpoint):
        self.remainingIterations = iterationNumber
        self.sleepInterval = sleepInterval
        self.size = size
        self.runningTime = 0
        self.breakpoint = 0
        self.id = Process._idCounter
        Process._idCounter += 1

