from operatingSystem import OS
from cpu import CPU
from algorithmPlanner import *
import threading
import threading

class System:
    _instance = None

    def __new__(cnt):
        if not cnt._instance:
            cnt._instance = super().__new__(cnt)
        return cnt._instance

    def __init__(self, n = 1):
        self.mutex = threading.Lock()
        self.cpu = [CPU() for _ in range(5)]
        self.os = OS(FirstComeFirstServe())
        
        for i in range(n):
            self.cpu[i].setOS(self.os)
            t = threading.Thread(target=self.cpu[i].run)
            self.threads.append(t)

    def startThreads(self):
        for thread in self.threads:
            thread.start()
        
        self.joinThreads()
    
    def joinThreads(self):  
        for thread in self.threads:
            thread.join()

    