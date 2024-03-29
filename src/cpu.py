import time
import cpu
from operatingSystem import OS

class CPU:
    _instance = None

    def __new__(cnt):
        if not cnt._instance:
            cnt._instance = super().__new__(cnt)
        return cnt._instance

    def setOS(self, os):
        self.os = os

    def run(self):
        while self.os.hasProcesses():
            proc = self.os.getProcess()
            if not proc:
                time.sleep(1)
            else:
                if proc.remainingIterations > 0:
                    print("Process [", proc.id, "] is running.", sep='')

                    for i in range(proc.size):
                        continue
                
                    proc.remainingIterations -= 1
                    if proc.sleepInterval > 0: #ako je sleepInterval is 0, no need to sleep
                        self.os.sleep(proc)
                else:
                    self.os.finishProcess(proc)
