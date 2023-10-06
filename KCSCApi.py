import requests
from datetime import datetime

class KCSCApiReturn:
    def __init__(self, stopId = 0, predictIndex = 0, stopName=None, nextTime=0, nextTimeDT=0, nextTime12=0, nextSecs=0, nextMin=0,
                 nextDeparture=False, nextOccupancy=0, nextOccupancyCount=0, nextOccupancyStatus=None, nextTripId=0, nextVehicleId=0, isLate=False):
        self.stopId = 0
        self.predictIndex = 0
        self.stopName = None
        self.nextTime = 0
        self.nextTimeDT = 0
        self.nextTime12 = 0
        self.nextSecs = 0
        self.nextMin = 0
        self.nextDeparture = False
        self.nextOccupancy = 0
        self.nextOccupancyCount = 0
        self.nextOccupancyStatus = None
        self.nextTripId=0
        self.nextVehicleId = 0
        self.isLate = False

def getNow(apistuct):
    api_url = 'https://kcata-transit.citypost.us/predictions?stopId=' + str(apistuct.stopId)
    payload = (requests.get(api_url))
    rc = payload.status_code

    if rc != 200:
        return rc
    
    response = payload.json()

    if "errorCode" in response:
        rc = response["errorCode"]
        return rc
    else:
        data = response["data"]["predictionsData"][0]
        apistuct.stopName = data['stopName']
        stopLen = len(apistuct.stopName)
        stopDir = apistuct.stopName[stopLen - 2]
        if stopDir == "S":
            apistuct.stopName = apistuct.stopName[:(stopLen - 3)]
            apistuct.stopName = apistuct.stopName + " Southbound"
        elif stopDir == "N":
            apistuct.stopName = apistuct.stopName[:(stopLen - 3)]
            apistuct.stopName = apistuct.stopName + " Northbound"
        elif stopDir == "E":
            apistuct.stopName = apistuct.stopName[:(stopLen - 3)]
            apistuct.stopName = apistuct.stopName + " Eastbound"
        elif stopDir == "W":
            apistuct.stopName = apistuct.stopName[:(stopLen - 3)]
            apistuct.stopName = apistuct.stopName + " Westbound"
        apistuct.nextTime = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['time']
        apistuct.nextTimeDT = datetime.fromtimestamp(apistuct.nextTime)
        apistuct.nextTime12 = apistuct.nextTimeDT.strftime("%I:%M %p")
        apistuct.nextSecs = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['sec']
        apistuct.nextMin = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['min']
        apistuct.nextOccupancy = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['occupancyPercent']
        apistuct.nextOccupancyCount = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['occupancyCount']
        apistuct.nextOccupancyStatus = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['occupancyStatus']
        apistuct.nextTripId = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['tripId']
        apistuct.nextVehicleId = data['destinations'][0]['predictions'][int(apistuct.predictIndex)]['vehicleId']
        if apistuct.nextSecs < 0:
            apistuct.isLate = True
        return 0