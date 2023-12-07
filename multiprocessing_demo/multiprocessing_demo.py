from multiprocessing import Pool, Process
import os
import time


def printProcessMetadata(processName: str) -> None:
    time.sleep(5)
    print('process name:', processName)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print('\n')

def printMessage(message: str) -> None:
    printProcessMetadata()
    print(message)




if __name__ == '__main__':  
    # p = Pool(5)
    # print(p.map(printMessage, ["Message 1", "Message 2", "Message 3"]))
    
    print("CPU count: ", os.cpu_count())  

    process1 = Process(target=printProcessMetadata, args=('Process 1',))
    process2 = Process(target=printProcessMetadata, args=('Process 2',))
    process3 = Process(target=printProcessMetadata, args=('Process 3',))
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()

