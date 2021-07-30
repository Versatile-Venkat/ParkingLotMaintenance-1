from slot import CreateSlot
from parkingDetails import ParkingDetails

def execute(inputAsList):
  lotCreated=False
  for i in inputAsList:
    t=i.split(" ")
    command=t[0]
    if command == "Create_parking_lot":
      if(lotCreated==False):
        lengthOfParkingLot=(int)(t[1])
        if lengthOfParkingLot<=1000:
          slots = CreateSlot(lengthOfParkingLot)
          print('Creating parking of '+t[1]+' lots')
          lotCreated=True
        else:
          print('The maximum limit of parking lot size is 1000')
      else:
        print('Parking lot aldready created. Modification of size is not allowed')

    elif command == "Park":
      if(lotCreated):
        slotnum=slots.getSlot()
        if(slotnum != -1):
          ParkingDetails().parkVehicle(slotnum,t[1],t[3])
          print('Car with vehicle registration number \"'+t[1]+'\" has been parked at slot number %d'%slotnum)
        else:
          print('no place to park')
      else:
        print("Lot is not created yet! Please do create space for parking")
    
    elif command=='Slot_numbers_for_driver_of_age':
      slotlist=ParkingDetails().getSlotByAgeOfDriver(t[1])
      if len(slotlist)>0:
        print('Slot numbers for driver of age '+t[1]+' is ')
        for i in slotlist:
          print(i,end=" ")
      else:
        print('The driver of age'+t[1]+'is not present in any slot')


    elif command=='Slot_number_for_car_with_number':
      carnumber=t[1]
      slotnums=ParkingDetails().getSlotByVehicleNumber(carnumber)
      if slotnums>0:
          print('Slot number for car with number '+t[1]+' is ',end=" ")
          print(slotnums)
      else:
        print('There is no car with the number'+carnumber)

    elif command=='Vehicle_registration_number_for_driver_of_age':
      age=t[1]
      numbers=ParkingDetails().getVehicleNumbersByAge(age)
      if len(numbers)>0:
        print('Vehicle numbers for drivers of age '+age+' is ',end="")
        for i in numbers:
          print(i,end=" ")
      else:
        print('No vehicle found for age '+age)

    elif command=="Leave":
      slotToEmpty=(int)(t[1])
      
      if slots.deleteSlot(slotToEmpty)==True:
        data=ParkingDetails().getSlotDetails(slotToEmpty)
        if len(data)>0:
          print('Slot number %d vacated, the car with vehicle registration number %s left the space, the driver of the car was of age %s'%(slotToEmpty,data[0],data[1]))
        else:
          print('slot empty')
      else:
        print('slot is aldready empty')
    
    else:
      print('enter a valid command')
    print()
