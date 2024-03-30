from operatingSystem import OS
from process import Process
from algorithmPlanner import *
from system import System

fcfs = FirstComeFirstServe()
spf = ShortestProcessFirst()

sys = System(2)
os = OS(sys, fcfs)
sys.setOS(os)

#process1 = Process(5, 10, 1)
#os.createProcess(process1)
#process2 = Process(3, 20, 2)
#os.createProcess(process2)
#process3 = Process(2, 15, 3)
#os.createProcess(process3)s

print("--------------------------------")
os.cpuScheduler.setPrioritizedAlgorithm(spf)

process0 = Process(5, 20, 1.0)
os.createProcess(process0)
process1 = Process(7, 50, 2.0)
os.createProcess(process1)
process2 = Process(3, 30, 3.0)
os.createProcess(process2)
process3 = Process(5, 15, 2.5)
os.createProcess(process3)

sys.startThreads()

