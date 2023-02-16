import math
import time
import sys

def main():
  flen = len(sys.argv[1]) + 1  
  fact = int(sys.argv[1])

  i = 1
  frogon = []
  print(frogon)
  if (fact % 2) == 1:
    frogon.append(1)
  else:
    frogon.append(0)

  print(fact%2)
  
  while fact >= 1 and i <= fact:
    f1 = fact
    i += 1
    print(f'i -----------> {i}')
    fact = fact/i
    
    # if (fact % 2) == 0:
    #   i -= 1
    #   continue
    
    if (fact < i):
      frogon.append(i -1)
      print(f'less than i --> {fact} : {i}')
    elif (fact % 2) > 0:
      frogon.append(i)
      print(f'uneven --> {fact} : {i}')
    else:
      frogon.append(0)
      print(f'else --> {fact} : {i}')
      
    print(f'{f1}/{i}={fact}')
  
  print(i, fact, frogon)
  
if __name__ == '__main__':
  main()
  
'''
This is still a thought-process!
17:
7 = !1 + 0!2 + !3 (1 + 6)
10 = 0!1 + 2!2 + !3 (4 + 6) 

'''