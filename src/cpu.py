import time

class CPU:
    def setOS(self, os):
        self.os = os

    def run(self):
        while self.os.hasProcesses():
            proc = self.os.getProcess()
            if not proc:
                time.sleep(0.001)
            else:
                if proc.remainingIterations > 0:
                    print("{:.3f}".format(time.time()), ": Process [", proc.id, "] is running.", sep='')

                    time0 = time.time()
                    stop = False

                    for i in range(proc.breakpoint, proc.size):
                        if proc.runningTime < 0.005:
                            time1 = time.time()
                            proc.runningTime = time1 - time0
                        else:
                            proc.breakpoint = i
                            proc.runningTime = 0
                            stop = True
                            
                    if stop:
                        self.os.cpuScheduler.putProcess(proc)
                        stop = False
                        continue
                
                    proc.remainingIterations -= 1
                    if proc.sleepInterval > 0: #ako je sleepInterval is 0, no need to sleep
                        self.os.sleep(proc)
                else:
                    self.os.finishProcess(proc)
