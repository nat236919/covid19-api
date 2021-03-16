<p align="center">
  <a href="https://nat236919.github.io/covid19-api/"><img src="https://i.ibb.co/Wg2yPBq/covid19-api-logo.png"></a>
</p>

<p align="center">
    <em>API for exploring covid-19 cases around the globe powered by FastAPI framework</em>
</p>

<p align="center">
  <a href="https://github.com/nat236919/Covid2019API/issues" target="_blank">
      <img src="https://img.shields.io/github/issues/nat236919/Covid2019API" alt="issues">
  </a>
  <a href="https://github.com/nat236919/Covid2019API/forks" target="_blank">
      <img src="https://img.shields.io/github/forks/nat236919/Covid2019API" alt="forks">
  </a>
  <a href="https://github.com/nat236919/Covid2019API/stars" target="_blank">
      <img src="https://img.shields.io/github/stars/nat236919/Covid2019API" alt="starts">
  </a>
  <a href="https://github.com/nat236919/Covid2019API/blob/master/LICENCE" target="_blank">
      <img src="https://img.shields.io/github/license/nat236919/Covid2019API" alt="licence">
  </a>
  <a href="https://travis-ci.org/github/nat236919/covid19-api" target="_blank">
      <img src="https://travis-ci.org/nat236919/covid19-api.svg?branch=development" alt="build">
  </a>
</p>

# Introduction

This API provides the information regarding '2019 Novel Coronavirus (covid-19)'. It contains a number of confirmed, death, and recovered cases based on the data provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

## Example

* https://covid19.nuttaphat.com/
* https://covid2019-api.herokuapp.com/

## Applications

* [Coronavirus App by YaseenAbdullah](https://github.com/YaseenAbdullah/coronavirus)
* [Covid 19 App - Map, info & help by DavidBarbaran](https://github.com/DavidBarbaran/Covid19App)
* [COVID-19 Visual Explorer by FitnessAI](https://www.fitnessai.com/covid-19-charts-coronavirus-growth-rate-visual-explorer)
* [BAILAM (Data and API Integration)](https://www.bailam.com/covid19)
* [Coronavirus Tech Handbook (Data Tools)](https://coronavirustechhandbook.com/data-tools)

### References

https://github.com/CSSEGISandData/COVID-19

## Branches

|  Branch           |     Feature                      |              Description                                     |
| ----------------- | -------------------------------- |  ----------------------------------------------------------- |
| master            | Docker + Web API                 | For deploying to a server                                    |
| development       | Docker + Web API                 | For testing before merging to Master                         |

## Features

1. The current data (daily updated)
2. Confirmed, Deaths, Recovered
3. The affected countries
4. Individual affected country
5. Timeseries

## How to install

* Run the following command in your command line to run the server

```console
uvicorn main:app
```

## How to install (Docker-compose)

* Run the following command in your command line to run the server

```console
docker-compose up
```

* Or run the server in the background

```console
docker-compose up -d
```

* The port can be changed at <b>docker-compose.override.yml</b>

```yml
version: '3'
services:
  web:
    container_name: "covid19_api_web_container"
    volumes:
      - ./app:/app
    ports:
      - "80:80"
    environment:
      - 'RUN=uvicorn main:app'
```

## How to install (from Dockerhub)

* Download the latest image

```console
docker pull nat236919/covid19-api:latest
```

* Create a container and run

```console
docker run nat236919/covid19-api
```

## How to use API (v2)

Check it out [here](./app/docs/api_docs/v2.md)

## How to use API (v1)

Check it out [here](./app/docs/api_docs/v1.md)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://nuttaphat.azurewebsites.net"><img src="https://avatars0.githubusercontent.com/u/9074112?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nuttaphat Arunoprayoch</b></sub></a><br /><a href="#maintenance-nat236919" title="Maintenance">🚧</a> <a href="https://github.com/nat236919/covid19-api/commits?author=nat236919" title="Code">💻</a> <a href="https://github.com/nat236919/covid19-api/issues?q=author%3Anat236919" title="Bug reports">🐛</a> <a href="https://github.com/nat236919/covid19-api/commits?author=nat236919" title="Documentation">📖</a> <a href="#ideas-nat236919" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/nat236919/covid19-api/pulls?q=is%3Apr+reviewed-by%3Anat236919" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/soapy1"><img src="https://avatars0.githubusercontent.com/u/976973?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sophia Castellarin</b></sub></a><br /><a href="https://github.com/nat236919/covid19-api/commits?author=soapy1" title="Code">💻</a></td>
    <td align="center"><a href="https://keybase.io/endoffile78"><img src="https://avatars2.githubusercontent.com/u/11342054?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jeremy</b></sub></a><br /><a href="https://github.com/nat236919/covid19-api/commits?author=endoffile78" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ChooseYourPlan"><img src="https://avatars2.githubusercontent.com/u/32968964?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tim</b></sub></a><br /><a href="#translation-ChooseYourPlan" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/melsaa"><img src="https://avatars0.githubusercontent.com/u/32761948?v=4?s=100" width="100px;" alt=""/><br /><sub><b>melsaa</b></sub></a><br /><a href="https://github.com/nat236919/covid19-api/commits?author=melsaa" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/owen-duncan-snobel"><img src="https://avatars.githubusercontent.com/u/43126781?v=4?s=100" width="100px;" alt=""/><br /><sub><b>owen-duncan-snobel</b></sub></a><br /><a href="https://github.com/nat236919/covid19-api/commits?author=owen-duncan-snobel" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/maria-sitkovets-03994b159/"><img src="https://avatars.githubusercontent.com/u/28634142?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Maria Sitkovets</b></sub></a><br /><a href="https://github.com/nat236919/covid19-api/commits?author=mSitkovets" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Sponsor this project

<a href="https://www.buymeacoffee.com/HdYFLQU" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
