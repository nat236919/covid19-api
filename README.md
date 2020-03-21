<p align="center">
    <img src="https://cdn2.iconfinder.com/data/icons/covid-19-2/64/29-Doctor-256.png">
</p>

<h1>COVID2019-API</h1>

[![issues](<https://img.shields.io/github/issues/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/issues)
[![forks](<https://img.shields.io/github/forks/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/forks)
[![stars](<https://img.shields.io/github/stars/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/stars)
[![license](<https://img.shields.io/github/license/nat236919/Covid2019API>)](https://github.com/nat236919/Covid2019API/blob/master/LICENCE)

https://covid2019-api.herokuapp.com/

This API provides the information regarding '2019 Novel Coronavirus (covid-19)'. It contains a number of confirmed, death, and recovered cases based on the data provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

#### References
https://github.com/CSSEGISandData/COVID-19


## Features
1. The current data (daily updated)
2. Confirmed, Deaths, Recovered
3. The affected countries
4. Individual affected country
5. Timeseries


## How to use API (v2)
Send a request to the follwing URLs:

|  Request (GET)              |                       Description                               |
| ---------------------------- | -------------------------------------------------------------- |
| https://covid2019-api.herokuapp.com/v2/current     | Get all data from all the reportedly affected countries (List of Object) |
| https://covid2019-api.herokuapp.com/v2/total  | Get the total numbers of Confirmed, Deaths, and Recovered |
| https://covid2019-api.herokuapp.com/v2/confirmed   | Get the total number of Confirmed cases |
| https://covid2019-api.herokuapp.com/v2/deaths | Get the total number of Deaths |
| https://covid2019-api.herokuapp.com/v2/recovered | Get the total number of Recovered cases |
| https://covid2019-api.herokuapp.com/v2/country/china | Search a country by a key name (*space may be needed) |
| https://covid2019-api.herokuapp.com/v2/country/kr | Search a country by an [ISO country code (alpha2)] (https://www.iban.com country-codes) |

#### Examples API (v2)

1. Get current data
```python
https://covid2019-api.herokuapp.com/v2/current
{"data": [{
    "location": "China",
    "confirmed": 80945,
    "deaths": 3180,
    "recovered": 64196
    },
    {
    "location": "Italy",
    "confirmed": 17660,
    "deaths": 1266,
    "recovered": 1439
    }.....n],
"dt": "3/13/20",
"ts": 1584028800}
```

2. Get total data
```python
https://covid2019-api.herokuapp.com/v2/total
{
  "data": {
    "confirmed": 145193,
    "deaths": 5404,
    "recovered": 70251
  },
  "dt": "3/13/20",
  "ts": 1584028800
}
```

3. Get confirmed cases
```python
https://covid2019-api.herokuapp.com/v2/confirmed
{
  "data": 145193,
  "dt": "3/13/20",
  "ts": 1584028800
}
```

4. Get deaths
```python
https://covid2019-api.herokuapp.com/v2/deaths
{
  "data": 5404,
  "dt": "3/13/20",
  "ts": 1584028800
}
```

5. Get recovered cases
```python
https://covid2019-api.herokuapp.com/v2/recovered
{
  "data": 70251,
  "dt": "3/13/20",
  "ts": 1584028800
}
```

6. Get a country data
```python
https://covid2019-api.herokuapp.com/v2/country/th
{
  "data":{
    "location": "Thailand",
    "confirmed": 322,
    "deaths": 1,
    "recovered": 42
  },
  "dt": "3/20/20",
  "ts": 1584633600.0
}

https://covid2019-api.herokuapp.com/v2/country/united%20kingdom
{
  "data":{
    "location": "United Kingdom",
    "confirmed": 4014,
    "deaths": 178,
    "recovered": 67
  },
  "dt": "3/20/20",
  "ts": 1584633600.0
}
```


## How to use API (v1)
Send a request to the follwing URLs:

|  Request (GET)              |                       Description                               |
| ---------------------------- | -------------------------------------------------------------- |
| https://covid2019-api.herokuapp.com/current     | Get all data from all the reportedly affected countries (Object) |
| https://covid2019-api.herokuapp.com/current_list | Get all data from all the reportedly affected countries (List, Array) |
| https://covid2019-api.herokuapp.com/total  | Get the total numbers of Confirmed, Deaths, and Recovered |
| https://covid2019-api.herokuapp.com/confirmed   | Get the total number of Confirmed cases |
| https://covid2019-api.herokuapp.com/deaths | Get the total number of Deaths |
| https://covid2019-api.herokuapp.com/recovered | Get the total number of Recovered cases |
| https://covid2019-api.herokuapp.com/countries  | Get a list of the reportedly affected countries |
| https://covid2019-api.herokuapp.com/country/mainland_china |  Search a country by a key name (refered to 'current' method) |
| https://covid2019-api.herokuapp.com/country/kr | Search a country by an [ISO country code (alpha2)] (https://www.iban.com/country-codes) |
| https://covid2019-api.herokuapp.com/timeseries/confirmed |  Get the time series - Confirmed |
| https://covid2019-api.herokuapp.com/timeseries/deaths |  Get the time series - Deaths |
| https://covid2019-api.herokuapp.com/timeseries/recovered | Get the time series - Recovered |

#### Examples API (v1)

1. Get current data
```python
https://covid2019-api.herokuapp.com/current
{"Mainland_China":{"confirmed":44641,"deaths":1113,"recovered":4730},"Thailand":{"confirmed":33,"deaths":0,"recovered":10},"Japan":{"confirmed":26,"deaths":0,"recovered":9},"South_Korea":{"confirmed":28,"deaths":0,"recovered":4},"Taiwan":{"confirmed":18,"deaths":0,"recovered":1},"US":{"confirmed":13,"deaths":0,"recovered":3},"Macau":{"confirmed":10,"deaths":0,"recovered":1},"Hong_Kong":{"confirmed":49,"deaths":1,"recovered":0},"Singapore":{"confirmed":47,"deaths":0,"recovered":9},"Vietnam":{"confirmed":15,"deaths":0,"recovered":6},"France":{"confirmed":11,"deaths":0,"recovered":0},"Nepal":{"confirmed":1,"deaths":0,"recovered":0},"Malaysia":{"confirmed":18,"deaths":0,"recovered":3},"Canada":{"confirmed":7,"deaths":0,"recovered":0},"Australia":{"confirmed":15,"deaths":0,"recovered":2},"Cambodia":{"confirmed":1,"deaths":0,"recovered":0},"Sri_Lanka":{"confirmed":1,"deaths":0,"recovered":1},"Germany":{"confirmed":16,"deaths":0,"recovered":0},"Finland":{"confirmed":1,"deaths":0,"recovered":1},"United_Arab_Emirates":{"confirmed":8,"deaths":0,"recovered":1},"Philippines":{"confirmed":3,"deaths":1,"recovered":0},"India":{"confirmed":3,"deaths":0,"recovered":0},"Italy":{"confirmed":3,"deaths":0,"recovered":0},"UK":{"confirmed":8,"deaths":0,"recovered":0},"Russia":{"confirmed":2,"deaths":0,"recovered":0},"Sweden":{"confirmed":1,"deaths":0,"recovered":0},"Spain":{"confirmed":2,"deaths":0,"recovered":0},"Belgium":{"confirmed":1,"deaths":0,"recovered":0},"Others":{"confirmed":135,"deaths":0,"recovered":0},"dt":"2/11/20 20:44","ts":1581425040.0}

https://covid2019-api.herokuapp.com/current_list
{"countries":[{"Mainland_China":{"confirmed":66292,"deaths":1520,"recovered":7973},"Thailand":{"confirmed":33,"deaths":0,"recovered":12},"Japan":{"confirmed":29,"deaths":1,"recovered":9},"South_Korea":{"confirmed":28,"deaths":0,"recovered":7},"Taiwan":{"confirmed":18,"deaths":0,"recovered":2},"US":{"confirmed":15,"deaths":0,"recovered":3},"Macau":{"confirmed":10,"deaths":0,"recovered":3},"Hong_Kong":{"confirmed":56,"deaths":1,"recovered":1},"Singapore":{"confirmed":67,"deaths":0,"recovered":17},"Vietnam":{"confirmed":16,"deaths":0,"recovered":7},"France":{"confirmed":11,"deaths":0,"recovered":2},"Nepal":{"confirmed":1,"deaths":0,"recovered":1},"Malaysia":{"confirmed":19,"deaths":0,"recovered":3},"Canada":{"confirmed":7,"deaths":0,"recovered":1},"Australia":{"confirmed":15,"deaths":0,"recovered":8},"Cambodia":{"confirmed":1,"deaths":0,"recovered":1},"Sri_Lanka":{"confirmed":1,"deaths":0,"recovered":1},"Germany":{"confirmed":16,"deaths":0,"recovered":1},"Finland":{"confirmed":1,"deaths":0,"recovered":1},"United_Arab_Emirates":{"confirmed":8,"deaths":0,"recovered":1},"Philippines":{"confirmed":3,"deaths":1,"recovered":1},"India":{"confirmed":3,"deaths":0,"recovered":0},"Italy":{"confirmed":3,"deaths":0,"recovered":0},"UK":{"confirmed":9,"deaths":0,"recovered":1},"Russia":{"confirmed":2,"deaths":0,"recovered":2},"Sweden":{"confirmed":1,"deaths":0,"recovered":0},"Spain":{"confirmed":2,"deaths":0,"recovered":0},"Belgium":{"confirmed":1,"deaths":0,"recovered":0},"Others":{"confirmed":218,"deaths":0,"recovered":0},"Egypt":{"confirmed":1,"deaths":0,"recovered":0}}],"dt":"2/14/20","ts":1581609600.0}
```

2. Get total data
```python
https://covid2019-api.herokuapp.com/total
{"confirmed":45117,"deaths":1115,"recovered":4781,"dt":"2/11/20 20:44","ts":1581425040.0}
```

3. Get confirmed cases
```python
https://covid2019-api.herokuapp.com/confirmed
{"confirmed":45117,"dt":"2/11/20 20:44","ts":1581425040.0}
```

4. Get deaths
```python
https://covid2019-api.herokuapp.com/deaths
{"deaths":1115,"dt":"2/11/20 20:44","ts":1581425040.0}
```

5. Get recovered cases
```python
https://covid2019-api.herokuapp.com/recovered
{"recovered":4781,"dt":"2/11/20 20:44","ts":1581425040.0}
```

6. Get all the affected countries (Note: Others -> Diamond Princess cruise ship)
```python
https://covid2019-api.herokuapp.com/countries
{"countries":["Mainland_China","Thailand","Japan","South_Korea","Taiwan","US","Macau","Hong_Kong","Singapore","Vietnam","France","Nepal","Malaysia","Canada","Australia","Cambodia","Sri_Lanka","Germany","Finland","United_Arab_Emirates","Philippines","India","Italy","UK","Russia","Sweden","Spain","Belgium","Others"],"dt":"2/11/20 20:44","ts":1581425040.0}
```

7. Get a country by its key name (small letters) or ISO code (Alpha-2 code)
```python
https://covid2019-api.herokuapp.com/country/mainland_china
{"Mainland_China":{"confirmed":44641,"deaths":1113,"recovered":4730},"dt":"2/11/20 20:44","ts":1581425040.0}

https://covid2019-api.herokuapp.com/country/cn
{"Mainland_China":{"confirmed":44641,"deaths":1113,"recovered":4730},"dt":"2/11/20 20:44","ts":1581425040.0}

https://covid2019-api.herokuapp.com/country/kr
{"South_Korea":{"confirmed":28,"deaths":0,"recovered":4},"dt":"2/11/20 20:44","ts":1581425040.0}
```

8. Get a time series data from cases (confirmed, deaths, recovered)
```python
https://covid2019-api.herokuapp.com/timeseries/confirmed
{"confirmed":[{"Province/State":"Anhui","Country/Region":"Mainland_China","Lat":"31.825709999999997","Long":"117.2264","1/21/20 22:00":"","1/22/20 12:00":"1.0","1/23/20 12:00":"9.0","1/24/20 0:00":"15.0","1/24/20 12:00":"15.0","1/25/20 0:00":"39.0","1/25/20 12:00":"39.0","1/25/20 22:00":"60.0","1/26/20 11:00":"60.0","1/26/20 23:00":"70.0","1/27/20 9:00":"70.0","1/27/20 19:00":"70.0","1/27/20 20:30":"106.0","1/28/20 13:00":"106.0","1/28/20 18:00":"106.0","1/28/20 23:00":"152.0","1/29/20 13:30":"152.0","1/29/20 14:30":"152.0","1/29/20 21:00":"200.0","1/30/20 11:00":"200.0","1/31/20 14:00":"237.0","2/1/20 10:00":"297.0","2/2/20 21:00":"408.0","2/3/20 21:00":"480.0","2/4/20 9:40":"480.0","2/4/20 22:00":"530.0","2/5/20 9:00":"530.0","2/5/20 23:00":"591.0","2/6/20 9:00":"591.0","2/6/20 14:20":"591.0","2/7/20 20:13":"665.0","2/7/20 22:50":"733.0","2/8/20 10:24":"733.0","2/8/20 23:04":"779.0","2/9/20 10:30":"779.0","2/9/20 23:20":"830.0","2/10/20 10:30":"830.0","2/10/20 19:30":"830.0","2/11/20 10:50":"860","2/11/20 20:44":"889","2/12/20 10:20":"889","2/12/20 22:00":"910"....n],"dt":"2/11/20 20:44","ts":1581425040.0}

https://covid2019-api.herokuapp.com/timeseries/deaths
{"deaths":[{"Province/State":"Anhui","Country/Region":"Mainland_China","Lat":"31.825709999999997","Long":"117.2264","1/21/20 22:00":"","1/22/20 12:00":"","1/23/20 12:00":"","1/24/20 0:00":"","1/24/20 12:00":"","1/25/20 0:00":"","1/25/20 12:00":"","1/25/20 22:00":"","1/26/20 11:00":"","1/26/20 23:00":"","1/27/20 9:00":"","1/27/20 19:00":"","1/27/20 20:30":"","1/28/20 13:00":"","1/28/20 18:00":"","1/28/20 23:00":"","1/29/20 13:30":"","1/29/20 14:30":"","1/29/20 21:00":"","1/30/20 11:00":"","1/31/20 14:00":"","2/1/20 10:00":"","2/2/20 21:00":"","2/3/20 21:00":"","2/4/20 9:40":"","2/4/20 22:00":"","2/5/20 9:00":"","2/5/20 23:00":"","2/6/20 9:00":"","2/6/20 14:20":"","2/7/20 20:13":"","2/7/20 22:50":"","2/8/20 10:24":"0.0","2/8/20 23:04":"1.0","2/9/20 10:30":"1.0","2/9/20 23:20":"3.0","2/10/20 10:30":"3.0","2/10/20 19:30":"3.0","2/11/20 10:50":"4","2/11/20 20:44":"4","2/12/20 10:20":"4","2/12/20 22:00":"5"...n],"dt":"2/11/20 20:44","ts":1581425040.0}

https://covid2019-api.herokuapp.com/timeseries/recovered
{"recovered":[{"Province/State":"Anhui","Country/Region":"Mainland_China","Lat":"31.825709999999997","Long":"117.2264","1/21/20 22:00":"","1/22/20 12:00":"","1/23/20 12:00":"","1/24/20 0:00":"","1/24/20 12:00":"","1/25/20 0:00":"","1/25/20 12:00":"","1/25/20 22:00":"","1/26/20 11:00":"","1/26/20 23:00":"","1/27/20 9:00":"","1/27/20 19:00":"","1/27/20 20:30":"","1/28/20 13:00":"","1/28/20 18:00":"","1/28/20 23:00":"","1/29/20 13:30":"2.0","1/29/20 14:30":"2.0","1/29/20 21:00":"2.0","1/30/20 11:00":"2.0","1/31/20 14:00":"3.0","2/1/20 10:00":"5.0","2/2/20 21:00":"7.0","2/3/20 21:00":"14.0","2/4/20 9:40":"14.0","2/4/20 22:00":"20.0","2/5/20 9:00":"23.0","2/5/20 23:00":"23.0","2/6/20 9:00":"34.0","2/6/20 14:20":"34.0","2/7/20 20:13":"47.0","2/7/20 22:50":"47.0","2/8/20 10:24":"59.0","2/8/20 23:04":"59.0","2/9/20 10:30":"72.0","2/9/20 23:20":"73.0","2/10/20 10:30":"88.0","2/10/20 19:30":"88.0","2/11/20 10:50":"105","2/11/20 20:44":"108","2/12/20 10:20":"127","2/12/20 22:00":"128".....n],"dt":"2/11/20 20:44","ts":1581425040.0}
```
