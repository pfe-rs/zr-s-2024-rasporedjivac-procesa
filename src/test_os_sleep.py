import pytest
from algorithmPlanner import *
from process import Process
from operatingSystem import OS
from cpu import CPU
import time

def test_os_sleep():
    cpu = CPU()
    os = OS(cpu, FirstComeFirstServe())
    cpu.setOS(os)
    
    time1 = 1.0
    time2 = 2.0
    time3 = 3.0
    
    p1 = Process(5, 30, time1) 
    p3 = Process(6, 20, time2)
    p2 = Process(3, 25, time3) 
    
    os.createProcess(p1)
    os.createProcess(p2)
    os.createProcess(p3)
    
    dt = 3.0
    
    t1_0 = time.time()
    os.sleep(p1)
    t1_1 = time.time()
    assert abs(t1_1 - (t1_0 + time1)) <= dt
    
    t2_0 = time.time()
    os.sleep(p2)
    t2_1 = time.time()
    assert abs(t2_1 - (t2_0 - time2)) <= dt
    
    t3_0 = time.time()
    os.sleep(p3)
    t3_1 = time.time()
    assert abs(t3_1 - (t3_0 - time3)) <= dt