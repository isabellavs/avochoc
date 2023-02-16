import random
import time
import ctypes

'''
Practical, Section A, Data Structures 2
To run:
export PYTHONHASHSEED=0;python3 movieList.py
'''
#------------------------------------------------------------------------------
class Node:
  def __init__(self, title=None, level=0):
      
    self.title = title
    self.next = [None] * (level + 1)
    self.key = None
    if title is not None:
      self.key = ctypes.c_size_t(hash(title)).value

#------------------------------------------------------------------------------
class SkipList:
  def __init__(self, maxLevels=18):
      
    self.maxLevels = maxLevels
    self.head = Node(None, maxLevels)
    self.level = 0
    self.length = 0
        
  #--------------------------------------------------------------------------
  def flipCoin(self):
      
    choices = [True, False]
    return random.choice(choices)
    
  #--------------------------------------------------------------------------
  def getRandomLevel(self):
    
    level = 0
    while self.flipCoin() and level < self.maxLevels:
      level += 1
      
    return level
  
  #--------------------------------------------------------------------------
  def insert(self, title):
    
    updateList = [None] * (self.maxLevels + 1)
    head = self.head
    key = ctypes.c_size_t(hash(title)).value
    
    for i in range(self.level, -1, -1):
      while (head.next[i] is not None) and (head.next[i].key < key):
        head = head.next[i]
      updateList[i] = head
    
    head = head.next[0]

    if head is None or head.key != key:
      
      newLevel = self.getRandomLevel()
      if newLevel > self.level:
        for i in range(self.level + 1, newLevel + 1):
          updateList[i] = self.head
        self.level = newLevel
        
      head = Node(title, newLevel)
      
      for i in range(newLevel + 1):
        head.next[i] = updateList[i].next[i]
        updateList[i].next[i] = head

      self.length += 1
      
    return
  
  #--------------------------------------------------------------------------
  def locateKey(self, key):
    
    head = self.head
    
    for i in range(self.level, -1, -1):
      while (head.next[i] is not None) and (head.next[i].key < key):
        head = head.next[i]
        
    head = head.next[0]
    
    if head is not None and head.key == key:
      return head
      
    return Node()
  
  #--------------------------------------------------------------------------
  def searchKey(self, key):

    return self.locateKey(key)
  
  #--------------------------------------------------------------------------
  def searchTitle(self, title):
    
    key = ctypes.c_size_t(hash(title)).value
    return self.locateKey(key)

#------------------------------------------------------------------------------
def testSL(sl):
  
  print('\ntests:\n------')

  print(f"search 'Zzyzx (Special Edition)' by title:")
  st = time.time()
  print(sl.searchTitle("Zzyzx (Special Edition)\n").title)
  print(f'{time.time() - st}: searched title\n')
  
  print(f"search 'Zzyzx (Special Edition)' by key:")
  st = time.time()
  print(sl.searchKey(10029677178616478400).title)
  print(f'{time.time() - st}: searched key\n')
  
  print('search more titles')
  st = time.time()
  print(sl.searchTitle("ZZ Top: Live In Germany 1982\n").title)
  print(sl.searchTitle("Hook 'N' Shoot: 2007 Women's Grand Prix\n").title)
  print(sl.searchTitle("!Hero: The Rock Opera: Live On Stage (2-Disc Collector's Edition)\n").title)
  print(sl.searchTitle("Classic TV Westerns (2-Disc): Bonanza: Badge Without Honor / The Lone Ranger: Pete & Pedro / Annie Oakley: ... / ...\n").title)
  print(sl.searchTitle("Coleccion Pedro Infante: Que Te Ha Dado Esa Mujer?!\n").title)
  print(sl.searchTitle("Coleman Hawkins / Harry 'Sweets' Edison: London Concert 1964\n").title)
  print(sl.searchTitle("Hooked On Baby: Read;2007-01-09 00:00;102199;2010-02-12 00:00;;;;;;;\n").title)
  print(sl.searchTitle("Build Your Character 3D Content Creation With SOFTIMAGE\XSI\n").title)
  print(sl.searchTitle("$ [Dollars]\n").title)
  print(sl.searchTitle("'I Don't Have A Problem': The Path To Addiction\n").title)
  print(f'{time.time() - st}: searched 10 titles')
  
  print('\nsearch bogus title')
  st = time.time()
  print(sl.searchTitle("bogus\n").title)
  print(f'{time.time() - st}: searched 9 titles')
    
#------------------------------------------------------------------------------
def main():

    st = time.time()
    sl = SkipList()

    try:
      
      with open('datastructures3.csv', mode='r', encoding=None) as inData:
        for line in inData.readlines():
          sl.insert((line))
      
      print(f'\n{time.time() - st}: file read and list creation duration')
      print(f'list length: {sl.length}')
      
    except Exception as e:
      print(f"error: {e}")
      
    testSL(sl)
    print(f'\n{time.time() - st}: total time')

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#------------------------------------------------------------------------------
'''
Notes:
  option: store lists with similair titles in the nodes
'''