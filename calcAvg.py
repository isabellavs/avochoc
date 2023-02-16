import sys

def getAvg():
  
  inNumbers = sys.argv[1].split(',')

  try:
    
    total = 0
    cnt = 0
    
    for num in inNumbers:
      total += float(num)
      cnt += 1

    avg = float(total) / float(cnt)
      
    print(f"Total:{total}, Count:{cnt}, Average is {str('%.2f' % avg)}")
    
  # because we have to cater for possible non-numbers    
  except Exception as err:
    print(f"Error:{err}")
  
if __name__ == "__main__":
  
  if len(sys.argv) < 2:
    print('Usage: python3 calcAvg.py 1,2,3,4,5.44')
  else:
    getAvg()