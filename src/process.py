class Process:
    _idCounter = 0
    def __init__(self, iterationNumber, size, sleepInterval):
        self.remainingIterations = iterationNumber
        self.sleepInterval = sleepInterval
        self.size = size
        self.id = Process._idCounter
        Process._idCounter += 1

