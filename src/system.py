from operatingSystem import OS
from cpu import CPU
from algorithmPlanner import *
import threading


class System:
    _instance = None

    def __init__(self, nocpu = 1):
        self.mutex = threading.Lock()
        self.cpu = [CPU() for _ in range(nocpu)]
        self.numberOfCPUs = nocpu
        self.threads = []

    def startThreads(self):
        for thread in self.threads:
            thread.start()
        
        self.joinThreads()
    
    def joinThreads(self):  
        for thread in self.threads:
            thread.join()

    def setOS(self, os):
        self.os = os
        
        for i in range(self.numberOfCPUs):
            self.cpu[i].setOS(self.os)
            t = threading.Thread(target=self.cpu[i].run)
            self.threads.append(t)

    