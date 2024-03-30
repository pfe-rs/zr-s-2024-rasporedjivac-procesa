import pytest
from algorithmPlanner import *
from process import Process
from operatingSystem import OS
from cpu import CPU

def test_queue_order():
    cpu = CPU()
    os = OS(cpu, FirstComeFirstServe())
    cpu.setOS(os)
    
    p1 = Process(5, 30, 2) 
    p3 = Process(6, 20, 2)
    p2 = Process(3, 25, 1) 
    
    os.createProcess(p1)
    os.createProcess(p2)
    os.createProcess(p3)


    assert os.getProcess() == p1
    assert os.getProcess() == p2
    assert os.getProcess() == p3

def test_priority_queue_order():
    cpu = CPU()
    os = OS(cpu, ShortestProcessFirst())
    cpu.setOS(os)
    
    p1 = Process(5, 30, 2) 
    p2 = Process(6, 20, 2)
    p3 = Process(3, 25, 1) 
    
    os.createProcess(p1)
    os.createProcess(p2)
    os.createProcess(p3)


    assert os.getProcess() == p2
    assert os.getProcess() == p3
    assert os.getProcess() == p1

