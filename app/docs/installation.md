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
