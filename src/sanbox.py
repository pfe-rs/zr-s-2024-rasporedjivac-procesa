from operatingSystem import OS
from cpu import CPU
from process import Process
from algorithmPlanner import *

fcfs = FirstComeFirstServe()
spf = ShortestProcessFirst()

cpu = CPU()
os = OS(cpu, fcfs)
cpu.setOS(os)

#process1 = Process(5, 10, 1)
#os.createProcess(process1)
#process2 = Process(3, 20, 2)
#os.createProcess(process2)
#process3 = Process(2, 15, 3)
#os.createProcess(process3)s

print("--------------------------------")
os.cpuScheduler.setPrioritizedAlgorithm(spf)

process4 = Process(5, 50, 1)
os.createProcess(process4)
process5 = Process(7, 30, 2)
os.createProcess(process5)
process6 = Process(3, 15, 3)
os.createProcess(process6)


cpu.run()

