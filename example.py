import KCSCApi

print()
print()

stop1 = KCSCApi.KCSCApiReturn()
stop1.stopId = 1601
rc = KCSCApi.getNow(stop1)
if rc != 0:
    print(rc)
else:
    print("Stop : " + stop1.stopName)
    print()
    print("Next car at: " + stop1.nextTime12)
    print("            ", str(stop1.nextTime) + " unix epoch time")
    print("            ", str(stop1.nextTimeDT) + " datetime")
    print("Next car in: ", str(stop1.nextSecs) + " seconds")
    print()
    print("Next car occupancy: ", stop1.nextOccupancy, "%")
    print()
    print("----------------------------------------------")
    print()

stop1secondTrain = KCSCApi.KCSCApiReturn()
stop1secondTrain.stopId = 1601
stop1secondTrain.predictIndex = 1
rc = KCSCApi.getNow(stop1secondTrain)
if rc != 0:
    print(rc)
else:
    print("Stop : " + stop1secondTrain.stopName)
    print()
    print("Next car at: " + stop1secondTrain.nextTime12)
    print("            ", str(stop1secondTrain.nextTime) + " unix epoch time")
    print("            ", str(stop1secondTrain.nextTimeDT) + " datetime")
    print("Next car in: ", str(stop1secondTrain.nextSecs) + " seconds")
    print()
    print("Next car occupancy: ", stop1secondTrain.nextOccupancy, "%")
    print()
    print("----------------------------------------------")
    print()

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



