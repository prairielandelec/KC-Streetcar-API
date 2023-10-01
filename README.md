# KC-Streetcar-API
A python interface to break down the undocumented Kansas City Streetcar Time API

The public streetcar has a handy tracker that can be found here:
https://kcstreetcar.org/route/streetcar-tracker/


This python module just helps break down the API calls that happen in the backend of that tracker page since the API is undocumented.


The API uses a "stopID" to identify the stops allong the route. This is also undocumented but I found the minimum and maximum stopID's and created this list:

| stopId  | Stop Name |
| ------------- | ------------- |
|  1601  |  RIVER MARKET WEST ON DELAWARE AT 4TH ST Southbound  |
|  1602  |  NORTH LOOP ON MAIN AT 7TH ST Southbound  |
|  1603  |  LIBRARY ON MAIN AT 9TH ST Southbound  |
|  1604  |  METRO CENTER ON MAIN AT 12TH ST Southbound  |
|  1605  |  POWER & LIGHT ON MAIN AT 14TH ST Southbound  |
|  1606  |  KAUFFMAN CENTER ON MAIN AT 16TH ST Southbound  |
|  1607  |  CROSSROADS ON MAIN AT 19TH ST Southbound  |
|  1608  |  UNION STATION ON MAIN AT PERSHING Southbound  |
|  1609  |  CROSSROADS ON MAIN AT 19TH ST Northbound  |
|  1610  |  KAUFFMAN CENTER ON MAIN AT 16TH ST Northbound  |
|  1611  |  POWER & LIGHT ON MAIN AT 14TH ST Northbound  |
|  1612  |  METRO CENTER ON MAIN AT 12TH ST Northbound  |
|  1613  |  LIBRARY ON MAIN AT 9TH ST Northbound  |
|  1614  |  NORTH LOOP ON MAIN AT 7TH ST Northbound  |
|  1615  |  CITY MARKET ON WALNUT AT 5TH ST Eastbound  |

Pick your stopId and use it with this module to get the following information for the given stop:

| Data Name | Data Type | Description |
| --------- | --------- | ------------------------------------------------ |
| stopName  | str       | the API's name for the stop |
| nextTime  | str       | when the next train is expected in a formatted 12 hour clock |
| nextTimeDT  | datetime  | a datetime object that states when the next train is expected |
| nextTimestamp | float | a timestamp in UNIX Epoch time to do math with (in Kansas City Time) |
| nextSecs  | int       | a nice small integer to do more basic math with |
| isLate    | bool      | a boolean to indicate if the next train is late, useful for indicators |
