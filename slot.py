class CreateSlot:
  #Initialises the slot in the system.
  empty=set() #to keep track of empty slots
  full=set() #to keep track of slots which are full
  def __init__(self,size):
    self.size=size
    self.empty=set()
    self.full=set()
    for i in range(1,size+1):
      self.empty.add(i)
  def getSlot(self): #returns a slot number if there is space to park. Else returns -1
    if len(self.empty)>0:
      m=min(self.empty)
      self.empty.remove(m)
      self.full.add(m)
      return m
    else:
      return -1
  def deleteSlot(self,slot):
    #Deletes the slot which is to be freed. If it is actually free, returns -1
    if slot in self.full:
      self.full.remove(slot)
      self.empty.add(slot)
      return True
    else:
      return False