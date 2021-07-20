FROM tiangolo/uvicorn-gunicorn:python3.8-slim

# Open port
EXPOSE 80

# Setup work directory
WORKDIR /app
COPY app ./

# Install dependencies
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python3-dev libssl-dev && \
    apt-get autoremove -y && \
    pip uninstall pipenv -y
