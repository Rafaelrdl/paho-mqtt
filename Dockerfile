FROM python:3.12-slim

WORKDIR /app

COPY application /app/application

ENV PYTHONPATH=/app

RUN pip install paho-mqtt
RUN pip install pymongo

CMD ["python", "application/run.py"]