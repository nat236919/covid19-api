FROM tiangolo/uvicorn-gunicorn:python3.7

# Open port
EXPOSE 80

# Setup work directory
WORKDIR /app
COPY ./app /app

# Install dependencies
COPY ./app/requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
