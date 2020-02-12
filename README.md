# COVID2019-API
Covid2019 | API
<p>
<img src="https://img.shields.io/github/issues/nat236919/NovelCoronaAPI">
<img src="https://img.shields.io/github/forks/nat236919/NovelCoronaAPI">
<img src="https://img.shields.io/github/stars/nat236919/NovelCoronaAPI">
<img src="https://img.shields.io/github/license/nat236919/NovelCoronaAPI">
</p>

https://covid2019-api.herokuapp.com/

This API provides the information regarding '2019 Novel Coronavirus (nCoV)'. It contains a number of confirmed, death, and recovered cases based on the data provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE).

## Dashboard
https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6

## Features
1. The current data (daily updated)
2. Confirmed, Deaths, Recovered
3. The affected countries
4. Individual affected country

## How to use
Send a request to the follwing URLs:

1. Get current data
```python
https://covid2019-api.herokuapp.com/current
{"Mainland_China":{"confirmed":44641,"deaths":1113,"recovered":4730},"Thailand":{"confirmed":33,"deaths":0,"recovered":10},"Japan":{"confirmed":26,"deaths":0,"recovered":9},"South_Korea":{"confirmed":28,"deaths":0,"recovered":4},"Taiwan":{"confirmed":18,"deaths":0,"recovered":1},"US":{"confirmed":13,"deaths":0,"recovered":3},"Macau":{"confirmed":10,"deaths":0,"recovered":1},"Hong_Kong":{"confirmed":49,"deaths":1,"recovered":0},"Singapore":{"confirmed":47,"deaths":0,"recovered":9},"Vietnam":{"confirmed":15,"deaths":0,"recovered":6},"France":{"confirmed":11,"deaths":0,"recovered":0},"Nepal":{"confirmed":1,"deaths":0,"recovered":0},"Malaysia":{"confirmed":18,"deaths":0,"recovered":3},"Canada":{"confirmed":7,"deaths":0,"recovered":0},"Australia":{"confirmed":15,"deaths":0,"recovered":2},"Cambodia":{"confirmed":1,"deaths":0,"recovered":0},"Sri_Lanka":{"confirmed":1,"deaths":0,"recovered":1},"Germany":{"confirmed":16,"deaths":0,"recovered":0},"Finland":{"confirmed":1,"deaths":0,"recovered":1},"United_Arab_Emirates":{"confirmed":8,"deaths":0,"recovered":1},"Philippines":{"confirmed":3,"deaths":1,"recovered":0},"India":{"confirmed":3,"deaths":0,"recovered":0},"Italy":{"confirmed":3,"deaths":0,"recovered":0},"UK":{"confirmed":8,"deaths":0,"recovered":0},"Russia":{"confirmed":2,"deaths":0,"recovered":0},"Sweden":{"confirmed":1,"deaths":0,"recovered":0},"Spain":{"confirmed":2,"deaths":0,"recovered":0},"Belgium":{"confirmed":1,"deaths":0,"recovered":0},"Others":{"confirmed":135,"deaths":0,"recovered":0}}
```

2. Get confirmed cases
```python
https://covid2019-api.herokuapp.com/confirmed
{"confirmed":40536}
```

3. Get deaths
```python
https://covid2019-api.herokuapp.com/deaths
{"deaths":910}
```

4. Get recovered cases
```python
https://covid2019-api.herokuapp.com/recovered
{"recovered":3312}
```

5. Get all the affected countries (Note: Others -> Diamond Princess cruise ship)
```python
https://covid2019-api.herokuapp.com/countries
{"countries":["Mainland_China","Thailand","Japan","South_Korea","Taiwan","US","Macau","Hong_Kong","Singapore","Vietnam","France","Nepal","Malaysia","Canada","Australia","Cambodia","Sri_Lanka","Germany","Finland","United_Arab_Emirates","Philippines","India","Italy","UK","Russia","Sweden","Spain","Belgium","Others"]}
```

6. Get a country by its key name (small letters) or ISO code (Alpha-2 code)
```python
https://covid2019-api.herokuapp.com/country/mainland_china
{"Mainland_China":{"confirmed":44641,"deaths":1113,"recovered":4730}}

https://covid2019-api.herokuapp.com/country/cn
{"Mainland_China":{"confirmed":44641,"deaths":1113,"recovered":4730}}

https://covid2019-api.herokuapp.com/country/kr
{"South_Korea":{"confirmed":28,"deaths":0,"recovered":4}}
```

#### References
https://github.com/CSSEGISandData/COVID-19
