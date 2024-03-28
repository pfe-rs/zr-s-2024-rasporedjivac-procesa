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
        return self.procesess.get()
    def put_process(self, proc):
        pass