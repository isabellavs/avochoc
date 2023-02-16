import time

def main():
  
  st = time.time()
  numList = []

  with open('algorithms1.csv', 'r') as inNum:
    for line in inNum:
      numList.append(int(line.rstrip()))
      
  fileTime = time.time() - st  
  st1 = time.time()
  n = len(numList)
  
  for i in range(n):
    for j in range(0, n -i -1):
      if numList[j] > numList[j + 1]:
        numList[j], numList[j + 1] = numList[j + 1], numList[j]

  sortTime = time.time() - st1
  print(numList)
  print(f'\n{fileTime}: consumed file')
  print(f'{sortTime}: sort time')
  print(f'{time.time() - st}: all done')
  
if __name__ == '__main__':
  main()