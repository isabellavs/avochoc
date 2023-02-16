import random
import time

'''
Practical, Section A, Data Structures 2
'''
#------------------------------------------------------------------------------
class Node:
  def __init__(self, first_name=None, last_name=None, level=0):
      
    self.values = (first_name, last_name)
    self.next = [None] * (level + 1)
    
    self.key = None
    if first_name is not None:
      self.key = first_name
    if last_name is not None:
      self.key += last_name

#------------------------------------------------------------------------------
class SkipList:
  def __init__(self, maxLevels=10):
      
    self.maxLevels = maxLevels
    self.head = Node(None, None, maxLevels)
    self.level = 0
        
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
  def getUpdateList(self, key):
    
    update = [None] * (self.maxLevels + 1)
    head = self.head
    
    for i in range(self.maxLevels, -1, -1):
      while (head.next[i] is not None) and (head.next[i].key < key):
        head = head.next[i]
      update[i] = head
    
    return update
  
  #--------------------------------------------------------------------------
  def insert(self, first_name, last_name):
    
    updateList = [None] * (self.maxLevels + 1)
    head = self.head
    key = first_name + last_name
    
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
        
      head = Node(first_name, last_name, newLevel)
      
      for i in range(newLevel + 1):
        head.next[i] = updateList[i].next[i]
        updateList[i].next[i] = head
  
  #--------------------------------------------------------------------------
  def search(self, first_name, last_name):
    
    key = None
    if first_name is not None:
      key = first_name
    if last_name is not None:
      key += last_name
    
    head = self.head
    
    for i in range(self.level, -1, -1):
      while (head.next[i] is not None) and (head.next[i].key < key):
        head = head.next[i]
        
    head = head.next[0]
    
    if head is not None and head.key == key:
      return head
      
    return Node()
    
  #--------------------------------------------------------------------------
  def remove(self, first_name, last_name):
    
    current = None
    
    if (current := self.search(first_name, last_name)).key is None:
      return None
  
    updateList = self.getUpdateList(current.key)
    
    for i in range((len(current.next) -1) , -1, -1):
      updateList[i].next[i] = current.next[i]
      if self.head.next[i] is None:
        self.maxLevels -= 1
    
    return Node()
    
  #--------------------------------------------------------------------------
  def update(self, first_name, last_name, newFirstName, newLastName):

    self.remove(first_name, last_name)
    self.insert(newFirstName, newLastName)

#------------------------------------------------------------------------------
def testSL(sl):
  
  print('testing search:\n--------------:')
  st2 = time.time()
  print(sl.search('James', 'Butt').values)
  print(f'{time.time() - st2}: searched one\n')
  st2 = time.time()
  print(sl.search('Mitsue', 'Tollner').values)
  print(sl.search('Someone', 'Fake').values)
  print(sl.search('James', 'Butt').values)
  print(f'{time.time() - st2}: searched two and one false\n')
  
  print('test insert:\n-----------:')
  st2 = time.time()
  sl.insert('James', 'Butter')
  sl.insert('Sara', 'van Goodie')
  sl.insert('Kirk', 'Somebody')
  print(f'{time.time() - st2}: inserted three\n')
  print(f"find last insert: {sl.search('Sara', 'van Goodie').values}\n")
  print(f"find last insert: {sl.search('Kirk', 'Somebody').values}\n")
  print(f"find last insert: {sl.search('James', 'Butter').values}\n")
  
  print('test update:\n-----------:\n')
  print(f"updating ('Mitsue', 'Tollner') to ('Mitze', 'Tollner')")
  st2 = time.time()
  sl.update('Mitsue', 'Tollner', 'Mitze', 'Tollner')
  print(f'{time.time() - st2}: updated rec\n')
  print(f"search for old rec: {sl.search('Mitsue', 'Tollner').values}")
  print(f"search for new rec: {sl.search('Mitze', 'Tollner').values}\n")
  
  print('test remove:\n-----------:\n')
  print(f"removing ('James','Butt')")
  st2 = time.time()
  sl.remove('James', 'Butt')
  print('search for removed item:')
  print(sl.search('James', 'Butt').values)
  print(f'{time.time() - st2}: removed item\n')
    
#------------------------------------------------------------------------------
def main():

    st = time.time()
    sl = SkipList()

    st1 = time.time()
    with open('datastructures2.csv', 'r') as inData:
        for line in inData.readlines():
            y = line.partition(';')
            sl.insert(y[0], y[2][:-1])
    print(f'\n{time.time() - st1}: file read duration\n')

    testSL(sl)

    print(f'\n{time.time() - st}: total time')

#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#------------------------------------------------------------------------------