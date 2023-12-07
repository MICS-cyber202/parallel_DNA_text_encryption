from multiprocessing import Pool

def printMessage(message: str) -> None:
    print(message)


if __name__ == '__main__':  
    p = Pool(5)
    print(p.map(printMessage, ["Message 1", "Message 2", "Message 3"]))

