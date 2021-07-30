from slotRegister import LotRegister

class ParkingDetails:
  
  slotDict={} #slot:[v.no,age]
  
  def parkVehicle(self,slot,vehicleNum,age):
    #creates an object with the vehicle details and fixes a slot
    register=LotRegister(slot,vehicleNum,age)
    self.slotDict[slot]=register

  def getSlotDetails(self,slotnumber):
    #get the vehiclenumber and age of the driver of particular slot
    data=[]
    if slotnumber in self.slotDict:
      data.append(self.slotDict[slotnumber].vehicleNumber)
      data.append(self.slotDict[slotnumber].age)
    return data


  def getSlotByAgeOfDriver(self,age):
    #returns all slots that has vehicle driven by a particular age driver
    result=[]
    for i in self.slotDict.keys():
      if i in self.slotDict and self.slotDict[i].age==age:
        result.append(i)
    return result
  
  def getSlotByVehicleNumber(self,number):
    #returns the slot where the particular vehicle is parked
    for i in self.slotDict.keys():
      if self.slotDict[i].vehicleNumber==number:
        return i
    return -1
  
  
  def getVehicleNumbersByAge(self,age):
    #get all vehicle numbers driven by a particular age driver
    result=[]
    for i in self.slotDict.keys():
      if self.slotDict[i].age==age:
        result.append(self.slotDict[i].vehicleNumber)
    return result
  

    
