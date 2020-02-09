FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Nuttaphat Arunoprayoch <nat236919@gmail.com>"

RUN pip install fastapi

COPY ./app /app
