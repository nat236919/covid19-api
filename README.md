# NovelCoronaAPI
Novel Corona Virus | API

https://corona-api.herokuapp.com/

This API provides the information regarding '2019 Novel Coronavirus (nCoV)'. It contains a number of confirmed, death, and recovered cases based on the data provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE).

## Dashboard
https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6

## Features
1. The current data (daily updated)
2. Confirmed, Deaths, Recovered
3. The affected countries

## How to use
Send a request to the follwing URLs:

https://corona-api.herokuapp.com/current
```python
{"China":{"confirmed":40160,"deaths":908,"recovered":3286},"Thailand":{"confirmed":32,"deaths":0,"recovered":10},"Japan":{"confirmed":26,"deaths":0,"recovered":1},"South Korea":{"confirmed":27,"deaths":0,"recovered":3},"Taiwan":{"confirmed":18,"deaths":0,"recovered":1},"US":{"confirmed":12,"deaths":0,"recovered":3},"Macau":{"confirmed":10,"deaths":0,"recovered":1},"Hong Kong":{"confirmed":36,"deaths":1,"recovered":0},"Singapore":{"confirmed":43,"deaths":0,"recovered":2},"Vietnam":{"confirmed":14,"deaths":0,"recovered":1},"France":{"confirmed":11,"deaths":0,"recovered":0},"Nepal":{"confirmed":1,"deaths":0,"recovered":0},"Malaysia":{"confirmed":18,"deaths":0,"recovered":1},"Canada":{"confirmed":7,"deaths":0,"recovered":0},"Australia":{"confirmed":15,"deaths":0,"recovered":2},"Cambodia":{"confirmed":1,"deaths":0,"recovered":0},"Sri Lanka":{"confirmed":1,"deaths":0,"recovered":1},"Germany":{"confirmed":14,"deaths":0,"recovered":0},"Finland":{"confirmed":1,"deaths":0,"recovered":0},"United Arab Emirates":{"confirmed":7,"deaths":0,"recovered":0},"Philippines":{"confirmed":3,"deaths":1,"recovered":0},"India":{"confirmed":3,"deaths":0,"recovered":0},"Italy":{"confirmed":3,"deaths":0,"recovered":0},"UK":{"confirmed":3,"deaths":0,"recovered":0},"Russia":{"confirmed":2,"deaths":0,"recovered":0},"Sweden":{"confirmed":1,"deaths":0,"recovered":0},"Spain":{"confirmed":2,"deaths":0,"recovered":0},"Belgium":{"confirmed":1,"deaths":0,"recovered":0},"Others":{"confirmed":64,"deaths":0,"recovered":0},"ts":1581313691.605966}
```

https://corona-api.herokuapp.com/confirmed
```python
{"confirmed":40536}
```

https://corona-api.herokuapp.com/deaths
```python
{"deaths":910}
```

https://corona-api.herokuapp.com/recovered
```python
{"recovered":3312}
```

https://corona-api.herokuapp.com/countries
```python
{"countries":["China","Thailand","Japan","South Korea","Taiwan","US","Macau","Hong Kong","Singapore","Vietnam","France","Nepal","Malaysia","Canada","Australia","Cambodia","Sri Lanka","Germany","Finland","United Arab Emirates","Philippines","India","Italy","UK","Russia","Sweden","Spain","Belgium","Others"]}
```

#### References
https://github.com/CSSEGISandData/2019-nCoV
