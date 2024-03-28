from abc import ABC, abstractmethod
import queue

class AlgorithmPlanner(ABC):
    def __init__(self):
        pass
    def get_process(self):
        pass
    def put_process(self, proc):
        pass
    
class FirstComeFirstServe(AlgorithmPlanner):
    def __init__(self):
        self.procesess = queue.Queue()
    def get_process(self):
        return self.procesess.get()
    def put_process(self, proc):
        self.procesess.put(proc)