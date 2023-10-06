import KCSCApi

print()
print()

stop1 = KCSCApi.KCSCApiReturn() #create a new object with type KCSCApiReturn
stop1.stopId = 1601             #set the stopId to be River Market West Southbound
rc = KCSCApi.getNow(stop1)      #get the payload for the given stopId

if rc != 0:                     #if we do not succeed, print the error and escape
    print(rc)
else:                           #if we succeed, print all of the data in the object formatted
    print("Stop : " + stop1.stopName)
    print()
    print("Next car at: " + stop1.nextTime12)
    print("            ", str(stop1.nextTime) + " unix epoch time")
    print("            ", str(stop1.nextTimeDT) + " datetime")
    print("Next car in: ", str(stop1.nextSecs) + " seconds")
    print()
    print("Departure State: ", str(stop1.nextDeparture))
    print()
    print("Next car occupancy: ", stop1.nextOccupancy, "%")
    print("                    ", stop1.nextOccupancyCount, " people")
    print("                    ", stop1.nextOccupancyStatus)
    print()
    print("Next car tripId: ", stop1.nextTripId)
    print()
    print("Next car vehicleId: ", stop1.nextVehicleId)
    print()
    print("----------------------------------------------")
    print()

##  do the same thing, but this time get the streetcar coming after the next streetcar. This can be useful if time is too low to get to the next car

stop1secondTrain = KCSCApi.KCSCApiReturn()
stop1secondTrain.stopId = 1601
stop1secondTrain.predictIndex = 1
rc = KCSCApi.getNow(stop1secondTrain)
if rc != 0:
    print(rc)
else:
    if stop1secondTrain.nextSecs < 120:
        print("next car arrives at " + stop1secondTrain.stopName + " in: " + str(stop1.nextSecs) + " seconds which is less than two minutes")
        print()
        print("Getting next car")
        print()
        print("Stop : " + stop1secondTrain.stopName)
        print()
        print("Next car at: " + stop1secondTrain.nextTime12)
        print("            ", str(stop1secondTrain.nextTime) + " unix epoch time")
        print("            ", str(stop1secondTrain.nextTimeDT) + " datetime")
        print("Next car in: ", str(stop1secondTrain.nextSecs) + " seconds")
        print()
        print("Next car occupancy: ", stop1secondTrain.nextOccupancy, "%")
        print("                    ", stop1secondTrain.nextOccupancyCount, " people")
        print("                    ", stop1secondTrain.nextOccupancyStatus)
        print()
        print("----------------------------------------------")
        print()

## same as above, but this time get the data for City Market Eastbound

stop2 = KCSCApi.KCSCApiReturn()
stop2.stopId = 1615
rc = KCSCApi.getNow(stop2)
if rc != 0:
    print(rc)
else:
    print("Stop : " + stop2.stopName)
    print()
    print("Next car at: " + stop2.nextTime12)
    print("            ", str(stop2.nextTime) + " unix epoch time")
    print("            ", str(stop2.nextTimeDT) + " datetime")
    print("Next car in: ", str(stop2.nextSecs) + " seconds")
    print()
    print("Next car occupancy: ", stop2.nextOccupancy, "%")



