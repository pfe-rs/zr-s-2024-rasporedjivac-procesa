os.createProcess(proc) #scheduler.addProcess(proc) totalProcesses++
def run():
    while os.hasProcesses(): #postoje procesi koji se izvrsavaju (ready ili blocked) total processes > 0
        proc = os.getProcess() # scheduler.getProcess()
        if not proc:
            time.sleep()
        else:
            if proc.remainingIterations > 0:
                dowork(proc.workAmout) #for i in range(proc.workAmount) dummy work

                proc.remainingIterations -= 1
                os.sleep(proc.sleepTime, proc)
            else:
                os.exit(proc) #totall processes--

                