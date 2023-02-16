import time
import sys
'''
Caveats: 
  This could bomb out spectacularly on a 32bit system.
  Earlier versions of Python may throw integer overflow exceptions
Resources (some of it):
  https://stackoverflow.com/questions/63922356/how-python-is-working-with-a-number-bigger-than-the-64-bit-unsigned-integer-limi
  And, pick the useful bits here:
  https://stackoverflow.com/questions/52151647/integer-overflow-in-python3
'''
def main():
  
  st = time.time()
  numBuff = []
  total = 0
  
  try:
    with open('researchlv1.csv', 'r') as inNum:
        for line in inNum:
          total += int(line)
  except Exception as err:
    print(f"Error: {err}")
    
  print(numBuff)
  print(total)
  print(sys.maxsize)
  
if __name__ == '__main__':
  main()