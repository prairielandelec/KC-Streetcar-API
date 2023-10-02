# KC-Streetcar-API
A python interface to break down the undocumented Kansas City Streetcar Time API

The public streetcar has a handy tracker that can be found here:
https://kcstreetcar.org/route/streetcar-tracker/


This python module just helps break down the API calls that happen in the backend of that tracker page since the API is undocumented.

I have not found any documentation about rate limiting, but it does seem to occur if you poll more frequently than once per second. There is no built in rate limiting so please use responsibly and at your own risk. 

## How To Use

To use this module you need to place the KCSCApi.py file in the root directory of your project and import the file as you would any other external module
```python
import KCSCApi
```

You will also need to create an object with the type KCSCApiReturn to store your responses in and provide a stopId that you would like to receive data for (see [stopId](#stopid) documentation for list of stops and their corresponding ID's)
```python
stop1 = KCSCApi.KCSCApiReturn() #creating an object of class type KCSCApiReturn to store data
stop1.stopId = 1601 #this is the stop ID for River Market West Southbound
```

After you have created an object to store the data and provided a stop ID for that object, run the getNow function to pull the data in from the API and dump it into the individual data points. The function will return a 0 on success and the relevant HTTP error code or API error code upon failure
```python
rc = KCSCApi.getNow(stop1)
```

To grab any of the data from the object, refer to the [class table](#kcscapireturn-class) below. Data is stored in a custom class object for easy retrieval using dot notation as I am a C++ programmer primarily and dictionaries feel wrong to me.
```python
    print("Stop : " + stop1.stopName)           #this will print the name of the stop for given stopId
    print()                                     #new line
    print("Next car at: " + stop1.nextTime12)   #this will return the time of the next car in 12 hour time
```



## stopId
The API uses a "stopID" to identify the stops along the route. This is also undocumented but I found the minimum and maximum stopID's and created this list:

| stopId | Stop Name                                            |
| -------| -------------                                        |
|  1601  |  RIVER MARKET WEST ON DELAWARE AT 4TH ST Southbound  |
|  1602  |  NORTH LOOP ON MAIN AT 7TH ST Southbound             |
|  1603  |  LIBRARY ON MAIN AT 9TH ST Southbound                |
|  1604  |  METRO CENTER ON MAIN AT 12TH ST Southbound          |
|  1605  |  POWER & LIGHT ON MAIN AT 14TH ST Southbound         |
|  1606  |  KAUFFMAN CENTER ON MAIN AT 16TH ST Southbound       |
|  1607  |  CROSSROADS ON MAIN AT 19TH ST Southbound            |
|  1608  |  UNION STATION ON MAIN AT PERSHING Southbound        |
|  1609  |  CROSSROADS ON MAIN AT 19TH ST Northbound            |
|  1610  |  KAUFFMAN CENTER ON MAIN AT 16TH ST Northbound       |
|  1611  |  POWER & LIGHT ON MAIN AT 14TH ST Northbound         |
|  1612  |  METRO CENTER ON MAIN AT 12TH ST Northbound          |
|  1613  |  LIBRARY ON MAIN AT 9TH ST Northbound                |
|  1614  |  NORTH LOOP ON MAIN AT 7TH ST Northbound             |
|  1615  |  CITY MARKET ON WALNUT AT 5TH ST Eastbound           |

Pick your stopId and use it with this module to get the following information for the given stop:

## KCSCApiReturn Class

There is a class created in the module that stores the contents of the return 

| Member Name     | Data Type | Description                                                                           |
| ---------     | --------- | ------------------------------------------------                                      |
| stopId        | int       | the set stopId for the given request                                                  |
| predictIndex  | int       | the offset from the next car (1 would be the car after the next car)                  | 
| stopName      | str       | the API's name for the stop                                                           |
| nextTime      | float     | a timestamp in UNIX Epoch time to do math with (in Kansas City Time)                  |
| nextTimeDT    | datetime  | a datetime object that states when the next train is expected                         |
| nextTime12    | str       | when the next train is expected in a formatted 12 hour clock (in Kansas City Time)    |
| nextSecs      | int       | a nice small integer to do more basic math with                                       |
| nextOccupancy | int       | percentage occupancy of the next car                                                  |
| isLate        | bool      | a boolean to indicate if the next train is late, useful for indicators                |
