FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /django_web

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /django_web

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/django_web

COPY entrypoint.sh /django_web/entrypoint.sh

RUN chmod +x /django_web/entrypoint.sh

ENTRYPOINT ["/django_web/entrypoint.sh"]