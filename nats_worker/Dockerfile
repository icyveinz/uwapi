FROM python:3.11-slim

WORKDIR /nats_worker

COPY . /nats_worker

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/nats_worker

CMD ["python", "consumer.py"]