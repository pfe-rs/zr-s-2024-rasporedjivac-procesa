from abc import ABC, abstractmethod
import queue
from queue import PriorityQueue
from dataclasses import dataclass, field

class AlgorithmPlanner(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def getProcess(self):
        pass
    @abstractmethod
    def putProcess(self, proc):
        pass
    def getNumberOfProcesses(self):
        pass
    
class FirstComeFirstServe(AlgorithmPlanner):
    def __init__(self):
        self.procesess = queue.Queue()
    def getProcess(self):
        if not self.procesess.empty():
            return self.procesess.get()
        else:
            return None
    def putProcess(self, proc):
        self.procesess.put(proc)
    def getNumberOfProcesses(self):
        return self.procesess.qsize()


@dataclass(order=True)
class ShortestProcessFirst(AlgorithmPlanner):
    def __init__(self):
        self.priorityQueue = PriorityQueue()
    
    def getProcess(self):
        if not self.priorityQueue.empty():
            return self.priorityQueue.get()[1]
        else:
            return None

    def putProcess(self, proc):
        self.priorityQueue.put((proc.size, proc))
    
    def getNumberOfProcesses(self):
        return self.priorityQueue.qsize()