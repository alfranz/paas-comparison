FROM python:3.11-slim

WORKDIR /app
COPY app/requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

ARG PAAS_ENV='LOCAL'
ENV PAAS_ENV=$PAAS_ENV

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8082"]
