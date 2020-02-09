FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Nuttaphat Arunoprayoch <nat236919@gmail.com>"

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install kaggle
RUN pip install zipfile
RUN pip install pandas

COPY ./app /app
