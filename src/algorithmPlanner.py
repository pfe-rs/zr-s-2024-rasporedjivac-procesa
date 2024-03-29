from abc import ABC, abstractmethod
import queue
from queue import PriorityQueue
from dataclasses import dataclass, field

class AlgorithmPlanner(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def get_process(self):
        pass
    @abstractmethod
    def put_process(self, proc):
        pass
    
class FirstComeFirstServe(AlgorithmPlanner):
    def __init__(self):
        self.procesess = queue.Queue()
    def get_process(self):
        if not self.procesess.empty():
            return self.procesess.get()
        else:
            return None
    def put_process(self, proc):
        self.procesess.put(proc)


@dataclass(order=True)
class ShortestProcessFirst(AlgorithmPlanner):
    def __init__(self):
        self.process_queue = PriorityQueue()
    
    def get_process(self):
        if not self.process_queue.empty():
            return self.process_queue.get()
        else:
            return None

    def put_process(self, proc):
        proc.numOfIterations = field(compare=False)
        self.process_queue.put(proc)
