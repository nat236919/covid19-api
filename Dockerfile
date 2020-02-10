FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Nuttaphat Arunoprayoch <nat236919@gmail.com>"

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install pandas
RUN pip install requests
RUN pip install csv

COPY ./app /app
