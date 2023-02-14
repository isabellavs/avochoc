import sys
import io
import time
from pyskiplist import SkipList

def slurpFile():

    st = time.time()
    buffData = []
    with open('datastructures2.csv', mode='r') as inData:
        buffData = inData.read().splitlines()

    sl = SkipList()
    for line in buffData:
        y = line.rstrip().partition(';') # 3.61
        sl.insert(y[0], y[2])

    print(f'{time.time() - st} : slurp duration')
    return sl
    
def readFile():

    st = time.time()
    sl = SkipList()

    with open('datastructures2.csv') as inData:
        for line in inData.readlines():
            y = line.partition(';') # 3.5
            sl.insert(y[0], y[2][:-1])

    print(f'{time.time() - st} : read duration')
    return sl

def searchFile():
    print('search')

def insertRec():
    print('insert')

def updateRec():
    print('update')

def deleteRec():
    print('delete')

def main():

    st = time.time()
    sl = SkipList()

    #sl = slurpFile()
    sl = readFile()
    st2 = time.time()

    print(sl.search('Chauncey'))
    print(f'{time.time() -st2} : search')
    print(f'{time.time() - st} : main')

if __name__ == "__main__":
    
    main()
    